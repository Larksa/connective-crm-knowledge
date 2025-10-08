"""
Compare extracted fields from recording with existing documentation
to identify NEW, VERIFIED, and ENHANCED metadata
"""

import re
from pathlib import Path
from collections import defaultdict

# Load extracted fields
extracted_path = Path(r'C:\Users\JamesLarkey\Documents\connective-crm-knowledge\knowledge\sections\jlall_extracted_fields.md')
extracted_content = extracted_path.read_text(encoding='utf-8')

# Load existing docs
liabilities_path = Path(r'C:\Users\JamesLarkey\Documents\connective-crm-knowledge\knowledge\sections\liabilities.md')
assets_path = Path(r'C:\Users\JamesLarkey\Documents\connective-crm-knowledge\knowledge\sections\assets_other.md')
living_path = Path(r'C:\Users\JamesLarkey\Documents\connective-crm-knowledge\knowledge\sections\living_expenses.md')
main_ref_path = Path(r'C:\Users\JamesLarkey\Documents\connective-crm-knowledge\knowledge\COMPLETE_CONNECTIVE_CRM_REFERENCE.md')

liabilities_content = liabilities_path.read_text(encoding='utf-8')
assets_content = assets_path.read_text(encoding='utf-8')
living_content = living_path.read_text(encoding='utf-8')
main_ref_content = main_ref_path.read_text(encoding='utf-8')

# Extract field names from extracted recording
extracted_fields = {}
field_sections = re.findall(r'### (.+?)\n\n\*\*Core Identifiers\*\*(.*?)(?=\n---|\Z)', extracted_content, re.DOTALL)
for field_title, field_content in field_sections:
    # Get field name
    field_name_match = re.search(r'- \*\*Field Name:\*\* `(.+?)`', field_content)
    selector_match = re.search(r'- \*\*Selector:\*\* `(.+?)`', field_content)
    data_testid_match = re.search(r'- \*\*data-testid:\*\* `(.+?)`', field_content)
    element_type_match = re.search(r'- \*\*Element Type:\*\* (\w+)', field_content)

    if field_name_match:
        field_name = field_name_match.group(1)
        extracted_fields[field_name] = {
            'title': field_title,
            'selector': selector_match.group(1) if selector_match else 'Unknown',
            'data_testid': data_testid_match.group(1) if data_testid_match else None,
            'type': element_type_match.group(1) if element_type_match else 'Unknown',
            'content': field_content
        }

print("=" * 100)
print("FIELD EXTRACTION COMPARISON - jlall.json vs Existing Documentation")
print("=" * 100)
print(f"\nTotal fields extracted from recording: {len(extracted_fields)}")
print()

# Categorize fields by section
liability_fields = ['liabilityType', 'institution', 'accountName', 'accountBSB', 'accountNumber',
                   'balance', 'limit', 'accountRepayment', 'accountRepaymentFrequency',
                   'accountClearingFromLoan', 'priority']

asset_fields = ['assetType', 'assetName', 'assetValue', 'valueBasis', 'vehicleType']

living_expense_fields = ['frequency', 'amount']  # These appear in living expenses too

# Check Liabilities
print("=" * 100)
print("LIABILITIES SECTION ANALYSIS")
print("=" * 100)
print()

liability_in_recording = {k: v for k, v in extracted_fields.items() if k in liability_fields or k == 'name'}
print(f"Liability fields found in recording: {len(liability_in_recording)}")
print()

for field_name, field_data in sorted(liability_in_recording.items()):
    documented = field_name in liabilities_content or field_data['selector'] in liabilities_content

    if documented:
        # Check if data-testid is in docs
        has_data_testid_in_docs = 'data-testid' in liabilities_content and field_name in liabilities_content

        print(f"[VERIFIED] {field_name}")
        print(f"  Selector: {field_data['selector']}")
        if field_data['data_testid']:
            if has_data_testid_in_docs:
                print(f"  data-testid: {field_data['data_testid']} (already documented)")
            else:
                print(f"  [ENHANCE] data-testid: {field_data['data_testid']} (ADD THIS)")
        print()
    else:
        print(f"[NEW] {field_name} - NOT YET DOCUMENTED")
        print(f"  Selector: {field_data['selector']}")
        if field_data['data_testid']:
            print(f"  data-testid: {field_data['data_testid']}")
        print()

# Check Assets-Other
print("=" * 100)
print("ASSETS-OTHER SECTION ANALYSIS")
print("=" * 100)
print()

