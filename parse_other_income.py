import json
from collections import defaultdict

# Load recording
recording_path = r'C:\Users\JamesLarkey\Downloads\WorkflowCapture-windows\recordings\connective-other-income-mcp\connective-other-income-mcp.json'
with open(recording_path, 'r') as f:
    data = json.load(f)

events = data.get('events', [])

print("=" * 100)
print("OTHER INCOME WORKFLOW ANALYSIS")
print("=" * 100)

# Track unique elements
elements = {}
workflow_steps = []
dropdown_options = defaultdict(set)

for idx, event in enumerate(events):
    event_type = event.get('type', '')

    if event_type not in ['browser_click', 'browser_input']:
        continue

    # Extract key information
    selector = event.get('selector', '')
    element_id = event.get('id', '')
    tag_name = event.get('tagName', '')
    text = event.get('text', '')
    value = event.get('value')
    data_testid = event.get('dataTestId')
    form_field_info = event.get('formFieldInfo', {})

    # Determine best selector
    if data_testid:
        best_selector = f'[data-testid="{data_testid}"]'
    elif element_id and not element_id.startswith('btn_'):  # Skip dynamic UUID buttons
        best_selector = f'#{element_id}'
    else:
        best_selector = selector

    # Track element
    element_key = element_id or selector
    if element_key not in elements:
        elements[element_key] = {
            'id': element_id,
            'selector': best_selector,
            'tag': tag_name,
            'type': form_field_info.get('type', tag_name) if form_field_info else tag_name,
            'name': form_field_info.get('name', '') if form_field_info else '',
            'label': form_field_info.get('label', '') if form_field_info else '',
            'data_testid': data_testid,
            'interactions': []
        }

        # Extract dropdown options
        if form_field_info and form_field_info.get('dropdown'):
            dropdown = form_field_info['dropdown']
            options = dropdown.get('options', [])
            for opt in options:
                opt_text = opt.get('text', '')
                opt_value = opt.get('value', '')
                if opt_value and not opt.get('disabled', False):
                    dropdown_options[element_key].add(opt_text)

    # Track interaction
    interaction_info = {
        'event_type': event_type,
        'value': value,
        'text': text[:50] if text else None
    }
    elements[element_key]['interactions'].append(interaction_info)

    # Build workflow sequence
    workflow_step = {
        'step': len(workflow_steps) + 1,
        'action': event_type,
        'selector': best_selector,
        'id': element_id,
        'tag': tag_name,
        'text': text[:50] if text else '',
        'value': value
    }
    workflow_steps.append(workflow_step)

print("\n" + "=" * 100)
print("DISCOVERED ELEMENTS")
print("=" * 100)

for elem_key, elem_info in sorted(elements.items(), key=lambda x: x[1].get('id') or ''):
    print(f"\nElement ID: {elem_info['id']}")
    print(f"  Best Selector: {elem_info['selector']}")
    print(f"  Tag: {elem_info['tag']}")
    print(f"  Type: {elem_info['type']}")
    if elem_info.get('name'):
        print(f"  Name: {elem_info['name']}")
    if elem_info.get('data_testid'):
        print(f"  data-testid: {elem_info['data_testid']}")
    if elem_key in dropdown_options:
        print(f"  Dropdown Options ({len(dropdown_options[elem_key])}):")
        for option in sorted(dropdown_options[elem_key]):
            if option and option != '<Clear undefined>':
                print(f"    - {option}")
    print(f"  Interactions: {len(elem_info['interactions'])}")

print("\n" + "=" * 100)
print("WORKFLOW SEQUENCE (STEP-BY-STEP)")
print("=" * 100)

current_form = None
for step in workflow_steps:
    # Detect form boundaries
    if step['tag'] == 'button' and 'Add' in step['text']:
        current_form = f"Form {step['step']}"
        print(f"\n--- {current_form} START ---")

    print(f"\n{step['step']}. {step['action'].upper()}: {step['selector']}")
    if step['text']:
        print(f"   Text: \"{step['text']}\"")
    if step['value']:
        print(f"   Value: \"{step['value']}\"")
    if step['tag']:
        print(f"   Tag: {step['tag']}")

