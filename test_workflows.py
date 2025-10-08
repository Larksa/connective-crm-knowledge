"""Test workflow querying"""
from sdk import CRMReference
import json

crm = CRMReference()

print("=" * 60)
print("WORKFLOW TEST")
print("=" * 60)
print()

# List all workflows
workflows = crm.list_workflows()
print(f"Total workflows available: {len(workflows)}")
print(f"Workflows: {', '.join(workflows)}")
print()

# Test each new workflow
new_workflows = ['add_liability', 'add_asset_other', 'add_living_expense', 'add_other_income']

for wf_name in new_workflows:
    print("=" * 60)
    print(f"Testing: {wf_name}")
    print("=" * 60)

    wf = crm.get_workflow(wf_name)
    if wf:
        print(f"Name: {wf.name}")
        print(f"Title: {wf.title}")
        print(f"Steps: {len(wf.steps)}")
        print(f"Validated: {wf.validated}")
        print()
        print("First 3 steps:")
        for step in wf.steps[:3]:
            print(f"  {step.number}. {step.description}")
            print(f"     Selector: {step.selector}")
            print(f"     Action: {step.action}")
        print()
    else:
        print(f"ERROR: Could not load workflow {wf_name}")
        print()

print("=" * 60)
print("Testing workflow JSON output")
print("=" * 60)
wf = crm.get_workflow('add_other_income')
print(json.dumps(wf.to_dict(), indent=2))
