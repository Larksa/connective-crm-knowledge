"""
Enhanced JSON Field Extractor

Purpose: Extract ALL fields from a Connective CRM workflow recording JSON
         and output complete field documentation in markdown format.

This script addresses the gap where JSON recordings contain rich metadata
but only dropdown fields were being extracted to the knowledge base.

Usage:
    python tools/extract_all_fields_from_recording.py <recording.json>
"""

import json
import sys
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Set, Optional
from dataclasses import dataclass, field


@dataclass
class FieldMetadata:
    """Complete metadata for a single field"""
    # Core identifiers
    name: str
    label: str = ""
    selector: str = ""
    html_id: str = ""
    data_testid: Optional[str] = None

    # Type information
    element_type: str = ""  # button, input, select, textarea, checkbox
    input_type: str = ""    # text, select-one, button, etc.
    format_type: str = ""   # currency, date, text

    # Context
    section: str = ""
    related_fields: List[str] = field(default_factory=list)
    is_in_form: bool = False
    form_action: str = ""
    form_method: str = ""

    # Behavior
    required: bool = False
    readonly: bool = False
    disabled: bool = False
    auto_save: bool = False
    triggers_modal: bool = False

    # Validation
    pattern: Optional[str] = None
    min_length: Optional[int] = None
    max_length: Optional[int] = None
    min_value: Optional[float] = None
    max_value: Optional[float] = None

    # For select fields
    dropdown_options: List[str] = field(default_factory=list)

    # Selectors
    xpath: str = ""
    css_classes: str = ""
    alternative_selectors: List[str] = field(default_factory=list)
    unstable_selectors: List[Dict[str, str]] = field(default_factory=list)

    # Timing
    wait_after_interaction: float = 0.5
    observed_interactions: int = 0

    # Examples
    recorded_values: List[str] = field(default_factory=list)

    # Button specific
    button_text: str = ""

    def get_primary_selector(self) -> str:
        """Determine the most reliable selector"""
        # Priority: data-testid (without UUID) > ID (without UUID) > name > xpath

        # Check data-testid
        if self.data_testid:
            # If data-testid contains UUID pattern, mark as unstable
            if self._has_uuid(self.data_testid):
                return f"#{self.html_id}" if self.html_id and not self._has_uuid(self.html_id) else self.selector
            return f'[data-testid="{self.data_testid}"]'

        # Check ID
        if self.html_id:
            if self._has_uuid(self.html_id):
                # ID has UUID, try name-based selector
                if self.name:
                    return f'[name="{self.name}"]'
                return self.selector
            return f"#{self.html_id}"

        # Fall back to existing selector
        return self.selector

    def _has_uuid(self, value: str) -> bool:
        """Check if string contains UUID pattern"""
        import re
        uuid_pattern = r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}'
        return bool(re.search(uuid_pattern, value, re.IGNORECASE))

    def get_reliability_rating(self) -> str:
        """Rate selector reliability"""
        primary = self.get_primary_selector()

        if '[data-testid="' in primary and not self._has_uuid(primary):
            return "[RECOMMENDED] (stable data-testid)"
        elif primary.startswith('#') and not self._has_uuid(primary):
            return "[RECOMMENDED] (stable ID)"
        elif '[name="' in primary:
            return "[ALTERNATIVE] (name attribute)"
        elif self._has_uuid(primary):
            return "[CAUTION] (contains UUID - may change)"
        else:
            return "[USE WITH CARE] (complex selector)"


