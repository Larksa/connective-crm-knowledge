import json
from pathlib import Path

# Load the recording
recording_path = r'C:\Users\JamesLarkey\Downloads\WorkflowCapture-windows\recordings\connective-other-income-mcp\connective-other-income-mcp.json'
with open(recording_path, 'r') as f:
    data = json.load(f)

print("=" * 80)
print("METADATA")
print("=" * 80)
metadata = data.get('metadata', {})
for key, value in metadata.items():
    print(f"{key}: {value}")

print("\n" + "=" * 80)
print("WORKFLOW SUMMARY")
print("=" * 80)
workflow_summary = data.get('workflow_summary', {})
for key, value in workflow_summary.items():
    print(f"{key}: {value}")

print("\n" + "=" * 80)
print("AUTOMATION HINTS")
print("=" * 80)
automation_hints = data.get('automation_hints', {})
for key, value in automation_hints.items():
    if isinstance(value, list):
        print(f"\n{key}:")
        for item in value:
            print(f"  - {item}")
    else:
        print(f"{key}: {value}")

print("\n" + "=" * 80)
print("SESSION INTERACTIONS")
print("=" * 80)
session = data.get('session', {})
interactions = session.get('interactions', [])
print(f"Total interactions: {len(interactions)}")
for i, interaction in enumerate(interactions[:10]):  # First 10
    print(f"\n[{i+1}] {interaction.get('type', 'unknown')}")
    if 'selector' in interaction:
        print(f"  Selector: {interaction['selector']}")
    if 'value' in interaction:
        print(f"  Value: {interaction['value']}")
    if 'text' in interaction:
        print(f"  Text: {interaction['text']}")

print("\n" + "=" * 80)
print("UNIQUE SELECTORS DETECTED")
print("=" * 80)
selectors = set()
for interaction in interactions:
    if 'selector' in interaction:
        selectors.add(interaction['selector'])
for selector in sorted(selectors):
    print(f"  {selector}")

print("\n" + "=" * 80)
print("FORM FIELDS DETECTED")
print("=" * 80)
fields = {}
for interaction in interactions:
    if interaction.get('type') in ['input', 'select', 'click']:
        selector = interaction.get('selector', '')
        field_type = interaction.get('type', '')
        value = interaction.get('value') or interaction.get('text', '')
        if selector not in fields:
            fields[selector] = {
                'type': field_type,
                'values': []
            }
        if value and value not in fields[selector]['values']:
            fields[selector]['values'].append(value)

for selector, info in sorted(fields.items()):
    print(f"\n{selector}")
    print(f"  Type: {info['type']}")
    if info['values']:
        print(f"  Values: {', '.join(map(str, info['values'][:5]))}")

print("\n" + "=" * 80)
print("TAB SWITCHES")
print("=" * 80)
tab_switches = workflow_summary.get('tab_switches', [])
for tab in tab_switches:
    print(f"  {tab}")
