"""
Data models for Connective CRM Reference

Structured representations of elements, workflows, and sections
parsed from the Complete CRM Reference documentation.
"""

from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any
from enum import Enum


class ElementType(Enum):
    """Types of UI elements"""
    BUTTON = "button"
    INPUT = "input"
    SELECT = "select"
    TEXTAREA = "textarea"
    TAB = "tab"
    RICH_TEXT = "rich_text"
    AG_GRID = "ag_grid"
    CHECKBOX = "checkbox"
    UNKNOWN = "unknown"


@dataclass
class Element:
    """
    Represents a UI element in the Connective CRM

    Attributes:
        name: Element identifier (e.g., 'lender', 'propertyType')
        element_type: Type of element (button, select, input, etc.)
        selector: Primary CSS selector
        label: Human-readable label
        section: Which section it belongs to
        options: List of options if dropdown/select
        fallback_selectors: Alternative selectors if primary fails
        notes: Additional usage notes
        framework: Special framework if applicable (Froala, AG-Grid, etc.)
        hidden: Whether element is display:none but accessible
        triggers_modal: Whether clicking opens a modal
        required: Whether field is required
    """
    name: str
    element_type: ElementType
    selector: str
    label: str
    section: str
    options: List[str] = field(default_factory=list)
    fallback_selectors: List[str] = field(default_factory=list)
    notes: str = ""
    framework: Optional[str] = None
    hidden: bool = False
    triggers_modal: bool = False
    required: bool = False

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization"""
        return {
            "name": self.name,
            "type": self.element_type.value,
            "selector": self.selector,
            "label": self.label,
            "section": self.section,
            "options": self.options,
            "fallback_selectors": self.fallback_selectors,
            "notes": self.notes,
            "framework": self.framework,
            "hidden": self.hidden,
            "triggers_modal": self.triggers_modal,
            "required": self.required,
            "option_count": len(self.options) if self.options else 0
        }


@dataclass
class WorkflowStep:
    """
    Single step in a validated workflow

    Attributes:
        number: Step number (1-indexed)
        action: What to do (click, select, fill, etc.)
        selector: CSS selector to target
        description: Human-readable description
        value: Optional value to enter/select
        wait_time: Milliseconds to wait after action
        notes: Additional context
    """
    number: int
    action: str
    selector: str
    description: str
    value: Optional[str] = None
    wait_time: int = 0
    notes: str = ""

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return {
            "step": self.number,
            "action": self.action,
            "selector": self.selector,
            "description": self.description,
            "value": self.value,
            "wait_ms": self.wait_time,
            "notes": self.notes
        }


@dataclass
class Workflow:
    """
    Complete validated workflow for a task

    Attributes:
        name: Workflow identifier (e.g., 'add_note', 'upload_file')
        title: Human-readable title
        steps: List of WorkflowStep objects
        validated: Whether this workflow has been tested
        triggers_modal: Whether workflow involves modal interaction
        framework_notes: Special framework considerations
    """
    name: str
    title: str
    steps: List[WorkflowStep]
    validated: bool = True
    triggers_modal: bool = False
    framework_notes: str = ""

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return {
            "name": self.name,
            "title": self.title,
            "steps": [step.to_dict() for step in self.steps],
            "step_count": len(self.steps),
            "validated": self.validated,
            "triggers_modal": self.triggers_modal,
            "framework_notes": self.framework_notes
        }


@dataclass
class Section:
    """
    Logical section/grouping of elements

    Attributes:
        name: Section name (e.g., 'Financials', 'Attachments')
        purpose: What this section is for
        element_count: Number of elements in section
        elements: List of element names
        navigation_selector: Selector to navigate to this section
    """
    name: str
    purpose: str
    element_count: int
    elements: List[str] = field(default_factory=list)
    navigation_selector: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return {
            "name": self.name,
            "purpose": self.purpose,
            "element_count": self.element_count,
            "elements": self.elements,
            "navigation": self.navigation_selector
        }


@dataclass
class DropdownField:
    """
    Specialized representation of dropdown/select fields

    Attributes:
        field_name: Field identifier
        selector: CSS selector
        options: List of all valid options
        option_count: Number of options
        section: Which section it's in
        dynamic: Whether options are dynamically loaded
    """
    field_name: str
    selector: str
    options: List[str]
    option_count: int
    section: str
    dynamic: bool = False

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return {
            "field": self.field_name,
            "selector": self.selector,
            "option_count": self.option_count,
            "options": self.options,
            "section": self.section,
            "dynamic": self.dynamic
        }


@dataclass
class FuzzyMatchResult:
    """
    Result from fuzzy matching operation

    Attributes:
        original_value: The input value
        matched_value: The best match found
        confidence: Match confidence (0-100)
        is_exact: Whether it was an exact match
        alternatives: Other possible matches
    """
    original_value: str
    matched_value: str
    confidence: float
    is_exact: bool = False
    alternatives: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return {
            "input": self.original_value,
            "match": self.matched_value,
            "confidence": self.confidence,
            "exact": self.is_exact,
            "alternatives": self.alternatives
        }