class FieldExtractor:
    """Extract all fields from a recording JSON"""

    def __init__(self, json_path: Path):
        self.json_path = json_path
        with open(json_path, 'r', encoding='utf-8') as f:
            self.data = json.load(f)

        self.fields: Dict[str, FieldMetadata] = {}
        self.workflow_sequence: List[Dict] = []
        self.metadata = self.data.get('metadata', {})

    def extract(self):
        """Main extraction process"""
        events = self.data.get('events', [])

        for event in events:
            event_type = event.get('type', '')

            if event_type in ['browser_click', 'browser_input']:
                self._process_event(event)

        self._identify_related_fields()
        self._calculate_timing()

    def _process_event(self, event: Dict):
        """Process a single event and extract field metadata"""
        # Get form field info (richest source of metadata)
        form_field_info = event.get('formFieldInfo')
        element_context = event.get('elementContext', {})

        # Core identifiers
        field_id = event.get('id', '')
        field_name = event.get('name', '')
        tag_name = event.get('tagName', '')

        # Use formFieldInfo name if available, otherwise event name
        if form_field_info:
            field_name = form_field_info.get('name', field_name)
            field_id = form_field_info.get('id', field_id)

        # Key for tracking (prefer ID, fall back to selector)
        field_key = field_id or event.get('selector', '')
        if not field_key:
            return

        # Create or update field metadata
        if field_key not in self.fields:
            self.fields[field_key] = FieldMetadata(
                name=field_name or field_key,
                html_id=field_id,
                selector=event.get('selector', ''),
                xpath=event.get('xpath', ''),
                element_type=tag_name,
            )

        field = self.fields[field_key]
        field.observed_interactions += 1

        # Extract from formFieldInfo (most complete)
        if form_field_info:
            field.label = form_field_info.get('label', field.label)
            field.input_type = form_field_info.get('type', field.input_type)

            # Data attributes
            data_attrs = form_field_info.get('dataAttributes', {})
            if data_attrs.get('data-testid'):
                field.data_testid = data_attrs['data-testid']

            # Validation
            validation = form_field_info.get('validation', {})
            if validation:
                field.required = validation.get('required', False)
                field.readonly = validation.get('readonly', False)
                field.disabled = validation.get('disabled', False)
                field.pattern = validation.get('pattern')
                field.min_length = validation.get('minLength')
                field.max_length = validation.get('maxLength')
                field.min_value = validation.get('min')
                field.max_value = validation.get('max')

            # Dropdown options
            dropdown = form_field_info.get('dropdown')
            if dropdown:
                options = dropdown.get('options', [])
                for opt in options:
                    opt_text = opt.get('text', '')
                    opt_value = opt.get('value', '')
                    if opt_value and not opt.get('disabled', False):
                        if opt_text not in field.dropdown_options:
                            field.dropdown_options.append(opt_text)

            # Form context
            field.form_action = form_field_info.get('formAction', field.form_action)
            field.form_method = form_field_info.get('formMethod', field.form_method)

        # Extract from element context
        if element_context:
            field.is_in_form = element_context.get('isInForm', False)

            # Related fields
            related = element_context.get('relatedFields', [])
            for rel_field in related:
                rel_name = rel_field.get('name', '')
                rel_id = rel_field.get('id', '')
                if rel_name and rel_name not in field.related_fields:
                    field.related_fields.append(rel_name)
                elif rel_id and rel_id not in field.related_fields:
                    field.related_fields.append(rel_id)

        # Extract button text
        if tag_name == 'button':
            button_text = event.get('text', '')
            if button_text:
                field.button_text = button_text.strip()

        # Extract CSS classes
        field.css_classes = event.get('classes', field.css_classes)

        # Record values
        value = event.get('value')
        if value and value not in field.recorded_values:
            field.recorded_values.append(str(value))

    def _identify_related_fields(self):
        """Cross-reference related fields across all fields"""
        # Build a map of field names to keys
        name_to_key = {}
        for key, field in self.fields.items():
            if field.name:
                name_to_key[field.name] = key

        # Update related fields with actual field objects
        for field in self.fields.values():
            # Remove self-references
            field.related_fields = [
                rf for rf in field.related_fields
                if rf != field.name and rf != field.html_id
            ]

    def _calculate_timing(self):
        """Calculate recommended wait times from event timestamps"""
        # Could analyze event timestamps to determine wait times
        # For now, use defaults
        pass

    def generate_markdown(self, section_name: str = "Unknown") -> str:
        """Generate complete markdown documentation"""

        lines = []

        # Header
        lines.append(f"# {section_name} - Complete Field Reference")
        lines.append("")
        lines.append(f"**Source**: {self.json_path.name}")
        lines.append(f"**Generated**: {self.metadata.get('date', 'Unknown')}")
        lines.append(f"**Recording Duration**: {self.metadata.get('duration', 'Unknown')}")
        lines.append(f"**Total Events**: {self.metadata.get('events_count', 0)}")
        lines.append("")
        lines.append("---")
        lines.append("")

        # Summary
        lines.append("## Summary")
        lines.append("")
        lines.append(f"**Total Fields Discovered**: {len(self.fields)}")
        lines.append("")

        field_types = defaultdict(int)
        for field in self.fields.values():
            field_types[field.element_type] += 1

        lines.append("**Field Types**:")
        for ftype, count in sorted(field_types.items()):
            lines.append(f"- {ftype}: {count}")
        lines.append("")
        lines.append("---")
        lines.append("")

        # Field Definitions
        lines.append("## Field Definitions")
        lines.append("")

        # Sort fields: navigation first, then inputs, then buttons
        def field_sort_key(item):
            key, field = item
            type_priority = {
                'button': 0 if 'tab' in field.button_text.lower() else 3,
                'select': 1,
                'input': 2,
                'textarea': 2,
                'checkbox': 2,
            }
            return (type_priority.get(field.element_type, 99), field.name or key)

        for key, field in sorted(self.fields.items(), key=field_sort_key):
            lines.extend(self._generate_field_section(field))

        return '\n'.join(lines)

    def _generate_field_section(self, field: FieldMetadata) -> List[str]:
        """Generate markdown for a single field"""
        lines = []

        # Use label if available, otherwise name
        title = field.label or field.name or field.html_id
        lines.append(f"### {title}")
        lines.append("")

        # Core Identifiers
        lines.append("**Core Identifiers**")
        lines.append(f"- **Field Name:** `{field.name}`")
        if field.label and field.label != field.name:
            lines.append(f"- **Label:** {field.label}")

        primary_selector = field.get_primary_selector()
        reliability = field.get_reliability_rating()
        lines.append(f"- **Selector:** `{primary_selector}` {reliability}")

        if field.html_id:
            if field._has_uuid(field.html_id):
                lines.append(f"- **ID:** `{field.html_id}` [WARNING] (contains UUID - unstable)")
            else:
                lines.append(f"- **ID:** `{field.html_id}`")

        if field.data_testid:
            if field._has_uuid(field.data_testid):
                lines.append(f"- **data-testid:** `{field.data_testid}` [WARNING] (contains UUID - unstable)")
            else:
                lines.append(f"- **data-testid:** `{field.data_testid}`")

        lines.append("")

        # Type Information
        lines.append("**Type Information**")
        lines.append(f"- **Element Type:** {field.element_type}")
        if field.input_type:
            lines.append(f"- **Input Type:** {field.input_type}")
        if field.element_type == 'button' and field.button_text:
            lines.append(f"- **Button Text:** \"{field.button_text}\"")
        lines.append("")

        # Context
        if field.is_in_form or field.related_fields:
            lines.append("**Context**")
            if field.is_in_form:
                lines.append(f"- **In Form:** Yes")
                if field.form_action:
                    lines.append(f"- **Form Action:** {field.form_action}")
                if field.form_method:
                    lines.append(f"- **Form Method:** {field.form_method}")
            if field.related_fields:
                lines.append(f"- **Related Fields:** {', '.join(f'`{rf}`' for rf in field.related_fields[:5])}")
                if len(field.related_fields) > 5:
                    lines.append(f"  - *({len(field.related_fields) - 5} more...)*")
            lines.append("")

        # Validation
        if (field.required or field.readonly or field.disabled or
            field.pattern or field.min_length or field.max_length):
            lines.append("**Validation**")
            if field.required:
                lines.append(f"- **Required:** Yes")
            if field.readonly:
                lines.append(f"- **Readonly:** Yes")
            if field.disabled:
                lines.append(f"- **Disabled:** Yes")
            if field.pattern:
                lines.append(f"- **Pattern:** `{field.pattern}`")
            if field.min_length or field.max_length:
                lines.append(f"- **Length:** {field.min_length or 0} - {field.max_length or 'unlimited'}")
            lines.append("")

        # Dropdown Options
        if field.dropdown_options:
            lines.append("**Dropdown Options**")
            lines.append(f"- **Total Options:** {len(field.dropdown_options)}")
            lines.append("- **Options:**")
            for opt in sorted(field.dropdown_options):
                if opt and opt not in ['<Clear undefined>', '<Clear >']:
                    lines.append(f"  - {opt}")
            lines.append("")

        # Usage Example
        lines.append("**Usage Example**")
        lines.append("```python")

        if field.element_type == 'select':
            lines.append(f"# Select dropdown")
            lines.append(f"from selenium.webdriver.support.ui import Select")
            lines.append(f"{field.name}_dropdown = driver.find_element(By.CSS_SELECTOR, '{primary_selector}')")
            if field.dropdown_options:
                example_value = field.dropdown_options[0] if field.dropdown_options else "value"
                lines.append(f"Select({field.name}_dropdown).select_by_visible_text('{example_value}')")
            lines.append(f"time.sleep({field.wait_after_interaction})")
        elif field.element_type == 'input':
            lines.append(f"# Input field")
            lines.append(f"{field.name}_field = driver.find_element(By.CSS_SELECTOR, '{primary_selector}')")
            lines.append(f"{field.name}_field.clear()")
            example_value = field.recorded_values[0] if field.recorded_values else "value"
            lines.append(f"{field.name}_field.send_keys('{example_value}')")
            lines.append(f"time.sleep({field.wait_after_interaction})")
        elif field.element_type == 'button':
            lines.append(f"# Click button")
            lines.append(f"{field.name}_button = driver.find_element(By.CSS_SELECTOR, '{primary_selector}')")
            lines.append(f"{field.name}_button.click()")
            lines.append(f"time.sleep({field.wait_after_interaction})")

        lines.append("```")
        lines.append("")

        # Recorded Values
        if field.recorded_values:
            lines.append("**Recorded Values** (from actual usage)")
            for val in field.recorded_values[:5]:
                lines.append(f"- `{val}`")
            if len(field.recorded_values) > 5:
                lines.append(f"- *({len(field.recorded_values) - 5} more values recorded)*")
            lines.append("")

        # Metadata
        lines.append("**Metadata**")
        lines.append(f"- **Interactions Observed:** {field.observed_interactions}")
        if field.xpath:
            lines.append(f"- **XPath:** `{field.xpath}`")
        lines.append("")
        lines.append("---")
        lines.append("")

        return lines


