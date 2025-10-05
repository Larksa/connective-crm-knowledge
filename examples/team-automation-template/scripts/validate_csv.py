#!/usr/bin/env python3
"""
CSV Data Validation Script

Validates Connective CRM data in CSV files using the MCP knowledge base.
This example shows how to use the CRM SDK directly in automation scripts.

Usage:
    python scripts/validate_csv.py data/sample_data.csv
"""

import sys
import pandas as pd
from pathlib import Path

# Import from connective-crm-knowledge SDK
# Note: You need to add the SDK to your Python path or install it
# For this example, we assume connective-crm-knowledge is in home directory
import os
home = os.path.expanduser("~")
sys.path.insert(0, os.path.join(home, "connective-crm-knowledge", "sdk"))

from sdk import CRMReference


def validate_csv(csv_path):
    """
    Validate CSV data against Connective CRM knowledge base

    Args:
        csv_path: Path to CSV file
    """
    print(f"🔍 Validating: {csv_path}\n")

    # Load CSV
    try:
        df = pd.read_csv(csv_path)
        print(f"✅ Loaded {len(df)} rows\n")
    except Exception as e:
        print(f"❌ Error loading CSV: {e}")
        return

    # Initialize CRM knowledge
    crm = CRMReference()

    # Validation results
    issues = []
    corrections = []

    # Validate lender column (if exists)
    if 'Lender' in df.columns:
        print("📋 Validating Lenders...")
        for idx, lender in enumerate(df['Lender']):
            if pd.isna(lender):
                continue

            result = crm.validate_and_correct("lender", str(lender))

            if not result['valid']:
                if result['corrected']:
                    corrections.append({
                        'row': idx + 2,  # +2 for header and 0-index
                        'field': 'Lender',
                        'original': lender,
                        'corrected': result['corrected'],
                        'confidence': result['confidence']
                    })
                else:
                    issues.append({
                        'row': idx + 2,
                        'field': 'Lender',
                        'value': lender,
                        'issue': 'No match found'
                    })

        print(f"   ✅ Checked {df['Lender'].notna().sum()} lenders\n")

    # Validate broker column (if exists)
    if 'Broker' in df.columns:
        print("📋 Validating Brokers...")
        for idx, broker in enumerate(df['Broker']):
            if pd.isna(broker):
                continue

            result = crm.validate_dropdown("agent", str(broker))

            if not result:
                # Try fuzzy match
                match = crm.fuzzy_match("agent", str(broker))
                if match.confidence > 70:
                    corrections.append({
                        'row': idx + 2,
                        'field': 'Broker',
                        'original': broker,
                        'corrected': match.matched_value,
                        'confidence': match.confidence
                    })
                else:
                    issues.append({
                        'row': idx + 2,
                        'field': 'Broker',
                        'value': broker,
                        'issue': 'Not in broker list'
                    })

        print(f"   ✅ Checked {df['Broker'].notna().sum()} brokers\n")

    # Print results
    print("\n" + "="*60)
    print("📊 VALIDATION RESULTS")
    print("="*60 + "\n")

    if corrections:
        print(f"⚠️  SUGGESTED CORRECTIONS ({len(corrections)}):\n")
        for c in corrections:
            print(f"   Row {c['row']} - {c['field']}:")
            print(f"      '{c['original']}' → '{c['corrected']}'")
            print(f"      (confidence: {c['confidence']:.1f}%)\n")

    if issues:
        print(f"❌ ISSUES FOUND ({len(issues)}):\n")
        for i in issues:
            print(f"   Row {i['row']} - {i['field']}:")
            print(f"      Value: '{i['value']}'")
            print(f"      Issue: {i['issue']}\n")

    if not corrections and not issues:
        print("✅ All data valid! No issues found.\n")

    # Summary
    print("="*60)
    print(f"Total rows: {len(df)}")
    print(f"Corrections suggested: {len(corrections)}")
    print(f"Issues found: {len(issues)}")
    print("="*60 + "\n")

    # Export corrected CSV (if corrections exist)
    if corrections:
        output_path = csv_path.replace('.csv', '_corrected.csv')

        # Apply corrections
        for c in corrections:
            row_idx = c['row'] - 2  # Convert back to 0-index
            df.at[row_idx, c['field']] = c['corrected']

        df.to_csv(output_path, index=False)
        print(f"💾 Corrected data saved to: {output_path}\n")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scripts/validate_csv.py data/sample_data.csv")
        sys.exit(1)

    csv_file = sys.argv[1]

    if not Path(csv_file).exists():
        print(f"❌ File not found: {csv_file}")
        sys.exit(1)

    validate_csv(csv_file)
