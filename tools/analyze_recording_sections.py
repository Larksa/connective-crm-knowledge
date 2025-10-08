"""Analyze which CRM sections are in a recording"""
import json
import sys
from pathlib import Path

if len(sys.argv) < 2:
    print("Usage: python analyze_recording_sections.py <recording.json>")
    sys.exit(1)

rec_path = Path(sys.argv[1])
with open(rec_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

events = data.get('events', [])
metadata = data.get('metadata', {})

print("=" * 80)
print(f"RECORDING: {rec_path.name}")
print("=" * 80)
print(f"Duration: {metadata.get('duration', 'N/A')}")
print(f"Events: {metadata.get('events_count', 'N/A')}")
print()

# Find navigation clicks (sections/tabs)
section_clicks = []
for i, event in enumerate(events):
    if event.get('type') != 'browser_click':
        continue

    text = event.get('text') or ''
    element_id = event.get('id') or ''
    button_text = event.get('button', {}).get('text', '') if isinstance(event.get('button'), dict) else ''

    # Look for section indicators
    indicators = {
        'Financials': 'financials' in element_id or 'Financials' in text,
        'Living Expenses': 'Living Expense' in text or 'Childcare' in text or 'Child & Spouse' in text,
        'Assets - Real Estate': 'Assets - Real Estate' in text or 'realEstateAssets' in element_id or 'Real Estate Asset' in text,
        'Assets - Other': 'Assets - Other' in text or 'otherAssets' in element_id or 'Other Assets' in text,
        'Liabilities': 'Liabilities' in text or 'liabilities' in element_id,
        'Other Income': 'Other Income' in text or 'incomes' in element_id,
        'Details': element_id == 'details',
        'Employment': element_id == 'employment',
        'Notes': 'addNoteToOpportunity' in element_id or 'Note Type' in text,
    }

    for section_name, matches in indicators.items():
        if matches:
            section_clicks.append((i, section_name, text[:50], element_id))

print("SECTIONS DETECTED:")
print()

sections_found = {}
for event_num, section, text, elem_id in section_clicks:
    if section not in sections_found:
        sections_found[section] = []
    sections_found[section].append((event_num, text, elem_id))

for section in sorted(sections_found.keys()):
    occurrences = sections_found[section]
    print(f"[{section}] - {len(occurrences)} interaction(s)")
    for event_num, text, elem_id in occurrences[:3]:
        print(f"  Event {event_num}: \"{text}\" (id={elem_id})")
    if len(occurrences) > 3:
        print(f"  ... and {len(occurrences) - 3} more")
    print()

# Count form fields
form_fields = []
for event in events:
    form_info = event.get('formFieldInfo')
    if form_info:
        field_name = form_info.get('name', '')
        field_type = form_info.get('type', '')
        if field_name and (field_name, field_type) not in form_fields:
            form_fields.append((field_name, field_type))

print(f"FORM FIELDS DETECTED: {len(form_fields)}")
for name, ftype in sorted(form_fields)[:15]:
    print(f"  {name:20} ({ftype})")
if len(form_fields) > 15:
    print(f"  ... and {len(form_fields) - 15} more")

print()
print("=" * 80)
print("RECOMMENDATION:")
print("=" * 80)

priority_sections = ['Living Expenses', 'Assets - Other', 'Liabilities']
has_priority = [s for s in priority_sections if s in sections_found]

if has_priority:
    print(f"This recording contains {len(has_priority)} priority section(s):")
    for s in has_priority:
        print(f"  - {s}")
    print()
    print("[RECOMMENDED] Extract fields from this recording!")
else:
    print("This recording doesn't contain priority sections (Living Expenses, Assets-Other, Liabilities)")
    print("[SKIP] for now - focus on recordings with priority sections")
