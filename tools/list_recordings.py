"""List all Connective CRM recordings and their metadata"""
import json
from pathlib import Path

recordings_dir = Path(r'C:\Users\JamesLarkey\Downloads\WorkflowCapture-windows\recordings')

# Find all connective-related recordings
connective_recordings = []
for json_file in recordings_dir.rglob('*.json'):
    if 'connective' in json_file.name.lower() or 'jl' in json_file.name.lower():
        connective_recordings.append(json_file)

print("=" * 80)
print("CONNECTIVE CRM RECORDINGS FOUND")
print("=" * 80)
print()

for rec_path in sorted(connective_recordings):
    try:
        with open(rec_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        metadata = data.get('metadata', {})

        print(f"File: {rec_path.name}")
        print(f"  Path: {rec_path.parent.name}/{rec_path.name}")
        print(f"  Name: {metadata.get('name', 'N/A')}")
        print(f"  Description: {metadata.get('description', 'N/A')}")
        print(f"  Date: {metadata.get('date', 'N/A')}")
        print(f"  Duration: {metadata.get('duration', 'N/A')}")
        print(f"  Events: {metadata.get('events_count', 'N/A')}")

        # Check if it has browser events
        events = data.get('events', [])
        browser_events = [e for e in events if e.get('type', '').startswith('browser_')]
        print(f"  Browser Events: {len(browser_events)}")

        # Try to detect section from events
        clicks = [e for e in events if e.get('type') == 'browser_click']
        texts = [e.get('text', '') for e in clicks[:10]]
        print(f"  First clicks: {', '.join([t[:20] for t in texts if t])[:60]}...")

        print()
    except Exception as e:
        print(f"File: {rec_path.name}")
        print(f"  ERROR: {e}")
        print()

print("=" * 80)
print(f"TOTAL CONNECTIVE RECORDINGS: {len(connective_recordings)}")
print("=" * 80)
