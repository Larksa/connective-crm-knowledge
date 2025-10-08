import json
from pathlib import Path
from collections import defaultdict

# Load the recording
recording_path = r'C:\Users\JamesLarkey\Downloads\WorkflowCapture-windows\recordings\connective-other-income-mcp\connective-other-income-mcp.json'
with open(recording_path, 'r') as f:
    data = json.load(f)

print("=" * 80)
print("EVENTS ANALYSIS")
print("=" * 80)
events = data.get('events', [])
print(f"Total events: {len(events)}\n")

# Group events by type
events_by_type = defaultdict(list)
for event in events:
    event_type = event.get('event_type', 'unknown')
    events_by_type[event_type].append(event)

print("\nEvent Types:")
for event_type, event_list in sorted(events_by_type.items()):
    print(f"  {event_type}: {len(event_list)}")

print("\n" + "=" * 80)
print("BROWSER INTERACTIONS")
print("=" * 80)
browser_events = [e for e in events if e.get('platform') == 'browser']
print(f"Total browser events: {len(browser_events)}\n")

# Extract selectors and interactions
selectors_found = {}
click_events = []
input_events = []

for event in browser_events:
    event_data = event.get('data', {})
    event_type = event.get('event_type', '')

    if event_type == 'browser_click':
        click_events.append(event)
        # Extract selector information
        selector = event_data.get('selector', '')
        tag_name = event_data.get('tag_name', '')
        text = event_data.get('text', '')
        element_id = event_data.get('element_id', '')
        element_name = event_data.get('element_name', '')
        classes = event_data.get('classes', '')

        if selector:
            if selector not in selectors_found:
                selectors_found[selector] = {
                    'type': 'click',
                    'tag': tag_name,
                    'text': text,
                    'id': element_id,
                    'name': element_name,
                    'classes': classes,
                    'count': 0
                }
            selectors_found[selector]['count'] += 1

    elif event_type == 'browser_input':
        input_events.append(event)
        selector = event_data.get('selector', '')
        tag_name = event_data.get('tag_name', '')
        value = event_data.get('value', '')
        element_id = event_data.get('element_id', '')
        element_name = event_data.get('element_name', '')

        if selector:
            if selector not in selectors_found:
                selectors_found[selector] = {
                    'type': 'input',
                    'tag': tag_name,
                    'values': [],
                    'id': element_id,
                    'name': element_name,
                    'count': 0
                }
            if 'values' not in selectors_found[selector]:
                selectors_found[selector]['values'] = []
            if value and value not in selectors_found[selector]['values']:
                selectors_found[selector]['values'].append(value)
            selectors_found[selector]['count'] += 1

print("\n" + "=" * 80)
print("DISCOVERED ELEMENTS")
print("=" * 80)

# Sort by priority: ID > name > classes
priority_selectors = []
for selector, info in selectors_found.items():
    if info.get('id'):
        priority = 1
        best_selector = f"#{info['id']}"
    elif info.get('name'):
        priority = 2
        best_selector = f"[name=\"{info['name']}\"]"
    elif selector.startswith('#') or selector.startswith('[data-testid'):
        priority = 1
        best_selector = selector
    else:
        priority = 3
        best_selector = selector

    priority_selectors.append((priority, best_selector, selector, info))

for priority, best_selector, orig_selector, info in sorted(priority_selectors):
    print(f"\n{best_selector}")
    print(f"  Original: {orig_selector}")
    print(f"  Type: {info['type']}")
    print(f"  Tag: {info['tag']}")
    if info.get('text'):
        print(f"  Text: {info['text'][:50]}")
    if info.get('values'):
        print(f"  Values: {info['values']}")
    if info.get('id'):
        print(f"  ID: {info['id']}")
    if info.get('name'):
        print(f"  Name: {info['name']}")
    if info.get('classes'):
        print(f"  Classes: {info['classes']}")
    print(f"  Interactions: {info['count']}")

print("\n" + "=" * 80)
print("WORKFLOW SEQUENCE")
print("=" * 80)
print("\nStep-by-step actions:\n")

step_num = 1
for event in browser_events:
    event_type = event.get('event_type', '')
    event_data = event.get('data', {})
    timestamp = event.get('timestamp', '')

    if event_type == 'browser_click':
        selector = event_data.get('selector', '')
        text = event_data.get('text', '')
        element_id = event_data.get('element_id', '')
        tag = event_data.get('tag_name', '')

        best_selector = selector
        if element_id:
            best_selector = f"#{element_id}"

        print(f"{step_num}. CLICK: {best_selector}")
        if text:
            print(f"   Text: \"{text[:50]}\"")
        if tag:
            print(f"   Tag: {tag}")
        step_num += 1

    elif event_type == 'browser_input':
        selector = event_data.get('selector', '')
        value = event_data.get('value', '')
        element_id = event_data.get('element_id', '')
        element_name = event_data.get('element_name', '')
        tag = event_data.get('tag_name', '')

        best_selector = selector
        if element_id:
            best_selector = f"#{element_id}"
        elif element_name:
            best_selector = f"[name=\"{element_name}\"]"

        print(f"{step_num}. INPUT: {best_selector}")
        print(f"   Value: \"{value}\"")
        if tag:
            print(f"   Tag: {tag}")
        step_num += 1

print("\n" + "=" * 80)
print("DROPDOWN OPTIONS DISCOVERED")
print("=" * 80)

# Find select elements and their options
select_elements = {}
for selector, info in selectors_found.items():
    if info.get('tag') == 'select' or (info.get('type') == 'input' and info.get('values')):
        select_elements[selector] = info

for selector, info in select_elements.items():
    best_selector = selector
    if info.get('id'):
        best_selector = f"#{info['id']}"

    print(f"\n{best_selector}")
    if info.get('values'):
        print(f"  Options discovered:")
        for value in info['values']:
            print(f"    - {value}")

print("\n" + "=" * 80)
print("METADATA SUMMARY")
print("=" * 80)
metadata = data.get('metadata', {})
print(f"Recording: {metadata.get('name')}")
print(f"Description: {metadata.get('description')}")
print(f"Duration: {metadata.get('duration')}")
print(f"Date: {metadata.get('date')} {metadata.get('time')}")
print(f"Complexity: {metadata.get('complexity_analysis', {}).get('complexity_level')}")
print(f"Forms Submitted: {data.get('workflow_summary', {}).get('forms_submitted')}")