def main():
    if len(sys.argv) < 2:
        print("Usage: python extract_all_fields_from_recording.py <recording.json> [section_name]")
        print("\nExample:")
        print("  python tools/extract_all_fields_from_recording.py recordings/other_income.json 'Other Income'")
        sys.exit(1)

    json_path = Path(sys.argv[1])
    section_name = sys.argv[2] if len(sys.argv) > 2 else json_path.stem.replace('_', ' ').title()

    if not json_path.exists():
        print(f"Error: File not found: {json_path}")
        sys.exit(1)

    print(f"Extracting fields from: {json_path}")
    print(f"Section: {section_name}")
    print()

    extractor = FieldExtractor(json_path)
    extractor.extract()

    print(f"[OK] Extracted {len(extractor.fields)} fields")
    print()

    # Generate markdown
    markdown = extractor.generate_markdown(section_name)

    # Output to file
    output_path = json_path.parent / f"{json_path.stem}_fields_complete.md"
    output_path.write_text(markdown, encoding='utf-8')

    print(f"[OK] Generated complete field documentation:")
    print(f"  {output_path}")
    print()

    # Print summary
    print("Field Summary:")
    for key, field in sorted(extractor.fields.items(), key=lambda x: x[1].name or x[0]):
        primary = field.get_primary_selector()
        print(f"  {field.name or field.html_id:20} | {field.element_type:10} | {primary}")


if __name__ == '__main__':
    main()