print("\n" + "=" * 100)
print("MARKDOWN FORMAT FOR KNOWLEDGE BASE")
print("=" * 100)

# Generate markdown in the project's format
print("\n#### Other Income Navigation")
print("**Selector**: `#incomes` (tab)")
print("**Section**: Financials")
print()

print("\n#### Other Income Elements")
print()

# Group elements by function
nav_elements = []
form_elements = []
action_elements = []

for elem_key, elem_info in elements.items():
    if elem_info['tag'] == 'button':
        if 'Add' in str(elem_info.get('text', '')):
            action_elements.append(elem_info)
        else:
            nav_elements.append(elem_info)
    elif elem_info['tag'] in ['select', 'input']:
        form_elements.append(elem_info)

# Print form fields
for elem in sorted(form_elements, key=lambda x: x.get('id', '')):
    field_name = elem['name'] or elem['id']
    field_type = 'select' if elem['tag'] == 'select' else 'input'

    print(f"#### Element: {field_name.replace('_', ' ').title()}")
    print(f"- **Field Name:** {field_name}")
    print(f"- **Selector:** `{elem['selector']}`")
    if elem.get('id'):
        print(f"- **ID:** `{elem['id']}`")
    print(f"- **Type:** {field_type}")
    if elem.get('data_testid'):
        print(f"- **data-testid:** `{elem['data_testid']}`")
    print(f"- **Section:** financials_income")

    # Add options if dropdown
    elem_key = elem['id'] or elem['selector']
    if elem_key in dropdown_options and dropdown_options[elem_key]:
        print(f"- **Options:**")
        for option in sorted(dropdown_options[elem_key]):
            if option and option != '<Clear undefined>':
                print(f"  - {option}")

    print()

print("\n" + "=" * 100)
print("WORKFLOW DOCUMENTATION")
print("=" * 100)
print("""
### Workflow: Add Other Income

**Section**: Financials > Incomes
**Forms Submitted**: 4 (from recording metadata)

**Steps**:

1. **Navigate to Financials Tab**
   - Selector: `#financials`
   - Action: Click

2. **Navigate to Incomes Sub-Tab**
   - Selector: `#incomes`
   - Action: Click
   - Wait: 1-2 seconds for tab to load

3. **Click Add Income Button**
   - Selector: `[data-testid="Add"]`
   - Action: Click
   - Note: Opens income form inline

4. **Select Income Type**
   - Selector: `#type`
   - Action: Select from dropdown
   - Options: Dividends, Family Allowance, Maintenance, Other

5. **Select Frequency**
   - Selector: `#frequency`
   - Action: Select from dropdown
   - Options: Annual, Monthly, Fortnightly, Weekly

6. **Enter Amount**
   - Selector: `#amount`
   - Action: Input (currency)
   - Format: Numeric value (e.g., 50000)

7. **Save Income Entry**
   - Action: Form auto-saves or submit button
   - Wait: 1-2 seconds

8. **Repeat Steps 3-7** for each additional income source

**Example Code**:
```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Navigate to Financials > Incomes
driver.find_element(By.ID, "financials").click()
time.sleep(1)
driver.find_element(By.ID, "incomes").click()
time.sleep(2)

# Add income
driver.find_element(By.CSS_SELECTOR, "[data-testid='Add']").click()
time.sleep(1)

# Fill form
Select(driver.find_element(By.ID, "type")).select_by_visible_text("Dividends")
Select(driver.find_element(By.ID, "frequency")).select_by_visible_text("Annual")
driver.find_element(By.ID, "amount").send_keys("15000")

# Wait for save
time.sleep(2)
```
""")

print("\n" + "=" * 100)
print("SUMMARY STATISTICS")
print("=" * 100)
print(f"Total Events: {len(events)}")
print(f"Browser Interactions: {len([e for e in events if e.get('type', '').startswith('browser_')])}")
print(f"Unique Elements: {len(elements)}")
print(f"Dropdown Fields: {len(dropdown_options)}")
print(f"Workflow Steps: {len(workflow_steps)}")
print(f"Forms Submitted: {data.get('workflow_summary', {}).get('forms_submitted', 0)}")
print(f"Duration: {data.get('metadata', {}).get('duration', 'Unknown')}")
