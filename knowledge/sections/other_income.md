# Other Income - Detailed Automation Guide

> **Parent Reference**: [COMPLETE_CONNECTIVE_CRM_REFERENCE.md](../COMPLETE_CONNECTIVE_CRM_REFERENCE.md)
> **CRM Tab**: Financials → Other Income
> **Integration Status**: ✅ Patterns documented for automation
> **Last Updated**: 2025-10-06

---

**🔗 Navigation**
- ⬆️ [Master Reference](../COMPLETE_CONNECTIVE_CRM_REFERENCE.md)
- 📙 [Living Expenses Guide](./living_expenses.md)
- 📘 [Liabilities Guide](./liabilities.md)
- 📗 [Assets - Other Guide](./assets_other.md)

---

## 📋 Table of Contents

1. [Overview](#overview)
2. [Navigation Path](#navigation-path)
3. [Complete Income Type List](#complete-income-type-list-4-types)
4. [Form Fields Reference](#form-fields-reference)
5. [Workflow Patterns](#workflow-patterns)
6. [Timing and Wait Strategies](#timing-and-wait-strategies)
7. [Complete Selector Reference](#complete-selector-reference)
8. [Error Handling and Edge Cases](#error-handling-and-edge-cases)
9. [Testing Checklist](#testing-checklist)
10. [Quick Start Guide](#quick-start-guide-for-ai-agent)
11. [Summary Statistics](#summary-statistics)

---

## Overview

### Purpose
The Other Income section in Connective Financial CRM captures non-employment income sources such as dividends, family allowances, maintenance payments, and other miscellaneous income for loan applications.

### User Workflow (From Voice Annotation)

**Voice Annotation (8.3s)**:
> _"this is recording the connective other income in the financial section"_

**Context**: User clarifies this is the "Other Income" section in Financials, not employment income (despite the original filename "connectiveemployment").

### Form Structure
- **Simple 3-field form** (income type, frequency, amount)
- **4 income type options** (Dividends, Family Allowance, Maintenance, Other)
- **4 frequency options** (Annual, Monthly, Fortnightly, Weekly)
- **Auto-save mechanism** (no explicit submit button)
- **Repeatable entries** for multiple income sources

### ⚠️ Critical Requirements
- **Page Load Timeout**: 40 seconds max observed (39,644ms)
- **Average Action Time**: 1.18 seconds
- **Total Wait Time**: ~40 seconds for complete workflow
- **Complexity Score**: 5/10 (simple but requires precise timing)

---

## Navigation Path

### To Access Financials Section
```
1. Click: #financials > span.TabButton-module_tab-button-elem__AV3Ub:nth-of-type(2)
   Text: "Financials"

2. Section appears with financial subsections
```

### Other Income Button
```css
Selector: #incomes > span
Text: "Other Income"
XPath: /html[1]/body[1]/div[1]/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/button[6]/span[1]
Element Rect: Left: 836.359375, Width: 83.703125, Height: 18
```

### Add Income Button
```css
Selector: #btn_d53c37a8-0cf4-4604-bbfb-6b19670998ec
XPath: //*[@id="btn_d53c37a8-0cf4-4604-bbfb-6b19670998ec"]
Tag: button
Text: "Income"
Classes: btn btn-light btn-sm
Element Rect: Left: 244, Width: 68.890625, Height: 25.953125
```

---

## Complete Income Type List (4 Types)

All income types available in the primary dropdown:

| # | Income Type | Description | Common Use Case |
|---|-------------|-------------|-----------------|
| 1 | **Dividends** | Investment dividend income | Share dividends, trust distributions, investment income |
| 2 | **Family Allowance** | Government family benefits | Family Tax Benefit A/B, Child Care Subsidy, Parenting Payment |
| 3 | **Maintenance** | Child/spousal support payments | Court-ordered maintenance, child support, voluntary support |
| 4 | **Other** | Miscellaneous income sources | Rental income, pensions, allowances, government benefits |

**Dropdown Text Observed**: `"Select Type...DividendsFamily AllowanceMaintenanceOther"`

### Income Type Use Cases

#### 1. Dividends
**Use When**: Receiving dividend income from shares or investments
**Common Sources**:
- Share dividends (ASX, international stocks)
- Trust distributions
- Investment income
- Managed fund distributions

#### 2. Family Allowance
**Use When**: Receiving government family benefits
**Common Sources**:
- Family Tax Benefit Part A
- Family Tax Benefit Part B
- Child Care Subsidy
- Parenting Payment (single/partnered)

#### 3. Maintenance
**Use When**: Receiving child or spousal support
**Common Sources**:
- Court-ordered child support
- Private child support agreements
- Spousal maintenance
- De facto maintenance

#### 4. Other
**Use When**: Any income not covered by specific categories
**Common Sources**:
- Rental income
- Pension payments
- Government allowances
- Disability support payments
- Centrelink benefits

---

## Form Fields Reference

### 1. Income Type Dropdown (Primary Selection)

**Field Properties**:
- **ID**: `type`
- **CSS Selector**: `#type`
- **XPath**: `//*[@id="type"]`
- **Tag**: `select`
- **Classes**: `undefined form-item__element--select text-placeholder form-control`
- **Input Type**: `select-one`
- **Element Rect**: Left: 241.1875, Width: 259.40625, Height: 32

**Dropdown Text Observed**: `"Select Type...DividendsFamily AllowanceMaintenanceOther"`

**Available Options** (4):
```xml
<option value="">Select Type...</option>
<option value="Dividends">Dividends</option>
<option value="Family Allowance">Family Allowance</option>
<option value="Maintenance">Maintenance</option>
<option value="Other">Other</option>
```

**Selection Example**:
```python
# Select by value
select_option("#type", value="Dividends")

# Or by visible text
select_option("#type", text="Family Allowance")
```

---

### 2. Frequency Dropdown

**Field Properties**:
- **ID**: `frequency`
- **CSS Selector**: `#frequency`
- **XPath**: `//*[@id="frequency"]`
- **Tag**: `select`
- **Classes**: `undefined form-item__element--select text-placeholder form-control-sm form-control`
- **Input Type**: `select-one`
- **Element Rect**: Left: 780, Width: 169.59375, Height: 28

**Dropdown Text Observed**: `"Frequency...AnnualMonthlyFortnightlyWeekly"`

**Available Options** (4):
```xml
<option value="">Clear</option>
<option value="Annual">Annual</option>
<option value="Monthly">Monthly</option>
<option value="Fortnightly">Fortnightly</option>
<option value="Weekly">Weekly</option>
```

**Selection Example**:
```python
# Select by value
select_option("#frequency", value="Annual")

# Or by visible text
select_option("#frequency", text="Monthly")
```

---

### 3. Amount Field (Income Amount)

**Field Properties**:
- **ID**: `amount`
- **CSS Selector**: `#amount`
- **XPath**: `//*[@id="amount"]`
- **Tag**: `input`
- **Type**: `text`
- **Classes**: `align-right border-radius-right form-control-sm form-control`
- **Element Rect**: Left: 983.46875, Height: 28
- **Input Style**: Right-aligned (currency formatting)

**Input Pattern Observed**:
User types progressively: `1 → 10 → 100 → 1000 → 10000`

**Automation Pattern**:
```python
amount_field = find_element("#amount")
clear_field(amount_field)
type_text(amount_field, "10000")  # Direct value entry recommended
```

---

## Workflow Patterns

### Standard Other Income Entry Function

```python
def add_other_income_entry(
    income_type,
    frequency,
    amount
):
    """
    Adds a single other income entry to the Other Income form

    Args:
        income_type (str): One of 4 types: "Dividends", "Family Allowance", "Maintenance", "Other"
        frequency (str): "Annual", "Monthly", "Fortnightly", or "Weekly"
        amount (float): Income amount

    Returns:
        bool: True if successful, False otherwise
    """

    try:
        # STEP 1: Click "Add Income" button
        print(f"Clicking Add Income button...")
        add_button = wait_for_element(
            selector="#btn_d53c37a8-0cf4-4604-bbfb-6b19670998ec",
            timeout=10
        )
        click(add_button)
        time.sleep(1)

        # STEP 2: Select income type
        print(f"Selecting income type: {income_type}...")
        type_dropdown = wait_for_element("#type", timeout=5)
        select_option(type_dropdown, value=income_type)
        time.sleep(0.5)

        # STEP 3: Select frequency
        print(f"Selecting frequency: {frequency}...")
        frequency_dropdown = wait_for_element("#frequency", timeout=5)
        select_option(frequency_dropdown, value=frequency)
        time.sleep(0.5)

        # STEP 4: Enter amount
        print(f"Entering amount: ${amount}...")
        amount_field = wait_for_element("#amount", timeout=5)
        clear_field(amount_field)
        type_text(amount_field, str(amount))
        time.sleep(0.5)

        # STEP 5: Auto-save wait
        print(f"Waiting for auto-save...")
        time.sleep(2)

        print(f"✓ Successfully added other income: {income_type}")
        return True

    except Exception as e:
        print(f"✗ Error adding other income: {str(e)}")
        return False
```

---

### Example Usage - Multiple Income Sources

```python
# Navigate to Other Income section first
navigate_to_other_income()

# Example other income entries to add
income_entries = [
    {
        "type": "Dividends",
        "frequency": "Annual",
        "amount": 5000
    },
    {
        "type": "Family Allowance",
        "frequency": "Fortnightly",
        "amount": 350
    },
    {
        "type": "Maintenance",
        "frequency": "Monthly",
        "amount": 1200
    },
    {
        "type": "Other",
        "frequency": "Weekly",
        "amount": 200
    }
]

# Add each income entry
for income in income_entries:
    success = add_other_income_entry(
        income_type=income["type"],
        frequency=income["frequency"],
        amount=income["amount"]
    )
    if not success:
        print(f"Failed to add income: {income['type']}")
        break

    print(f"Added {income['type']} - ${income['amount']} {income['frequency']}")
```

---

## Timing and Wait Strategies

### Recommended Wait Times

| Action | Wait Time | Wait Strategy | Selector to Wait For |
|--------|-----------|---------------|---------------------|
| After clicking "Add Income" | 1 second | presence_of_element | #type |
| After income type selection | 0.5 seconds | fixed_wait | N/A |
| After frequency selection | 0.5 seconds | fixed_wait | N/A |
| After amount input | 0.5 seconds | fixed_wait | N/A |
| After save/complete | 2 seconds | fixed_wait | N/A |

### Performance Metrics from Recording

- **Average Time Between Actions**: 1.18 seconds
- **Total Wait Time Observed**: 39,644ms (~40 seconds)
- **Estimated Maximum Timeout**: 39,613ms (~40 seconds)
- **Recommended Global Timeout**: 40 seconds
- **Primary Wait Strategy**: presence_of_element
- **Total Events Captured**: 70
- **Recording Duration**: 1m 22s (82 seconds)

---

## Complete Selector Reference

### CSS Selectors Quick Reference

```css
/* Navigate to Financials */
#financials > span.TabButton-module_tab-button-elem__AV3Ub:nth-of-type(2)

/* Other Income button */
#incomes > span

/* Add Income button */
#btn_d53c37a8-0cf4-4604-bbfb-6b19670998ec

/* Form fields */
#type                  /* Income type dropdown */
#frequency             /* Frequency dropdown */
#amount                /* Income amount */
```

### XPath Selectors Quick Reference

```xpath
/* Financials tab */
#financials > span.TabButton-module_tab-button-elem__AV3Ub:nth-of-type(2)

/* Other Income button */
/html[1]/body[1]/div[1]/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/button[6]/span[1]

/* Add Income button */
//*[@id="btn_d53c37a8-0cf4-4604-bbfb-6b19670998ec"]

/* Form field IDs */
//*[@id="type"]
//*[@id="frequency"]
//*[@id="amount"]
```

---

## Error Handling and Edge Cases

### Common Issues and Solutions

#### 1. Add Income Button Not Clickable

**Cause**: Button not ready or already in edit mode
**Solution**: Retry with explicit wait

```python
for attempt in range(3):
    try:
        add_button = wait_for_element("#btn_d53c37a8-0cf4-4604-bbfb-6b19670998ec", timeout=5)
        click(add_button)
        wait_for_element("#type", timeout=3)
        break
    except TimeoutException:
        if attempt == 2:
            raise
        time.sleep(1)
```

#### 2. Income Type Dropdown Not Opening

**Cause**: Form not fully loaded
**Solution**: Wait for element to be interactive

```python
type_dropdown = wait_for_element("#type", timeout=5)
wait_until_clickable(type_dropdown)
select_option(type_dropdown, value=income_type)
```

#### 3. Amount Field Not Accepting Input

**Cause**: Field not cleared or numeric validation
**Solution**: Clear first, then type

```python
amount_field = find_element("#amount")
clear_field(amount_field)
time.sleep(0.2)  # Brief wait for clear
type_text(amount_field, str(amount))

# Verify input
entered_value = get_value(amount_field)
if entered_value != str(amount):
    clear_field(amount_field)
    type_text(amount_field, str(amount))
```

#### 4. Frequency Dropdown Shows Wrong Value

**Cause**: Value attribute vs display text mismatch
**Solution**: Use exact value/text match

```python
# Recommended: Use value attribute
select_option("#frequency", value="Annual")

# Or use exact text match
select_option("#frequency", text="Annual")
```

#### 5. Stale Element After Type Selection

**Cause**: Form updates dynamically
**Solution**: Re-locate elements

```python
try:
    frequency_dropdown = find_element("#frequency")
    select_option(frequency_dropdown, value=frequency)
except StaleElementReferenceException:
    # Re-locate element
    frequency_dropdown = find_element("#frequency")
    select_option(frequency_dropdown, value=frequency)
```

---

## Testing Checklist

### Before Running Automation

- [ ] Verify on Other Income page (correct tab selected)
- [ ] Check form is loaded and visible
- [ ] Confirm no existing entries that might conflict
- [ ] Validate input data (income types match list, values numeric)
- [ ] Verify frequency options are valid

### After Each Entry

- [ ] Income type shows correct selection
- [ ] Frequency dropdown shows selected option
- [ ] Amount field displays correct value
- [ ] No error messages visible
- [ ] Entry appears in table (if visible)

### After All Entries

- [ ] Total entries matches expected count
- [ ] All amounts correctly formatted
- [ ] All frequencies correctly set
- [ ] Form ready for save/submit

---

## Quick Start Guide for AI Agent

### Minimal Working Example

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Navigate to page (assuming already logged in)
driver.get("https://crm.connective.com.au/#/")

# Go to Financials
financials_tab = driver.find_element(By.CSS_SELECTOR, "#financials > span")
financials_tab.click()
time.sleep(2)

# Click Other Income
income_button = driver.find_element(By.CSS_SELECTOR, "#incomes > span")
income_button.click()
time.sleep(2)

# Click Add Income
add_button = driver.find_element(By.ID, "btn_d53c37a8-0cf4-4604-bbfb-6b19670998ec")
add_button.click()
time.sleep(1)

# Add dividend income
# 1. Select income type
income_type = Select(driver.find_element(By.ID, "type"))
income_type.select_by_visible_text("Dividends")
time.sleep(0.5)

# 2. Select frequency
frequency = Select(driver.find_element(By.ID, "frequency"))
frequency.select_by_visible_text("Annual")
time.sleep(0.5)

# 3. Enter amount
amount_field = driver.find_element(By.ID, "amount")
amount_field.clear()
amount_field.send_keys("5000")
time.sleep(2)

print("✓ Income added successfully")
```

---

## Summary Statistics

### Recording Metadata
- **Session Name**: connectiveemployment (Note: Actually "Other Income")
- **Recording Date**: 2025-10-06
- **Recording Time**: 05:47:51 - 05:49:14 UTC
- **Total Duration**: 1m 22s (82 seconds)
- **Total Events Captured**: 70
  - Browser clicks: 40
  - Browser inputs: 27
  - Voice annotations: 1

### Element Counts
- **Total Income Types**: 4
- **Form Fields**: 3 (all required)
- **Frequency Options**: 4

### Performance Metrics
- **Complexity Score**: 5/10 (simple form)
- **Tab Switches Required**: 0
- **Forms Submitted**: 0 (auto-save)
- **Average Action Time**: 1.18 seconds
- **Total Wait Time**: 39,644ms (~40 seconds)
- **Dynamic Elements**: 0

### Comparison with Other Forms

| Aspect | Living Expenses | Assets - Other | Liabilities | Other Income |
|--------|-----------------|----------------|-------------|--------------|
| Categories | 21 expense types | 18 asset types | 18 liability types | 4 income types |
| Form Fields | 3 per entry | 4-5 per entry | 9-12 per entry | 3 per entry |
| Average Action Time | 1.67 seconds | 1.10 seconds | 0.99 seconds | 1.18 seconds |
| Special Features | Frequency dropdown | Motor Vehicle conditional | Clearing checkbox | Simple 3-field form |
| Complexity | Moderate | Moderate | Moderate-High | Low (simplest!) |

---

## Critical Implementation Notes

1. **4 Income Types Total** - Dividends, Family Allowance, Maintenance, Other
2. **Simplest Form** - Only 3 fields required per entry
3. **No Optional Fields** - All fields must be completed
4. **Frequency Options** - Same as other forms: Annual, Monthly, Fortnightly, Weekly
5. **Auto-Save Pattern** - No explicit save button, triggers on field completion
6. **Progressive Input** - Users type incrementally (1→10→100→1000→10000)
7. **Same Timing as Assets** - ~40 second max timeout
8. **No Dual Application Fields** - No ownership allocation needed
9. **Value Attribute Matching** - Use exact value matching for dropdowns
10. **Fast Entry** - Can complete in under 5 seconds per entry

---

**Document Version**: 1.0
**Created**: 2025-10-06
**Based on Recording**: connectiveemployment.json (actually Other Income)
**Total Income Types Documented**: 4
**Total Events Analyzed**: 70
**Recording Duration**: 1 minute 22 seconds
**Status**: ✅ Production-Ready Documentation
