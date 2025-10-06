# Liabilities - Detailed Automation Guide

> **Parent Reference**: [COMPLETE_CONNECTIVE_CRM_REFERENCE.md](../COMPLETE_CONNECTIVE_CRM_REFERENCE.md)
> **CRM Tab**: Financials → Liabilities
> **Integration Status**: ✅ Patterns documented for automation
> **Last Updated**: 2025-10-06

---

**🔗 Navigation**
- ⬆️ [Master Reference](../COMPLETE_CONNECTIVE_CRM_REFERENCE.md)
- 📙 [Living Expenses Guide](./living_expenses.md)
- 📘 [Assets - Other Guide](./assets_other.md)

---

## 📋 Table of Contents

1. [Overview](#overview)
2. [Navigation Path](#navigation-path)
3. [Complete Liability Type List](#complete-liability-type-list-18-types)
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
The Liabilities section in Connective Financial CRM captures debt and financial obligation information for loan applications, including credit cards, loans, mortgages, and other financial liabilities.

### User Workflow (From Voice Annotations)

**Annotation 1 (8.9s)**:
> _"I am logging the liabilities in connective serum and about to click the plus liabilities to begin"_

**Annotation 2 (176.4s / 2m 56s)**:
> _"there are 18 types of liabilities these include buy Now Pay Later car loan commercial Bill credit card hacks hire purchase lease line of credit loan is guarantor mortgage loan are the loan outstanding taxation overdraft personal loan business loan store card term loan other"_

### Form Structure
- **Primary liability type dropdown** (18 categories)
- **Comprehensive fields** for account details, balances, repayments
- **Ownership allocation options** for dual applications
- **Clearing from loan checkbox** for refinancing scenarios
- **Security linking** for asset-backed liabilities
- **Auto-save mechanism** (no explicit submit button)

### ⚠️ Critical Requirements
- **Page Load Timeout**: 79 seconds max observed (79,414ms)
- **Average Action Time**: 0.99 seconds (FASTEST form in CRM!)
- **Total Wait Time**: ~79 seconds for complete workflow
- **Complexity Score**: 5/10 (moderate with comprehensive fields)

---

## Navigation Path

### To Access Financials Section
```
1. Click: #financials > span.TabButton-module_tab-button-elem__AV3Ub:nth-of-type(2)
   Text: "Financials"

2. Section appears with financial subsections
```

### Liabilities Button
```css
Selector: #liabilities > span
Text: "Liabilities"
XPath: /html[1]/body[1]/div[1]/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/button[4]/span[1]
```

### Add Liability Button
```css
Selector: #btn_e679a8ad-4968-42e0-85c8-4b2ac4961f0e
XPath: //*[@id="btn_e679a8ad-4968-42e0-85c8-4b2ac4961f0e"]
Tag: button
Text: "Liability"
Classes: btn btn-light btn-sm
```

---

## Complete Liability Type List (18 Types)

All liability types available in the primary dropdown:

| # | Liability Type | Description | Common Use Case |
|---|----------------|-------------|-----------------|
| 1 | **Buy Now Pay Later** | BNPL services | AfterPay, Zip, Klarna |
| 2 | **Car Loan** | Vehicle financing | Auto loans, vehicle purchase |
| 3 | **Commercial Bill** | Short-term business debt | Business financing, trade bills |
| 4 | **Credit Card** | Revolving credit | Personal/business credit cards |
| 5 | **HECS** | Education debt | Government student loans |
| 6 | **Hire Purchase** | Asset purchase agreement | Equipment/vehicle financing |
| 7 | **Lease** | Rental/lease obligations | Vehicle/equipment leases |
| 8 | **Line of Credit** | Flexible borrowing facility | Business/personal line of credit |
| 9 | **Loan as Guarantor** | Guaranteed loans | Third-party loan guarantees |
| 10 | **Mortgage** | Property loan | Home/investment mortgages |
| 11 | **Loan ATO** | Tax office debt | ATO payment plans |
| 12 | **Loan Outstanding Taxation** | Outstanding tax debt | Tax liabilities, unpaid tax |
| 13 | **Overdraft** | Bank account overdraft | Overdraft facilities |
| 14 | **Personal Loan** | Unsecured personal debt | Personal borrowing |
| 15 | **Business Loan** | Business debt | Commercial borrowing |
| 16 | **Store Card** | Retail credit cards | Department store cards |
| 17 | **Term Loan** | Fixed-term loan | Structured lending |
| 18 | **Other** | Miscellaneous liabilities | Catch-all category |

### Table Structure

The Liabilities table displays:
```
Liability Type | Institution | Account Name | Security | Balance | Limit | Repayment (frequency)
```

**Example Entry**:
```
Buy Now Pay Later | AfterPay | Personal Account | [Linked Asset] | $5,000 | $10,000 | $500 Monthly
```

---

## Form Fields Reference

### 1. Liability Type Dropdown (Primary Selection)

**Field Properties**:
- **ID**: `name`
- **CSS Selector**: `#name`
- **XPath**: `//*[@id="name"]`
- **Tag**: `select`
- **Classes**: `undefined form-item__element--select text-placeholder form-control-sm form-control`
- **Input Type**: `select-one`
- **Element Rect**: Left: 368.53125, Width: 112.28125, Height: 28

**Available Options** (18):
```xml
<option value="">Liability Type...</option>
<option value="">Clear Liability Type</option>
<option value="Buy Now Pay Later">Buy Now Pay Later</option>
<option value="Car Loan">Car Loan</option>
<option value="Commercial Bill">Commercial Bill</option>
<option value="Credit Card">Credit Card</option>
<option value="HECS">HECS</option>
<option value="Hire Purchase">Hire Purchase</option>
<option value="Lease">Lease</option>
<option value="Line of Credit">Line of Credit</option>
<option value="Loan as Guarantor">Loan as Guarantor</option>
<option value="Mortgage">Mortgage</option>
<option value="Loan ATO">Loan ATO</option>
<option value="Loan Outstanding Taxation">Loan Outstanding Taxation</option>
<option value="Overdraft">Overdraft</option>
<option value="Personal Loan">Personal Loan</option>
<option value="Business Loan">Business Loan</option>
<option value="Store Card">Store Card</option>
<option value="Term Loan">Term Loan</option>
<option value="Other">Other</option>
```

**Selection Example**:
```python
# Select by value
select_option("#name", value="Buy Now Pay Later")

# Or by visible text
select_option("#name", text="Credit Card")
```

---

### 2. Institution Field

**Field Properties**:
- **ID**: `institution`
- **CSS Selector**: `#institution`
- **XPath**: `//*[@id="institution"]`
- **Tag**: `input`
- **Type**: `text`
- **Classes**: `form-control-sm form-control`
- **Element Rect**: Left: 368.53125, Width: 112.28125, Height: 28

**Example Values**:
- "Commonwealth Bank"
- "Westpac"
- "AfterPay"
- "NAB"

---

### 3. Account Name Field

**Field Properties**:
- **ID**: `accountName`
- **CSS Selector**: `#accountName`
- **XPath**: `//*[@id="accountName"]`
- **Tag**: `input`
- **Type**: `text`
- **Classes**: `form-control-sm form-control`

**Example Values**:
- "Personal Credit Card"
- "Home Loan Account"
- "Business Line of Credit"

---

### 4. Account BSB Field (Optional)

**Field Properties**:
- **ID**: `accountBSB`
- **CSS Selector**: `#accountBSB`
- **XPath**: `//*[@id="accountBSB"]`
- **Tag**: `input`
- **Type**: `text`
- **Classes**: `form-control-sm form-control`

**Format**: 6 digits (e.g., "063-000")

---

### 5. Account Number Field (Optional)

**Field Properties**:
- **ID**: `accountNumber`
- **CSS Selector**: `#accountNumber`
- **XPath**: `//*[@id="accountNumber"]`
- **Tag**: `input`
- **Type**: `text`
- **Classes**: `form-control-sm form-control`

**Format**: Varies by institution (e.g., "12345678")

---

### 6. Balance Field (Outstanding Amount)

**Field Properties**:
- **ID**: `value`
- **CSS Selector**: `#value`
- **XPath**: `//*[@id="value"]`
- **Tag**: `input`
- **Type**: `text`
- **Classes**: `align-right border-radius-right form-control-sm form-control`
- **Element Rect**: Left: 844.40625, Width: 88.40625, Height: 28
- **Input Style**: Right-aligned (currency formatting)

**Purpose**: Current outstanding balance of the liability

**Input Pattern Observed**:
User types progressively: `5 → 50 → 500 → 5000`

**Automation Pattern**:
```python
balance_field = find_element("#value")
clear_field(balance_field)
type_text(balance_field, "5000")  # Direct value entry recommended
```

---

### 7. Limit Field (Credit Limit)

**Field Properties**:
- **ID**: `limit`
- **CSS Selector**: `#limit`
- **XPath**: `//*[@id="limit"]`
- **Tag**: `input`
- **Type**: `text`
- **Classes**: `align-right border-radius-right form-control-sm form-control`
- **Input Style**: Right-aligned (currency formatting)

**Purpose**: Maximum credit limit or approved amount

**Example Values**:
- "10000" (Credit Card limit)
- "500000" (Mortgage limit)
- "15000" (Personal loan approved amount)

---

### 8. Repayment Field (Periodic Payment Amount)

**Field Properties**:
- **ID**: `accountRepayment`
- **CSS Selector**: `#accountRepayment`
- **XPath**: `//*[@id="accountRepayment"]`
- **Tag**: `input`
- **Type**: `text`
- **Classes**: `align-right border-radius-right form-control-sm form-control`
- **Element Rect**: Left: 618.40625, Width: 88.40625, Height: 28
- **Input Style**: Right-aligned (currency formatting)

**Purpose**: Regular repayment amount

---

### 9. Repayment Frequency Dropdown

**Field Properties**:
- **ID**: `accountRepaymentFrequency`
- **CSS Selector**: `#accountRepaymentFrequency`
- **XPath**: `//*[@id="accountRepaymentFrequency"]`
- **Tag**: `select`
- **Classes**: `undefined form-item__element--select form-control-sm form-control`
- **Input Type**: `select-one`

**Available Options** (4):
```xml
<option value="">Clear</option>
<option value="annually">Annual</option>
<option value="monthly">Monthly</option>
<option value="fortnightly">Fortnightly</option>
<option value="weekly">Weekly</option>
```

**Selection Examples**:
```python
# Select by value
select_option("#accountRepaymentFrequency", value="monthly")

# Select by visible text
select_option("#accountRepaymentFrequency", text="Monthly")
```

---

### 10. Security Field (Linked Assets)

**Display**: Column header visible in table: "Security"

**Implementation**: No direct input field. Security is managed through:
- **"Security Details"** link/button
- **"Link/Unlink Assets"** functionality

**Note**: Security appears to be linked/associated with existing assets rather than typed in directly.

---

### 11. "Clearing from this Loan?" Checkbox

**Field Properties**:
- **Name**: `accountClearingFromLoan`
- **Tag**: `input`
- **Type**: `checkbox`
- **Classes**: `custom-control-input`
- **Value**: `on`

**Label Text**: "Clearing from this loan?"
**Label Selector**: `.custom-control-label`

**Purpose**: Indicates if this liability is being cleared/paid off from the new loan (refinancing)

**Usage**:
```python
# Check the checkbox
clearing_checkbox = find_element("[name='accountClearingFromLoan']")
check(clearing_checkbox)
```

---

### 12. Ownership Allocation Options

**Available Options**:
- **Allocate Evenly** - Split liability evenly between applicants
- **Custom...** - Custom allocation percentages
- **Equal Ownership** - Equal ownership of the liability

**Button Selector**: `.dropdown-item`

**Usage**:
```python
# Open ownership dropdown (if applicable)
ownership_dropdown_button = find_element_by_text("Ownership")
click(ownership_dropdown_button)

# Select option
allocate_option = find_element_by_text("Allocate Evenly")
click(allocate_option)
```

---

## Workflow Patterns

### Standard Liability Entry Function

```python
def add_liability_entry(
    liability_type,
    institution,
    account_name,
    balance,
    limit,
    repayment_amount,
    repayment_frequency,
    account_bsb=None,
    account_number=None,
    clearing_from_loan=False,
    ownership="equal"
):
    """
    Adds a single liability entry to the Liabilities form

    Args:
        liability_type (str): One of 18 liability types
        institution (str): Financial institution name
        account_name (str): Account name/description
        balance (float): Current outstanding balance
        limit (float): Credit limit or approved amount
        repayment_amount (float): Regular repayment amount
        repayment_frequency (str): "annually", "monthly", "fortnightly", or "weekly"
        account_bsb (str, optional): Bank BSB number
        account_number (str, optional): Account number
        clearing_from_loan (bool): Whether clearing from this loan
        ownership (str): "equal", "allocate_evenly", or "custom"

    Returns:
        bool: True if successful, False otherwise
    """

    try:
        # STEP 1: Click "Add Liability" button
        print(f"Clicking Add Liability button...")
        add_button = wait_for_element(
            selector="#btn_e679a8ad-4968-42e0-85c8-4b2ac4961f0e",
            timeout=10
        )
        click(add_button)
        time.sleep(1)

        # STEP 2: Select liability type
        print(f"Selecting liability type: {liability_type}...")
        liability_dropdown = wait_for_element("#name", timeout=5)
        select_option(liability_dropdown, text=liability_type)
        time.sleep(1)  # Wait for form to update

        # STEP 3: Enter institution
        print(f"Entering institution: {institution}...")
        institution_field = wait_for_element("#institution", timeout=5)
        clear_field(institution_field)
        type_text(institution_field, institution)
        time.sleep(0.5)

        # STEP 4: Enter account name
        print(f"Entering account name: {account_name}...")
        account_name_field = wait_for_element("#accountName", timeout=5)
        clear_field(account_name_field)
        type_text(account_name_field, account_name)
        time.sleep(0.5)

        # STEP 5: Enter BSB (if provided)
        if account_bsb:
            print(f"Entering BSB: {account_bsb}...")
            bsb_field = wait_for_element("#accountBSB", timeout=5)
            clear_field(bsb_field)
            type_text(bsb_field, account_bsb)
            time.sleep(0.5)

        # STEP 6: Enter account number (if provided)
        if account_number:
            print(f"Entering account number: {account_number}...")
            account_number_field = wait_for_element("#accountNumber", timeout=5)
            clear_field(account_number_field)
            type_text(account_number_field, account_number)
            time.sleep(0.5)

        # STEP 7: Enter balance
        print(f"Entering balance: ${balance}...")
        balance_field = wait_for_element("#value", timeout=5)
        clear_field(balance_field)
        type_text(balance_field, str(balance))
        time.sleep(0.5)

        # STEP 8: Enter limit
        print(f"Entering limit: ${limit}...")
        limit_field = wait_for_element("#limit", timeout=5)
        clear_field(limit_field)
        type_text(limit_field, str(limit))
        time.sleep(0.5)

        # STEP 9: Enter repayment amount
        print(f"Entering repayment: ${repayment_amount}...")
        repayment_field = wait_for_element("#accountRepayment", timeout=5)
        clear_field(repayment_field)
        type_text(repayment_field, str(repayment_amount))
        time.sleep(0.5)

        # STEP 10: Select repayment frequency
        print(f"Selecting frequency: {repayment_frequency}...")
        frequency_dropdown = wait_for_element("#accountRepaymentFrequency", timeout=5)
        select_option(frequency_dropdown, value=repayment_frequency.lower())
        time.sleep(0.5)

        # STEP 11: Handle "Clearing from this loan?" checkbox
        if clearing_from_loan:
            print(f"Checking 'Clearing from this loan?'...")
            clearing_checkbox = find_element("[name='accountClearingFromLoan']")
            check(clearing_checkbox)
            time.sleep(0.5)

        # STEP 12: Handle ownership allocation (if dual application)
        if ownership == "allocate_evenly":
            print(f"Setting ownership to 'Allocate Evenly'...")
            allocate_button = find_element_by_text("Allocate Evenly")
            click(allocate_button)
            time.sleep(0.5)

        # STEP 13: Save entry (auto-save mechanism)
        print(f"Saving entry...")
        time.sleep(2)  # Wait for auto-save

        print(f"✓ Successfully added {liability_type}")
        return True

    except Exception as e:
        print(f"✗ Error adding liability: {str(e)}")
        return False
```

---

### Example Usage - Multiple Liabilities

```python
# Navigate to Liabilities section first
navigate_to_liabilities()

# Define liabilities to add
liabilities_to_add = [
    {
        "type": "Credit Card",
        "institution": "Commonwealth Bank",
        "account_name": "Visa Platinum",
        "balance": 5000,
        "limit": 15000,
        "repayment": 200,
        "frequency": "monthly"
    },
    {
        "type": "Car Loan",
        "institution": "Westpac",
        "account_name": "Vehicle Finance",
        "balance": 25000,
        "limit": 30000,
        "repayment": 800,
        "frequency": "monthly",
        "clearing": True
    },
    {
        "type": "Mortgage",
        "institution": "NAB",
        "account_name": "Home Loan",
        "balance": 450000,
        "limit": 500000,
        "repayment": 2500,
        "frequency": "monthly"
    }
]

for liability in liabilities_to_add:
    success = add_liability_entry(
        liability_type=liability["type"],
        institution=liability["institution"],
        account_name=liability["account_name"],
        balance=liability["balance"],
        limit=liability["limit"],
        repayment_amount=liability["repayment"],
        repayment_frequency=liability["frequency"],
        clearing_from_loan=liability.get("clearing", False)
    )
    if not success:
        print(f"Failed to add {liability['type']}")
        break
```

---

## Timing and Wait Strategies

### Recommended Wait Times

| Action | Wait Time | Wait Strategy | Selector to Wait For |
|--------|-----------|---------------|---------------------|
| After clicking Add Liability | 1 second | presence_of_element | #name |
| After liability type selection | 1 second | presence_of_element | #institution |
| After institution input | 0.5 seconds | fixed_wait | N/A |
| After account name input | 0.5 seconds | fixed_wait | N/A |
| After balance input | 0.5 seconds | fixed_wait | N/A |
| After limit input | 0.5 seconds | fixed_wait | N/A |
| After repayment input | 0.5 seconds | fixed_wait | N/A |
| After frequency selection | 0.5 seconds | fixed_wait | N/A |
| After save/complete | 2 seconds | fixed_wait | N/A |

### Performance Metrics from Recording

- **Average Time Between Actions**: 0.99 seconds (FASTEST form!)
- **Total Wait Time Observed**: 79,414ms (~79 seconds)
- **Estimated Maximum Timeout**: 79 seconds
- **Recommended Global Timeout**: 80 seconds
- **Primary Wait Strategy**: presence_of_element
- **Total Events Captured**: 504
- **Recording Duration**: 8m 19s (499 seconds)

---

## Complete Selector Reference

### CSS Selectors Quick Reference

```css
/* Navigate to Financials */
#financials > span.TabButton-module_tab-button-elem__AV3Ub:nth-of-type(2)

/* Liabilities button */
#liabilities > span

/* Add Liability button */
#btn_e679a8ad-4968-42e0-85c8-4b2ac4961f0e

/* Form fields */
#name                         /* Liability type dropdown */
#institution                  /* Institution name */
#accountName                  /* Account name */
#accountBSB                   /* BSB number (optional) */
#accountNumber                /* Account number (optional) */
#value                        /* Balance */
#limit                        /* Credit limit */
#accountRepayment             /* Repayment amount */
#accountRepaymentFrequency    /* Repayment frequency dropdown */

/* Checkbox */
[name="accountClearingFromLoan"]   /* Clearing from loan checkbox */
```

### XPath Selectors Quick Reference

```xpath
/* Financials tab */
#financials > span.TabButton-module_tab-button-elem__AV3Ub:nth-of-type(2)

/* Liabilities button */
/html[1]/body[1]/div[1]/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/button[4]/span[1]

/* Add Liability button */
//*[@id="btn_e679a8ad-4968-42e0-85c8-4b2ac4961f0e"]

/* Form field IDs */
//*[@id="name"]
//*[@id="institution"]
//*[@id="accountName"]
//*[@id="accountBSB"]
//*[@id="accountNumber"]
//*[@id="value"]
//*[@id="limit"]
//*[@id="accountRepayment"]
//*[@id="accountRepaymentFrequency"]
```

---

## Error Handling and Edge Cases

### Common Issues and Solutions

#### 1. Add Liability Button Not Clickable

**Cause**: Button not ready or already in edit mode
**Solution**: Retry with explicit wait

```python
for attempt in range(3):
    try:
        add_button = wait_for_element("#btn_e679a8ad-4968-42e0-85c8-4b2ac4961f0e", timeout=5)
        click(add_button)
        wait_for_element("#name", timeout=3)
        break
    except TimeoutException:
        if attempt == 2:
            raise
        time.sleep(1)
```

#### 2. Liability Type Dropdown Not Opening

**Cause**: Form not fully loaded
**Solution**: Wait for element to be interactive

```python
liability_dropdown = wait_for_element("#name", timeout=5)
wait_until_clickable(liability_dropdown)
select_option(liability_dropdown, text=liability_type)
```

#### 3. Currency Fields Not Accepting Input

**Cause**: Field not cleared or numeric validation
**Solution**: Clear first, then type

```python
balance_field = find_element("#value")
clear_field(balance_field)
time.sleep(0.2)  # Brief wait for clear
type_text(balance_field, str(balance))

# Verify input
entered_value = get_value(balance_field)
if entered_value != str(balance):
    clear_field(balance_field)
    type_text(balance_field, str(balance))
```

#### 4. Frequency Dropdown Shows Wrong Value

**Cause**: Value attribute vs display text mismatch
**Solution**: Use value attribute (lowercase)

```python
# Correct: Use value attribute
select_option("#accountRepaymentFrequency", value="monthly")

# Incorrect: Display text may not match
select_option("#accountRepaymentFrequency", text="Monthly")  # May fail
```

#### 5. Clearing Checkbox Not Checking

**Cause**: Dynamic ID or element not found
**Solution**: Use name attribute instead of ID

```python
# Instead of ID (which is dynamic):
# clearing_checkbox = find_element("#cb_clearing_[dynamic-id]_accountClearingFromLoan")

# Use name attribute:
clearing_checkbox = find_element("[name='accountClearingFromLoan']")
check(clearing_checkbox)
```

---

## Testing Checklist

### Before Running Automation

- [ ] Verify on Liabilities page (correct tab selected)
- [ ] Check form is loaded and visible
- [ ] Confirm no existing entries that might conflict
- [ ] Validate input data (liability types match list, values numeric)
- [ ] Verify institution names are correct

### After Each Entry

- [ ] Liability type shows correct selection
- [ ] Institution field displays entered text
- [ ] Account name field displays entered text
- [ ] Balance field shows correct amount
- [ ] Limit field shows correct amount
- [ ] Repayment field shows correct amount
- [ ] Repayment frequency dropdown shows selected option
- [ ] If clearing: checkbox is checked
- [ ] If dual application: ownership option selected
- [ ] No error messages visible

### After All Entries

- [ ] Total entries matches expected count
- [ ] All values correctly formatted
- [ ] All required fields populated
- [ ] Clearing checkboxes set correctly
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

# Click Liabilities
liabilities_button = driver.find_element(By.CSS_SELECTOR, "#liabilities > span")
liabilities_button.click()
time.sleep(2)

# Click Add Liability
add_button = driver.find_element(By.ID, "btn_e679a8ad-4968-42e0-85c8-4b2ac4961f0e")
add_button.click()
time.sleep(1)

# Add a credit card liability
# 1. Select liability type
liability_type = Select(driver.find_element(By.ID, "name"))
liability_type.select_by_visible_text("Credit Card")
time.sleep(1)

# 2. Enter institution
institution_field = driver.find_element(By.ID, "institution")
institution_field.clear()
institution_field.send_keys("Commonwealth Bank")
time.sleep(0.5)

# 3. Enter account name
account_name_field = driver.find_element(By.ID, "accountName")
account_name_field.clear()
account_name_field.send_keys("Visa Platinum")
time.sleep(0.5)

# 4. Enter balance
balance_field = driver.find_element(By.ID, "value")
balance_field.clear()
balance_field.send_keys("5000")
time.sleep(0.5)

# 5. Enter limit
limit_field = driver.find_element(By.ID, "limit")
limit_field.clear()
limit_field.send_keys("15000")
time.sleep(0.5)

# 6. Enter repayment
repayment_field = driver.find_element(By.ID, "accountRepayment")
repayment_field.clear()
repayment_field.send_keys("200")
time.sleep(0.5)

# 7. Select frequency
frequency = Select(driver.find_element(By.ID, "accountRepaymentFrequency"))
frequency.select_by_value("monthly")
time.sleep(2)

print("✓ Liability added successfully")
```

---

## Summary Statistics

### Recording Metadata
- **Session Name**: liabilitiesreal
- **Recording Date**: 2025-10-06
- **Recording Time**: 04:37:52 - 04:46:12 UTC
- **Total Duration**: 8m 19s (499 seconds)
- **Total Events Captured**: 504
  - Browser clicks: 279
  - Browser inputs: 221
  - Voice annotations: 2

### Element Counts
- **Total Liability Types**: 18
- **Form Fields**: 12 (9 required + 3 optional)
- **Repayment Frequency Options**: 4
- **Ownership Options**: 3

### Performance Metrics
- **Complexity Score**: 5/10 (moderate)
- **Tab Switches Required**: 0
- **Forms Submitted**: 0 (auto-save)
- **Average Action Time**: 0.99 seconds (FASTEST!)
- **Total Wait Time**: 79,414ms (~79 seconds)
- **Dynamic Elements**: 1 (ownership allocation)

### Comparison with Other Forms

| Aspect | Living Expenses | Assets - Other | Liabilities |
|--------|-----------------|----------------|-------------|
| Categories | 21 expense types | 18 asset types | 18 liability types |
| Form Fields | 3 per entry | 4-5 per entry | 9-12 per entry |
| Average Action Time | 1.67 seconds | 1.10 seconds | 0.99 seconds (fastest!) |
| Special Features | Frequency dropdown | Motor Vehicle conditional | Clearing checkbox, Security linking |
| Complexity | Moderate | Moderate | Moderate-High |

---

## Critical Implementation Notes

1. **18 Liability Types Total** - Buy Now Pay Later through Other
2. **Fastest Form** - 0.99s average between actions
3. **Comprehensive Fields** - Up to 12 fields per liability entry
4. **Clearing Checkbox** - Use name attribute `[name="accountClearingFromLoan"]`
5. **Frequency Values** - Use lowercase: "annually", "monthly", "fortnightly", "weekly"
6. **Auto-Save Pattern** - No explicit save button, triggers on field completion
7. **Ownership Options** - Equal, Allocate Evenly, or Custom for dual applications
8. **Security Linking** - Managed through separate "Link/Unlink Assets" functionality
9. **BSB/Account Optional** - Only required for certain liability types
10. **Progressive Input** - Users type incrementally (5→50→500→5000)

---

**Document Version**: 1.0
**Created**: 2025-10-06
**Based on Recording**: liabilitiesreal.json
**Total Liability Types Documented**: 18
**Total Events Analyzed**: 504
**Recording Duration**: 8 minutes 19 seconds
**Status**: ✅ Production-Ready Documentation
