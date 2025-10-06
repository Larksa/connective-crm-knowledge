"""
Query Engine - Main SDK interface for querying CRM reference

Provides high-level methods for:
- Getting selectors
- Validating dropdown values
- Fuzzy matching
- Retrieving workflows
- Searching elements
"""

from pathlib import Path
from typing import Dict, List, Optional, Union
import json

from .models import Element, Workflow, Section, FuzzyMatchResult
from .reference_loader import ReferenceLoader
from .fuzzy_matcher import FuzzyMatcher


class CRMReference:
    """
    Main interface for querying the Connective CRM Reference

    Usage:
        crm = CRMReference()

        # Get element selector
        lender = crm.get_selector("lender")

        # Validate dropdown value
        is_valid = crm.validate_dropdown("lender", "Commonwealth Bank")

        # Fuzzy match
        match = crm.fuzzy_match("lender", "CBA")
    """

    def __init__(self, reference_path: Optional[Path] = None):
        """
        Initialize CRM Reference SDK

        Args:
            reference_path: Path to COMPLETE_CONNECTIVE_CRM_REFERENCE.md
                          If None, uses default location in memory/raw/
        """
        if reference_path is None:
            # Default: ../knowledge/COMPLETE_CONNECTIVE_CRM_REFERENCE.md
            sdk_dir = Path(__file__).parent
            project_root = sdk_dir.parent
            reference_path = project_root / "knowledge" / "COMPLETE_CONNECTIVE_CRM_REFERENCE.md"

        self.reference_path = reference_path
        self.loader = ReferenceLoader(reference_path)

        # Parse the reference (includes loading field mappings)
        self.loader.parse()

        # Initialize fuzzy matcher with field mappings
        self.fuzzy_matcher = FuzzyMatcher(
            min_confidence=80.0,
            field_mappings=self.loader.field_mappings
        )

        # Quick access to parsed data
        self.elements = self.loader.elements
        self.workflows = self.loader.workflows
        self.sections = self.loader.sections
        self.dropdown_fields = self.loader.dropdown_fields
        self.field_mappings = self.loader.field_mappings

    def get_selector(self, field_name: str) -> Optional[Element]:
        """
        Get element with selector information

        Args:
            field_name: Name of the field (e.g., 'lender', 'propertyType')

        Returns:
            Element object with selector and metadata, or None if not found
        """
        # Direct lookup
        if field_name in self.elements:
            return self.elements[field_name]

        # Case-insensitive search
        field_lower = field_name.lower()
        for name, element in self.elements.items():
            if name.lower() == field_lower:
                return element

        # Partial match search
        for name, element in self.elements.items():
            if field_lower in name.lower() or name.lower() in field_lower:
                return element

        return None

    def get_all_options(self, field_name: str) -> List[str]:
        """
        Get all valid options for a dropdown field

        Args:
            field_name: Name of the dropdown field

        Returns:
            List of valid options, or empty list if not found
        """
        element = self.get_selector(field_name)
        if element and element.options:
            return element.options

        # Check dropdown_fields directly
        if field_name in self.dropdown_fields:
            return self.dropdown_fields[field_name].options

        return []

    def validate_dropdown(self, field_name: str, value: str) -> bool:
        """
        Check if a value is valid for a dropdown field

        Args:
            field_name: Name of the dropdown field
            value: Value to validate

        Returns:
            True if value is valid (case-insensitive match)
        """
        options = self.get_all_options(field_name)
        if not options:
            return False

        value_lower = value.strip().lower()
        return any(opt.strip().lower() == value_lower for opt in options)

    def fuzzy_match(
        self,
        field_name: str,
        value: str,
        auto_correct: bool = False
    ) -> FuzzyMatchResult:
        """
        Find best match for a value using fuzzy matching

        Args:
            field_name: Name of the dropdown field
            value: Value to match
            auto_correct: If True, returns the matched value; if False, returns original

        Returns:
            FuzzyMatchResult with match info and confidence
        """
        options = self.get_all_options(field_name)
        if not options:
            return FuzzyMatchResult(
                original_value=value,
                matched_value=value if not auto_correct else "",
                confidence=0.0
            )

        # Pass field_name to enable field-specific mapping lookup
        result = self.fuzzy_matcher.match(
            value,
            options,
            field_name=field_name
        )

        if not auto_correct:
            # Keep original value in the result but show what it matched to
            return result

        # Auto-correct: use matched value if confidence is high enough
        if self.fuzzy_matcher.is_valid_match(result):
            return result
        else:
            # Low confidence, don't auto-correct
            result.matched_value = value
            return result

    def get_workflow(self, workflow_name: str) -> Optional[Workflow]:
        """
        Get a validated workflow by name

        Args:
            workflow_name: Name of workflow (e.g., 'add_note', 'upload_file')

        Returns:
            Workflow object with steps, or None if not found
        """
        return self.workflows.get(workflow_name)

    def list_workflows(self) -> List[str]:
        """
        Get list of all available workflow names

        Returns:
            List of workflow names
        """
        return list(self.workflows.keys())

    def get_section(self, section_name: str) -> Optional[Section]:
        """
        Get section information

        Args:
            section_name: Name of the section

        Returns:
            Section object, or None if not found
        """
        return self.sections.get(section_name)

    def find_in_section(
        self,
        section_name: str,
        search_term: Optional[str] = None
    ) -> List[Element]:
        """
        Get all elements in a section, optionally filtered by search term

        Args:
            section_name: Name of the section
            search_term: Optional search term to filter elements

        Returns:
            List of matching Element objects
        """
        section = self.get_section(section_name)
        if not section:
            return []

        elements = [
            self.elements[elem_name]
            for elem_name in section.elements
            if elem_name in self.elements
        ]

        if search_term:
            search_lower = search_term.lower()
            elements = [
                elem for elem in elements
                if search_lower in elem.name.lower()
                or search_lower in elem.label.lower()
            ]

        return elements

    def search_elements(self, query: str) -> List[Element]:
        """
        Search for elements matching a query across all sections

        Args:
            query: Search term

        Returns:
            List of matching Element objects
        """
        query_lower = query.lower()
        results = []

        for element in self.elements.values():
            if (query_lower in element.name.lower()
                or query_lower in element.label.lower()
                or query_lower in element.section.lower()
                or query_lower in element.selector.lower()):
                results.append(element)

        return results

    def get_element_by_selector(self, selector: str) -> Optional[Element]:
        """
        Find element by its CSS selector

        Args:
            selector: CSS selector (e.g., '#lender', '[data-testid="Add"]')

        Returns:
            Element object, or None if not found
        """
        for element in self.elements.values():
            if element.selector == selector:
                return element
            if selector in element.fallback_selectors:
                return element

        return None

    def validate_and_correct(
        self,
        field_name: str,
        value: str,
        min_confidence: float = 80.0
    ) -> Dict:
        """
        Validate a value and provide correction if needed

        Args:
            field_name: Name of the dropdown field
            value: Value to validate
            min_confidence: Minimum confidence for auto-correction

        Returns:
            Dictionary with validation result and suggested correction
        """
        # Check if valid
        is_valid = self.validate_dropdown(field_name, value)

        if is_valid:
            return {
                "valid": True,
                "original": value,
                "corrected": value,
                "confidence": 100.0,
                "message": "Value is valid"
            }

        # Try fuzzy match
        match = self.fuzzy_match(field_name, value)

        if match.confidence >= min_confidence:
            return {
                "valid": False,
                "original": value,
                "corrected": match.matched_value,
                "confidence": match.confidence,
                "message": f"Corrected '{value}' to '{match.matched_value}' (confidence: {match.confidence:.1f}%)",
                "alternatives": match.alternatives
            }
        else:
            # Get suggestions
            options = self.get_all_options(field_name)
            suggestions = self.fuzzy_matcher.suggest_corrections(value, options, max_suggestions=3)

            return {
                "valid": False,
                "original": value,
                "corrected": None,
                "confidence": match.confidence,
                "message": f"No high-confidence match found for '{value}'",
                "suggestions": suggestions
            }

    def get_summary(self) -> Dict:
        """
        Get summary statistics about the reference

        Returns:
            Dictionary with counts and stats
        """
        return {
            "total_elements": len(self.elements),
            "total_sections": len(self.sections),
            "total_workflows": len(self.workflows),
            "total_dropdown_fields": len(self.dropdown_fields),
            "total_dropdown_options": sum(
                len(options) for options in
                [elem.options for elem in self.elements.values() if elem.options]
            ),
            "total_field_mappings": len(self.field_mappings),
            "field_mappings_loaded": list(self.field_mappings.keys()),
            "sections": list(self.sections.keys()),
            "workflows": list(self.workflows.keys())
        }

    def export_to_json(self, output_path: Path):
        """
        Export all reference data to JSON

        Args:
            output_path: Path to output JSON file
        """
        data = {
            "elements": {
                name: elem.to_dict()
                for name, elem in self.elements.items()
            },
            "workflows": {
                name: workflow.to_dict()
                for name, workflow in self.workflows.items()
            },
            "sections": {
                name: section.to_dict()
                for name, section in self.sections.items()
            },
            "summary": self.get_summary()
        }

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def __repr__(self) -> str:
        """String representation"""
        summary = self.get_summary()
        return (
            f"CRMReference("
            f"elements={summary['total_elements']}, "
            f"workflows={summary['total_workflows']}, "
            f"sections={summary['total_sections']})"
        )
