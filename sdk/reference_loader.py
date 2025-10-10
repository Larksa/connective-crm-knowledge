"""
Reference Loader - Parse Complete CRM Reference markdown into Python objects

Extracts all elements, workflows, and dropdown options from the
COMPLETE_CONNECTIVE_CRM_REFERENCE.md file.
"""

import re
import json
from pathlib import Path
from typing import Dict, List, Tuple
from .models import (
    Element,
    ElementType,
    Workflow,
    WorkflowStep,
    Section,
    DropdownField
)


class ReferenceLoader:
    """
    Parses the Complete Connective CRM Reference markdown file
    into structured Python objects
    """

    def __init__(self, reference_path: Path):
        """
        Initialize loader with path to reference markdown

        Args:
            reference_path: Path to COMPLETE_CONNECTIVE_CRM_REFERENCE.md
        """
        self.reference_path = reference_path
        self.knowledge_dir = reference_path.parent  # knowledge/ directory
        self.content = self._load_file()

        # Parsed data
        self.elements: Dict[str, Element] = {}
        self.workflows: Dict[str, Workflow] = {}
        self.sections: Dict[str, Section] = {}
        self.dropdown_fields: Dict[str, DropdownField] = {}

        # Field mappings (loaded from JSON files)
        self.field_mappings: Dict[str, Dict] = {}

    def _load_file(self) -> str:
        """Load markdown file content"""
        if not self.reference_path.exists():
            raise FileNotFoundError(
                f"Reference file not found: {self.reference_path}"
            )
        return self.reference_path.read_text(encoding='utf-8')

    def parse(self):
        """Parse the complete reference document"""
        self._parse_sections()
        self._parse_elements()
        self._parse_dropdown_options()
        self._parse_workflows()
        self._load_field_mappings()

    def _parse_sections(self):
        """Extract section information"""
        # Pattern: ### Section Name\n\n**Purpose**: ...
        section_pattern = r'### (.+?) Section\n\n\*\*Purpose\*\*: (.+?)\n\*\*Total Elements\*\*: (\d+)'

        for match in re.finditer(section_pattern, self.content):
            name = match.group(1)
            purpose = match.group(2)
            element_count = int(match.group(3))

            section = Section(
                name=name,
                purpose=purpose,
                element_count=element_count
            )
            self.sections[name] = section

    def _parse_elements(self):
        """Extract all elements from element tables"""

        # Parse each section's element table
        sections_to_parse = [
            ("Attachments", ElementType.INPUT),
            ("BID & NCCP", ElementType.BUTTON),
            ("Calculations", None),  # Mixed types
            ("Details", ElementType.BUTTON),
            ("Financials", None),  # Mixed types
            ("Navigation", ElementType.TAB),
            ("Notes", None),  # Mixed types
            ("Questionnaires", ElementType.AG_GRID),
            ("Unknown/Dashboard", None)  # Mixed types
        ]

        for section_name, default_type in sections_to_parse:
            self._parse_section_elements(section_name, default_type)

    def _parse_section_elements(self, section_name: str, default_type: ElementType = None):
        """Parse elements from a specific section"""

        # Find section in content
        section_start = self.content.find(f"### {section_name} Section")
        if section_start == -1:
            return

        # Find next section or end
        next_section = self.content.find("###", section_start + 1)
        section_content = self.content[section_start:next_section] if next_section != -1 else self.content[section_start:]

        # Parse element table (markdown table format)
        # | Element | Type | Selector | ...
        table_pattern = r'\| \*\*(.+?)\*\* \| (.+?) \| `(.+?)` \|'

        for match in re.finditer(table_pattern, section_content):
            name = match.group(1).strip()
            type_str = match.group(2).strip()
            selector = match.group(3).strip()

            # Determine element type
            element_type = self._parse_element_type(type_str, default_type)

            element = Element(
                name=name,
                element_type=element_type,
                selector=selector,
                label=name,  # Will be refined if label column exists
                section=section_name
            )

            self.elements[name] = element

            # Add to section's element list
            if section_name in self.sections:
                self.sections[section_name].elements.append(name)

    def _parse_element_type(self, type_str: str, default: ElementType = None) -> ElementType:
        """Convert string type to ElementType enum"""
        type_map = {
            "button": ElementType.BUTTON,
            "input": ElementType.INPUT,
            "select": ElementType.SELECT,
            "textarea": ElementType.TEXTAREA,
            "tab": ElementType.TAB,
            "rich_text": ElementType.RICH_TEXT,
            "ag_grid": ElementType.AG_GRID,
            "checkbox": ElementType.CHECKBOX
        }

        return type_map.get(type_str.lower(), default or ElementType.UNKNOWN)

    def _parse_dropdown_options(self):
        """Extract all dropdown fields with their complete option lists"""

        # Pattern: ### N. Field Name (XX options)
        # **Selector**: `#selector`
        # **Section**: SectionName
        # ```
        # 1. Option 1
        # 2. Option 2
        # ...

        dropdown_pattern = r'### (\d+)\. (.+?) \((\d+) options?\)\n\*\*Selector\*\*: `(.+?)`\n\*\*Section\*\*: (.+?)\n\n```\n([\s\S]+?)```'

        for match in re.finditer(dropdown_pattern, self.content):
            field_name = match.group(2).strip()
            option_count = int(match.group(3))
            selector = match.group(4).strip()
            section = match.group(5).strip()
            options_text = match.group(6)

            # Parse options list
            options = []
            option_lines = options_text.strip().split('\n')
            for line in option_lines:
                # Format: "1.  Option Name" or "10. Option Name"
                option_match = re.match(r'\d+\.\s+(.+)', line.strip())
                if option_match:
                    options.append(option_match.group(1).strip())

            dropdown = DropdownField(
                field_name=field_name,
                selector=selector,
                options=options,
                option_count=len(options),
                section=section
            )

            self.dropdown_fields[field_name] = dropdown

            # Update element if exists
            # Find element by selector or create
            element_key = self._find_element_by_selector(selector)
            if element_key:
                self.elements[element_key].options = options
            else:
                # Create element from dropdown info
                element = Element(
                    name=field_name,
                    element_type=ElementType.SELECT,
                    selector=selector,
                    label=field_name,
                    section=section,
                    options=options
                )
                self.elements[field_name] = element

    def _find_element_by_selector(self, selector: str) -> str:
        """Find element key by selector"""
        for key, element in self.elements.items():
            if element.selector == selector:
                return key
        return None

    def _parse_workflows(self):
        """Extract validated workflows"""

        # Parse all validated workflows:
        # 1. Add Note to Opportunity
        # 2. Upload File to Attachments
        # 3. Complete Questionnaire
        # 4. Add Liability Entry (from jlall.json recording)
        # 5. Add Asset (Other) (from jlall.json recording)
        # 6. Add Living Expense Entry (from jlall.json recording)
        # 7. Add Other Income Entry (from other_income recording)
        # 8. Add Real Estate Asset (from connective-realestate-workflow recording)
        # 9. Complete Borrowing Capacity Calculation (from connective-calc-borrowing-capacity recording)
        # 10. Login and Dashboard Navigation (from shared workflow components)

        workflows_to_parse = [
            ("add_note", "Add Note to Opportunity"),
            ("upload_file", "Upload File to Attachments"),
            ("complete_questionnaire", "Complete Questionnaire"),
            ("add_liability", "Add Liability Entry"),
            ("add_asset_other", "Add Asset (Other)"),
            ("add_living_expense", "Add Living Expense Entry"),
            ("add_other_income", "Add Other Income Entry"),
            ("add_real_estate", "Add Real Estate Asset"),
            ("borrowing_capacity", "Complete Borrowing Capacity Calculation"),
            ("login_to_crm", "Login and Dashboard Navigation (Unified)")
        ]

        for workflow_id, workflow_title in workflows_to_parse:
            workflow = self._parse_workflow_section(workflow_id, workflow_title)
            if workflow:
                self.workflows[workflow_id] = workflow

    def _parse_workflow_section(self, workflow_id: str, title: str) -> Workflow:
        """Parse a specific workflow section"""

        # Find workflow in content
        section_marker = f"### Workflow"
        workflow_start = self.content.find(section_marker)

        # Look for workflow by title
        title_pos = self.content.find(title, workflow_start)
        if title_pos == -1:
            return None

        # Find steps section
        steps_start = self.content.find("**Steps**:", title_pos)
        if steps_start == -1:
            return None

        # Find end of workflow (next ### or ---)
        steps_end = self.content.find("\n---\n", steps_start)
        if steps_end == -1:
            steps_end = self.content.find("\n### ", steps_start + 1)

        workflow_content = self.content[steps_start:steps_end]

        # Parse individual steps
        # Format: N. **Step Title**
        #         - Selector: `...`
        #         - Action: ...
        steps = []
        step_pattern = r'(\d+)\. \*\*(.+?)\*\*\n\s+- Selector: `(.+?)`\n\s+- Action: (.+?)(?:\n|$)'

        for match in re.finditer(step_pattern, workflow_content):
            step_num = int(match.group(1))
            description = match.group(2)
            selector = match.group(3)
            action = match.group(4)

            step = WorkflowStep(
                number=step_num,
                action=action.strip(),
                selector=selector,
                description=description
            )
            steps.append(step)

        if not steps:
            return None

        return Workflow(
            name=workflow_id,
            title=title,
            steps=steps,
            validated=True
        )

    def _load_field_mappings(self):
        """Load field mapping JSON files for fuzzy matching"""
        mappings_dir = self.knowledge_dir / "mappings"

        if not mappings_dir.exists():
            # Mappings directory doesn't exist yet, skip
            return

        # Mapping files to load
        mapping_files = [
            "expense_mappings.json",
            "lender_mappings.json",
            "agent_mappings.json",
            "property_type_mappings.json",
            "liability_type_mappings.json",
            "asset_type_mappings.json",
            "motor_vehicle_type_mappings.json",
            "asset_value_basis_mappings.json",
            "income_other_type_mappings.json"
        ]

        for mapping_file in mapping_files:
            file_path = mappings_dir / mapping_file
            if file_path.exists():
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        # Extract field name from filename (e.g., "expense_mappings.json" -> "expense")
                        field_name = mapping_file.replace("_mappings.json", "")
                        self.field_mappings[field_name] = data
                except Exception as e:
                    # Log warning but continue
                    print(f"Warning: Could not load {mapping_file}: {e}")

    def get_field_mapping(self, field_name: str) -> Dict:
        """
        Get mapping data for a specific field

        Args:
            field_name: Name of the field (e.g., 'expense', 'lender', 'agent')

        Returns:
            Mapping dictionary or empty dict if not found
        """
        return self.field_mappings.get(field_name, {})

    def get_all_mappings(self) -> Dict[str, Dict]:
        """Get all loaded field mappings"""
        return self.field_mappings

    def get_summary(self) -> Dict:
        """Get summary statistics"""
        return {
            "total_elements": len(self.elements),
            "total_sections": len(self.sections),
            "total_workflows": len(self.workflows),
            "total_dropdown_fields": len(self.dropdown_fields),
            "total_dropdown_options": sum(
                len(df.options) for df in self.dropdown_fields.values()
            ),
            "total_field_mappings": len(self.field_mappings)
        }
