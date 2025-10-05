# How to Add Workflows to Connective CRM SDK

This guide explains how to add new workflows to the CRM SDK so they can be used in automation.

## Table of Contents

1. [What Are Workflows?](#what-are-workflows)
2. [Three Methods to Add Workflows](#three-methods-to-add-workflows)
3. [Method 1: Add to Markdown (Recommended)](#method-1-add-to-markdown-recommended)
4. [Method 2: Create in Python](#method-2-create-in-python)
5. [Method 3: Convert from Recordings](#method-3-convert-from-recordings)
6. [Complete Workflow Examples](#complete-workflow-examples)
7. [Using Workflows in Automation](#using-workflows-in-automation)
8. [Testing Your Workflows](#testing-your-workflows)
9. [Best Practices](#best-practices)
10. [Troubleshooting](#troubleshooting)

---

## What Are Workflows?

Workflows are **validated, step-by-step instructions** for common tasks in the Connective CRM. They include:

- Exact selectors for each step
- Action types (click, fill, select)
- Wait times between steps
- Notes about modals, frameworks, or special behavior

**Benefits**:
- ✅ Reusable across multiple automations
- ✅ Self-documenting (clear steps)
- ✅ Validated (tested and confirmed working)
- ✅ Version controlled (in markdown or code)
- ✅ Easy to share with team

---

## Three Methods to Add Workflows

| Method | Best For | Difficulty | Reusability |
|--------|----------|------------|-------------|
| **1. Add to Markdown** | General use, team sharing | Easy | High |
| **2. Create in Python** | Dynamic/conditional workflows | Medium | Medium |
| **3. Convert from Recording** | Complex multi-step processes | Easy | High |

---

## Method 1: Add to Markdown (Recommended)

The SDK automatically parses workflows from `memory/raw/COMPLETE_CONNECTIVE_CRM_REFERENCE.md`.

### Template

Copy this template and fill in your workflow details:

```markdown
### Workflow N: [Workflow Title]

**Status**: Validated
**Triggers Modal**: [Yes/No]
**Framework**: [Standard form / Froala editor / AG-Grid / etc.]

**Steps**:

1. **[Step Description]**
   - Selector: `[CSS selector]`
   - Action: [Click / Fill / Select / etc.]
   - Wait: [Time in seconds or description]
   - Notes: [Optional notes about this step]

2. **[Next Step Description]**
   - Selector: `[CSS selector]`
   - Action: [Action type]
   - Wait: [Wait time]

[... more steps ...]

**Complete Example**:
```python
# Step 1: [Description]
driver.find_element(By.ID, "selector").click()
time.sleep(2)

# Step 2: [Description]
driver.find_element(By.ID, "field").send_keys("value")

# [... more code ...]
```
```

### Example: Add New Applicant

```markdown
### Workflow 4: Add New Applicant

**Status**: Validated
**Triggers Modal**: Yes
**Framework**: Standard form

**Steps**:

1. **Navigate to Details Tab**
   - Selector: `#details`
   - Action: Click
   - Wait: 2 seconds for tab to load

2. **Click Add Applicant Button**
   - Selector: `[data-testid="Add Applicant"]`
   - Action: Click
   - Wait: 1 second for modal to appear

3. **Fill First Name**
   - Selector: `#firstName`
   - Action: Fill
   - Notes: Required field

4. **Fill Last Name**
   - Selector: `#lastName`
   - Action: Fill
   - Notes: Required field

5. **Fill Email**
   - Selector: `#email`
   - Action: Fill
   - Notes: Must be valid email format

6. **Fill Mobile**
   - Selector: `#mobile`
   - Action: Fill
   - Notes: Australian format (04XX XXX XXX)

7. **Click Save**
   - Selector: `[data-testid="Save"]`
   - Action: Click
   - Wait: 2 seconds for save confirmation

**Complete Example**:
```python
# Step 1: Navigate to Details
driver.find_element(By.ID, "details").click()
time.sleep(2)

# Step 2: Click Add Applicant
driver.find_element(By.CSS_SELECTOR, "[data-testid='Add Applicant']").click()
time.sleep(1)

# Step 3-6: Fill applicant details
driver.find_element(By.ID, "firstName").send_keys("John")
driver.find_element(By.ID, "lastName").send_keys("Smith")
driver.find_element(By.ID, "email").send_keys("john.smith@email.com")
driver.find_element(By.ID, "mobile").send_keys("0412345678")

# Step 7: Save
driver.find_element(By.CSS_SELECTOR, "[data-testid='Save']").click()
time.sleep(2)
```
```

### After Adding to Markdown

1. Save the file
2. Reload the SDK:
   ```python
   from sdk import CRMReference
   crm = CRMReference()  # Re-parses markdown
   ```
3. Use it:
   ```python
   workflow = crm.get_workflow("add_new_applicant")
   print(f"Steps: {len(workflow.steps)}")
   ```

---

## Method 2: Create in Python

For dynamic or conditional workflows that need to be generated at runtime.

### Template

```python
from sdk import Workflow, WorkflowStep

# Create steps
steps = [
    WorkflowStep(
        number=1,
        action="click",
        selector="#selector1",
        description="Step description",
        wait_time=2000  # milliseconds
    ),
    WorkflowStep(
        number=2,
        action="fill",
        selector="#field1",
        description="Fill field",
        value="Default value"
    ),
    # ... more steps
]

# Create workflow
workflow = Workflow(
    name="workflow_name",  # Lowercase, underscores
    title="Workflow Title",  # Human-readable
    steps=steps,
    validated=True,
    triggers_modal=False
)

# Add to CRM reference
crm.workflows["workflow_name"] = workflow
```

### Example: Update Financial Information

```python
from sdk import Workflow, WorkflowStep

def create_update_financials_workflow():
    """Create workflow for updating financial information"""

    steps = [
        WorkflowStep(
            number=1,
            action="click",
            selector="#financials",
            description="Navigate to Financials tab",
            wait_time=2000
        ),
        WorkflowStep(
            number=2,
            action="click",
            selector="#realEstateAssets",
            description="Click Real Estate Assets",
            wait_time=1000
        ),
        WorkflowStep(
            number=3,
            action="click",
            selector='[data-testid="Add"]',
            description="Click Add Property button",
            wait_time=1000,
            notes="Opens property form"
        ),
        WorkflowStep(
            number=4,
            action="select",
            selector="#propertyType",
            description="Select property type",
            value="Fully Detached House"
        ),
        WorkflowStep(
            number=5,
            action="select",
            selector="#propertyStatus",
            description="Select property status",
            value="Established"
        ),
        WorkflowStep(
            number=6,
            action="select",
            selector="#realEstatePurpose",
            description="Select property purpose",
            value="Owner Occupied"
        ),
        WorkflowStep(
            number=7,
            action="fill",
            selector="#value",
            description="Enter property value",
            value="850000"
        ),
        WorkflowStep(
            number=8,
            action="click",
            selector='[data-testid="Save"]',
            description="Save property",
            wait_time=2000,
            notes="Wait for save confirmation"
        )
    ]

    return Workflow(
        name="update_financials_add_property",
        title="Update Financials - Add Property",
        steps=steps,
        validated=True,
        triggers_modal=True
    )

# Use it
crm = CRMReference()
workflow = create_update_financials_workflow()
crm.workflows["update_financials_add_property"] = workflow

# Now available
my_workflow = crm.get_workflow("update_financials_add_property")
```

---

## Method 3: Convert from Recordings

If you have JSON recordings from your automation capture tool, convert them to workflows.

### Conversion Function

```python
import json
from sdk import Workflow, WorkflowStep

def convert_recording_to_workflow(
    recording_path: str,
    workflow_name: str,
    workflow_title: str
) -> Workflow:
    """
    Convert a JSON recording to a Workflow object

    Args:
        recording_path: Path to recording JSON file
        workflow_name: Identifier (lowercase_with_underscores)
        workflow_title: Human-readable title

    Returns:
        Workflow object
    """
    with open(recording_path) as f:
        recording = json.load(f)

    steps = []

    for i, action in enumerate(recording.get('actions', []), 1):
        step = WorkflowStep(
            number=i,
            action=action.get('type', 'click'),
            selector=action.get('selector', ''),
            description=action.get('description', f"Step {i}"),
            value=action.get('value'),
            wait_time=action.get('wait', 0),
            notes=action.get('notes', '')
        )
        steps.append(step)

    return Workflow(
        name=workflow_name,
        title=workflow_title,
        steps=steps,
        validated=True,
        triggers_modal=recording.get('triggers_modal', False)
    )

# Usage
workflow = convert_recording_to_workflow(
    'recordings/add_liability.json',
    'add_liability',
    'Add Liability to Financials'
)

crm = CRMReference()
crm.workflows['add_liability'] = workflow
```

### Example Recording Format

Your recording JSON should look like:

```json
{
  "name": "add_liability",
  "triggers_modal": false,
  "actions": [
    {
      "type": "click",
      "selector": "#financials",
      "description": "Navigate to Financials",
      "wait": 2000
    },
    {
      "type": "click",
      "selector": "#liabilities",
      "description": "Click Liabilities tab",
      "wait": 1000
    },
    {
      "type": "click",
      "selector": "[data-testid='Add']",
      "description": "Click Add Liability",
      "wait": 1000
    },
    {
      "type": "select",
      "selector": "#name",
      "value": "Mortgage Loan",
      "description": "Select liability type"
    },
    {
      "type": "fill",
      "selector": "#limit",
      "value": "500000",
      "description": "Enter loan amount"
    },
    {
      "type": "click",
      "selector": "[data-testid='Save']",
      "description": "Save liability",
      "wait": 2000
    }
  ]
}
```

---

## Complete Workflow Examples

### Example 1: Add Liability

```markdown
### Workflow 5: Add Liability

**Status**: Validated
**Triggers Modal**: No
**Framework**: Standard form

**Steps**:

1. **Navigate to Financials**
   - Selector: `#financials`
   - Action: Click
   - Wait: 2 seconds

2. **Click Liabilities Tab**
   - Selector: `#liabilities`
   - Action: Click
   - Wait: 1 second

3. **Click Add Button**
   - Selector: `[data-testid="Add"]`
   - Action: Click
   - Wait: 1 second for form to appear

4. **Select Liability Type**
   - Selector: `#name`
   - Action: Select
   - Notes: 19 options available (see dropdown reference)

5. **Select Priority**
   - Selector: `#priority`
   - Action: Select
   - Notes: First, Second, Third, Fourth

6. **Enter Limit/Balance**
   - Selector: `#limit`
   - Action: Fill
   - Notes: Numeric value

7. **Enter Repayment Amount**
   - Selector: `#accountRepayment`
   - Action: Fill
   - Notes: Optional field

8. **Select Repayment Frequency**
   - Selector: `#accountRepaymentFrequency`
   - Action: Select
   - Notes: Annual, Monthly, Fortnightly, Weekly

9. **Check if Clearing from Loan**
   - Selector: `[name="accountClearingFromLoan"]`
   - Action: Check
   - Notes: Optional checkbox

10. **Click Save**
    - Selector: `[data-testid="Save"]`
    - Action: Click
    - Wait: 2 seconds
```

### Example 2: Update Income Details

```markdown
### Workflow 6: Update Income Details

**Status**: Validated
**Triggers Modal**: No
**Framework**: Standard form

**Steps**:

1. **Navigate to Details Tab**
   - Selector: `#details`
   - Action: Click
   - Wait: 2 seconds

2. **Click Incomes Tab**
   - Selector: `#incomes`
   - Action: Click
   - Wait: 1 second

3. **Click Add Income**
   - Selector: `[data-testid="Add"]`
   - Action: Click
   - Wait: 1 second

4. **Select Income Type**
   - Selector: `#type`
   - Action: Select
   - Notes: Dividends, Family Allowance, Maintenance, Other

5. **Enter Amount**
   - Selector: `#amount`
   - Action: Fill
   - Notes: Numeric value

6. **Select Frequency**
   - Selector: `#frequency`
   - Action: Select
   - Notes: Annual, Monthly, Fortnightly, Weekly

7. **Click Save**
   - Selector: `[data-testid="Save"]`
   - Action: Click
   - Wait: 2 seconds
```

---

## Using Workflows in Automation

### Basic Usage

```python
from sdk import CRMReference

crm = CRMReference()

# Get workflow
workflow = crm.get_workflow("add_new_applicant")

# Execute each step
for step in workflow.steps:
    print(f"Step {step.number}: {step.description}")

    if step.action == "click":
        await page.click(step.selector)
    elif step.action == "fill":
        await page.fill(step.selector, data[step.description])
    elif step.action == "select":
        await page.select_option(step.selector, data[step.description])

    # Wait if specified
    if step.wait_time:
        await asyncio.sleep(step.wait_time / 1000)
```

### Workflow Executor Class

Create a reusable executor:

```python
import asyncio
from typing import Dict, Optional

class WorkflowExecutor:
    """Execute workflows with data substitution"""

    def __init__(self, page, crm_reference):
        self.page = page
        self.crm = crm_reference
        self.logger = logging.getLogger(__name__)

    async def execute(
        self,
        workflow_name: str,
        data: Optional[Dict] = None,
        dry_run: bool = False
    ):
        """
        Execute a workflow

        Args:
            workflow_name: Name of workflow to execute
            data: Dictionary mapping step descriptions to values
            dry_run: If True, just print steps without executing
        """
        workflow = self.crm.get_workflow(workflow_name)

        if not workflow:
            raise ValueError(f"Workflow '{workflow_name}' not found")

        self.logger.info(f"Executing: {workflow.title}")

        for step in workflow.steps:
            self.logger.info(f"  Step {step.number}: {step.description}")

            if dry_run:
                print(f"    [DRY RUN] {step.action} {step.selector}")
                continue

            # Execute action
            try:
                if step.action == "click":
                    await self.page.click(step.selector)

                elif step.action == "fill":
                    # Use data if provided, otherwise use step.value
                    value = data.get(step.description) if data else step.value
                    if value:
                        await self.page.fill(step.selector, str(value))

                elif step.action == "select":
                    value = data.get(step.description) if data else step.value
                    if value:
                        await self.page.select_option(step.selector, value)

                elif step.action == "check":
                    await self.page.check(step.selector)

                elif step.action == "uncheck":
                    await self.page.uncheck(step.selector)

                # Wait if specified
                if step.wait_time:
                    await asyncio.sleep(step.wait_time / 1000)

            except Exception as e:
                self.logger.error(
                    f"Failed at step {step.number}: {step.description}"
                )
                self.logger.error(f"Error: {e}")
                raise

        self.logger.info(f"✓ Completed: {workflow.title}")

# Usage
executor = WorkflowExecutor(page, crm)

# Execute with data
await executor.execute("add_new_applicant", {
    "Fill First Name": "John",
    "Fill Last Name": "Smith",
    "Fill Email": "john@email.com",
    "Fill Mobile": "0412345678"
})

# Dry run to test
await executor.execute("add_liability", dry_run=True)
```

---

## Testing Your Workflows

### 1. Test Parsing

```python
from sdk import CRMReference

crm = CRMReference()

# Check if workflow was parsed
workflow = crm.get_workflow("your_workflow_name")

if workflow:
    print(f"✓ Workflow parsed successfully")
    print(f"  Title: {workflow.title}")
    print(f"  Steps: {len(workflow.steps)}")
    for step in workflow.steps:
        print(f"    {step.number}. {step.description} ({step.action})")
else:
    print(f"✗ Workflow not found")
```

### 2. Validate Steps

```python
def validate_workflow(workflow):
    """Check workflow for common issues"""

    issues = []

    # Check step numbering
    for i, step in enumerate(workflow.steps, 1):
        if step.number != i:
            issues.append(f"Step {i} has wrong number: {step.number}")

    # Check required fields
    for step in workflow.steps:
        if not step.selector:
            issues.append(f"Step {step.number} missing selector")
        if not step.description:
            issues.append(f"Step {step.number} missing description")
        if not step.action:
            issues.append(f"Step {step.number} missing action")

    # Check action values
    valid_actions = ["click", "fill", "select", "check", "uncheck"]
    for step in workflow.steps:
        if step.action not in valid_actions:
            issues.append(
                f"Step {step.number} has invalid action: {step.action}"
            )

    # Report
    if issues:
        print("⚠️  Issues found:")
        for issue in issues:
            print(f"  - {issue}")
    else:
        print("✓ Workflow validation passed")

    return len(issues) == 0

# Use it
workflow = crm.get_workflow("add_new_applicant")
validate_workflow(workflow)
```

### 3. Test Execution (Dry Run)

```python
# Dry run - prints steps without executing
executor = WorkflowExecutor(page, crm)
await executor.execute("add_new_applicant", dry_run=True)

# Output:
#   Step 1: Navigate to Details Tab
#     [DRY RUN] click #details
#   Step 2: Click Add Applicant Button
#     [DRY RUN] click [data-testid="Add Applicant"]
#   ...
```

---

## Best Practices

### 1. Naming Conventions

```python
# Good workflow names
"add_new_applicant"
"update_financials_add_property"
"add_liability_mortgage"
"upload_payslip_document"

# Bad workflow names
"AddNewApplicant"  # Don't use camelCase
"add applicant"     # Don't use spaces
"new-app"          # Don't use abbreviations
"workflow1"        # Don't use generic names
```

### 2. Step Descriptions

```python
# Good descriptions
"Navigate to Financials tab"
"Click Add Liability button"
"Select liability type from dropdown"
"Enter loan amount in currency format"

# Bad descriptions
"Click button"      # Too vague
"Step 1"           # Not descriptive
"Do the thing"     # Unclear
"Next"             # Meaningless
```

### 3. Selector Priority

Use selectors in this order of preference:

1. **data-testid** - Most reliable
   ```python
   selector='[data-testid="Add Applicant"]'
   ```

2. **#id** - Reliable if not dynamic
   ```python
   selector='#firstName'
   ```

3. **Text content** - For consistent labels
   ```python
   selector='button:has-text("Save")'
   ```

4. **Class** - Less reliable, use as fallback
   ```python
   selector='.submit-button'
   ```

### 4. Wait Times

```python
# After navigation
wait_time=2000  # 2 seconds for page load

# After click (modal)
wait_time=1000  # 1 second for modal to appear

# After form submission
wait_time=2000  # 2 seconds for save confirmation

# No wait needed
wait_time=0  # For fills and selects
```

### 5. Error Handling

Add notes about potential issues:

```python
WorkflowStep(
    number=5,
    action="fill",
    selector="#email",
    description="Fill email address",
    notes="Validates email format - must include @"
)
```

---

## Troubleshooting

### Workflow Not Found

**Problem**: `crm.get_workflow("my_workflow")` returns `None`

**Solutions**:
1. Check workflow name matches markdown heading:
   ```markdown
   ### Workflow 4: My Workflow Name
   # Should be accessed as: "my_workflow_name"
   ```

2. Reload SDK after adding workflow:
   ```python
   crm = CRMReference()  # Re-parses markdown
   ```

3. List all workflows:
   ```python
   print(crm.list_workflows())
   ```

### Step Parsing Issues

**Problem**: Steps not parsing correctly from markdown

**Solutions**:
1. Check markdown format exactly matches template
2. Ensure steps are numbered sequentially (1, 2, 3...)
3. Each step must have selector and action
4. Code block must use triple backticks

### Execution Failures

**Problem**: Workflow fails during execution

**Solutions**:
1. Run dry run first:
   ```python
   await executor.execute("workflow_name", dry_run=True)
   ```

2. Check selectors are current:
   ```python
   # Verify element exists
   element = await page.query_selector(step.selector)
   if not element:
       print(f"Selector not found: {step.selector}")
   ```

3. Add wait times between steps:
   ```python
   # Increase wait_time if page is slow to respond
   wait_time=3000  # 3 seconds
   ```

4. Check for modals/overlays blocking clicks:
   ```python
   # Wait for modal to appear
   await page.wait_for_selector('.modal', state='visible')
   ```

---

## Quick Reference

### Workflow Template (Markdown)

```markdown
### Workflow N: [Title]

**Status**: Validated
**Triggers Modal**: [Yes/No]

**Steps**:

1. **[Description]**
   - Selector: `[selector]`
   - Action: [action]
   - Wait: [time]
```

### Workflow Template (Python)

```python
from sdk import Workflow, WorkflowStep

workflow = Workflow(
    name="workflow_name",
    title="Workflow Title",
    steps=[
        WorkflowStep(
            number=1,
            action="click",
            selector="#selector",
            description="Description"
        )
    ],
    validated=True
)
```

### Execute Workflow

```python
workflow = crm.get_workflow("workflow_name")
for step in workflow.steps:
    # Execute based on step.action
    pass
```

---

## Summary

You can add workflows three ways:

1. **Markdown** (easiest) - Add to COMPLETE_CONNECTIVE_CRM_REFERENCE.md
2. **Python** (flexible) - Create Workflow objects in code
3. **Recording** (fastest) - Convert JSON recordings to workflows

All workflows are instantly available via:
```python
workflow = crm.get_workflow("workflow_name")
```

Use the `WorkflowExecutor` class for easy execution with data substitution.

**Next**: Start adding your own workflows for common tasks!
