"""
Fuzzy Matcher - Smart value matching for dropdown options

Handles:
- Abbreviations: "CBA" → "Commonwealth Bank"
- Typos: "Commonwelth" → "Commonwealth Bank"
- Partial matches: "Commonwealth" → "Commonwealth Bank"
- Case insensitivity
"""

from typing import List, Optional
from rapidfuzz import fuzz, process
from .models import FuzzyMatchResult


class FuzzyMatcher:
    """
    Smart matching for dropdown values using fuzzy string matching
    """

    # Common abbreviations in banking/finance
    ABBREVIATIONS = {
        # Banks
        "CBA": "Commonwealth Bank",
        "NAB": "National Australia Bank",
        "ANZ": "ANZ",
        "WBC": "Westpac",
        "BOQ": "Bank of Queensland",
        "ING": "ING",
        "ME": "ME Bank",

        # Property types (common abbreviations)
        "APT": "Apartment/Unit/Flat",
        "UNIT": "Apartment/Unit/Flat",
        "HOUSE": "Fully Detached House",

        # Transaction types
        "FHB": "FHO",  # First Home Buyer → First Home Owner
        "REFI": "Refinance",

        # Frequencies
        "WEEKLY": "Weekly",
        "FORT": "Fortnightly",
        "MTH": "Monthly",
        "MONTH": "Monthly",
        "YR": "Annual",
        "YEAR": "Annual"
    }

    def __init__(self, min_confidence: float = 80.0, field_mappings: dict = None):
        """
        Initialize fuzzy matcher

        Args:
            min_confidence: Minimum confidence threshold (0-100) for matches
            field_mappings: Optional field-specific mappings from reference_loader
        """
        self.min_confidence = min_confidence
        self.field_mappings = field_mappings or {}

    def match(
        self,
        value: str,
        options: List[str],
        use_abbreviations: bool = True,
        field_name: str = None
    ) -> FuzzyMatchResult:
        """
        Find best match for a value in a list of options

        Args:
            value: Input value to match
            options: List of valid options
            use_abbreviations: Whether to check abbreviation dict first
            field_name: Optional field name for field-specific mapping lookup

        Returns:
            FuzzyMatchResult with best match and confidence
        """
        if not value or not options:
            return FuzzyMatchResult(
                original_value=value,
                matched_value="",
                confidence=0.0
            )

        # Check for exact match first (case insensitive)
        for option in options:
            if value.strip().lower() == option.strip().lower():
                return FuzzyMatchResult(
                    original_value=value,
                    matched_value=option,
                    confidence=100.0,
                    is_exact=True
                )

        # Check field-specific mappings FIRST (from JSON mapping files)
        # Normalize field_name: lowercase and replace spaces with underscores
        normalized_field_name = field_name.lower().replace(' ', '_').replace('/', '_') if field_name else None

        if normalized_field_name and normalized_field_name in self.field_mappings:
            mapping_data = self.field_mappings[normalized_field_name]
            mappings = mapping_data.get("mappings", {})

            # Search through mappings for value
            for crm_value, excel_variations in mappings.items():
                # Check if value matches any variation (case-insensitive)
                for variation in excel_variations:
                    if value.strip().lower() == variation.strip().lower():
                        # Found in mappings - return with 100% confidence
                        return FuzzyMatchResult(
                            original_value=value,
                            matched_value=crm_value,
                            confidence=100.0,
                            is_exact=True
                        )

        # Check abbreviations dictionary (fallback)
        if use_abbreviations:
            value_upper = value.strip().upper()
            if value_upper in self.ABBREVIATIONS:
                abbreviated = self.ABBREVIATIONS[value_upper]
                # Find this in options
                for option in options:
                    if abbreviated.lower() in option.lower():
                        return FuzzyMatchResult(
                            original_value=value,
                            matched_value=option,
                            confidence=95.0,  # High confidence for known abbreviation
                            is_exact=False
                        )

        # Fuzzy match using rapidfuzz
        # Use token_sort_ratio for better handling of word order differences
        matches = process.extract(
            value,
            options,
            scorer=fuzz.token_sort_ratio,
            limit=5  # Get top 5 matches
        )

        if not matches:
            return FuzzyMatchResult(
                original_value=value,
                matched_value="",
                confidence=0.0
            )

        # Best match
        best_match, best_score, _ = matches[0]

        # Get alternatives (matches above threshold)
        alternatives = [
            match[0] for match in matches[1:]
            if match[1] >= self.min_confidence
        ]

        return FuzzyMatchResult(
            original_value=value,
            matched_value=best_match,
            confidence=best_score,
            is_exact=False,
            alternatives=alternatives
        )

    def is_valid_match(self, result: FuzzyMatchResult) -> bool:
        """
        Determine if a match result is acceptable

        Args:
            result: FuzzyMatchResult to evaluate

        Returns:
            True if confidence meets threshold
        """
        return result.confidence >= self.min_confidence

    def add_abbreviation(self, abbr: str, full_form: str):
        """
        Add custom abbreviation to the dictionary

        Args:
            abbr: Abbreviation (will be uppercased)
            full_form: Full form to match
        """
        self.ABBREVIATIONS[abbr.upper()] = full_form

    def batch_match(
        self,
        values: List[str],
        options: List[str]
    ) -> List[FuzzyMatchResult]:
        """
        Match multiple values at once

        Args:
            values: List of input values
            options: List of valid options

        Returns:
            List of FuzzyMatchResults
        """
        return [self.match(value, options) for value in values]

    def suggest_corrections(
        self,
        value: str,
        options: List[str],
        max_suggestions: int = 3
    ) -> List[str]:
        """
        Get correction suggestions for an invalid value

        Args:
            value: Invalid input value
            options: List of valid options
            max_suggestions: Maximum number of suggestions

        Returns:
            List of suggested corrections
        """
        matches = process.extract(
            value,
            options,
            scorer=fuzz.token_sort_ratio,
            limit=max_suggestions
        )

        return [match[0] for match in matches if match[1] >= 60.0]