# Look for name field with asset context
asset_name_fields = [k for k, v in extracted_fields.items() if k == 'name' and 'asset' in v['selector'].lower()]
print(f"Asset type field (name): {len(asset_name_fields)} found")
if asset_name_fields:
    field = extracted_fields['name']
    print(f"  Selector: {field['selector']}")
    if field['data_testid']:
        print(f"  data-testid: {field['data_testid']}")

        # Check if documented
        if 'asset-type-0' in assets_content:
            print(f"  [VERIFIED] Documented as asset-type-{{index}}")
        else:
            print(f"  [ENHANCE] Add data-testid pattern to docs")
print()

# Check valueBasis
if 'valueBasis' in extracted_fields:
    field = extracted_fields['valueBasis']
    print(f"[VERIFIED] valueBasis")
    print(f"  Selector: {field['selector']}")

    # Check if marked as "assumed"
    if 'assumed' in assets_content and 'valueBasis' in assets_content:
        print(f"  [NOTE] Currently may be marked as 'assumed' - recording CONFIRMS it")
    print()

# Check ALL selectors mentioned in existing docs
print("=" * 100)
print("SELECTOR VERIFICATION")
print("=" * 100)
print()

# Find selectors in existing docs that we can now verify
doc_selectors = {
    '#institution': 'institution',
    '#accountName': 'accountName',
    '#accountBSB': 'accountBSB',
    '#accountNumber': 'accountNumber',
    '#value': 'balance',
    '#limit': 'limit',
    '#accountRepayment': 'accountRepayment',
    '#accountRepaymentFrequency': 'accountRepaymentFrequency',
    '[name="accountClearingFromLoan"]': 'accountClearingFromLoan',
    '#valueBasis': 'valueBasis',
    '#vehicleType': 'vehicleType',
}

for documented_selector, field_name in doc_selectors.items():
    if field_name in extracted_fields:
        extracted_selector = extracted_fields[field_name]['selector']

        if documented_selector in extracted_selector or extracted_selector == documented_selector:
            print(f"[CONFIRMED] {field_name}: {documented_selector}")
        else:
            print(f"[MISMATCH] {field_name}")
            print(f"  Documented: {documented_selector}")
            print(f"  Recording:  {extracted_selector}")
    else:
        # Check if it's named differently in recording
        alt_matches = [k for k, v in extracted_fields.items() if documented_selector in v['selector']]
        if alt_matches:
            print(f"[RENAME] {field_name} recorded as: {alt_matches[0]}")
        else:
            print(f"[NOT FOUND] {field_name} not in this recording")

print()
print("=" * 100)
print("CRITICAL FINDINGS")
print("=" * 100)
print()

# Check for UUID warnings
uuid_warnings = [k for k, v in extracted_fields.items() if 'UUID' in v.get('content', '') and 'WARNING' in v.get('content', '')]
print(f"Fields with UUID stability warnings: {len(uuid_warnings)}")
for field in uuid_warnings:
    print(f"  - {field}: {extracted_fields[field]['selector'][:60]}...")

print()

# Check for checkbox fields
checkbox_fields = [k for k, v in extracted_fields.items() if v['type'] == 'input' and 'checkbox' in v.get('content', '').lower()]
print(f"Checkbox fields found: {len(checkbox_fields)}")
for field in checkbox_fields:
    print(f"  - {field}: {extracted_fields[field]['selector']}")

print()

# Check for data-testid="Add" buttons
add_buttons = [k for k, v in extracted_fields.items() if v.get('data_testid') == 'Add']
print(f"'Add' buttons with data-testid: {len(add_buttons)}")
if add_buttons:
    print(f"  [VERIFIED] [data-testid=\"Add\"] pattern confirmed across sections")

print()
print("=" * 100)
print("RECOMMENDATIONS")
print("=" * 100)
print()
print("1. ADD to docs:")
print("   - data-testid values for all fields that have them")
print("   - Validation rules (required, readonly, disabled)")
print("   - relatedFields arrays")
print()
print("2. VERIFY in docs:")
print("   - All selectors are confirmed correct from recording")
print("   - Remove 'assumed' notes where selectors are now verified")
print()
print("3. ENHANCE docs with:")
print("   - Interaction counts (usage frequency)")
print("   - Recorded values (actual examples from usage)")
print("   - UUID stability warnings")
print()
