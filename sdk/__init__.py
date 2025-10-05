"""
Connective CRM SDK

Python SDK for querying the Complete Connective CRM Reference.
Provides structured access to all 74 elements, 286+ dropdown options,
and validated workflows.

Usage:
    from sdk import CRMReference

    crm = CRMReference()

    # Get selector info
    lender = crm.get_selector("lender")
    print(f"Selector: {lender.selector}")
    print(f"Options: {len(lender.options)}")

    # Validate dropdown value
    is_valid = crm.validate_dropdown("lender", "Commonwealth Bank")

    # Fuzzy match
    match = crm.fuzzy_match("lender", "CBA")
    print(f"CBA matches to: {match.matched_value}")
"""

from .models import (
    Element,
    ElementType,
    Workflow,
    WorkflowStep,
    Section,
    DropdownField,
    FuzzyMatchResult
)
from .query_engine import CRMReference

__version__ = "1.0.0"
__all__ = [
    "CRMReference",
    "Element",
    "ElementType",
    "Workflow",
    "WorkflowStep",
    "Section",
    "DropdownField",
    "FuzzyMatchResult"
]
