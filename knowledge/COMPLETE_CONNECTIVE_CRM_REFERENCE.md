# Connective CRM - Complete System Reference

**Last Updated**: 2025-10-04
**Total Elements**: 74
**Sections**: 8
**Validated Workflows**: 3

---

## Table of Contents

1. [Executive Summary](#executive-summary)
2. [Complete Element Directory by Section](#complete-element-directory-by-section)
   - [Attachments Section](#attachments-section)
   - [BID & NCCP Section](#bid--nccp-section)
   - [Details Section](#details-section)
   - [Financials Section](#financials-section)
   - [Navigation Section](#navigation-section)
   - [Notes Section](#notes-section)
   - [Questionnaires Section](#questionnaires-section)
   - [Unknown/Dashboard Section](#unknowndashboard-section)
3. [All Dropdown Fields with Complete Options](#all-dropdown-fields-with-complete-options)
4. [Validated Workflows](#validated-workflows)
5. [Quick Reference Tables](#quick-reference-tables)
6. [Usage Examples](#usage-examples)

---

## Executive Summary

This reference contains **complete knowledge** of the Connective CRM loan application system, extracted from workflow recordings and validated through actual usage.

### System Statistics

| Metric | Count |
|--------|-------|
| **Total Elements** | 74 |
| **Buttons** | 43 |
| **Dropdown Fields (Select)** | 20 |
| **Text Input Fields** | 6 |
| **Navigation Tabs** | 3 |
| **Rich Text Editors** | 1 |
| **AG-Grid Components** | 1 |
| **Sections Mapped** | 8 |
| **Validated Workflows** | 3 |
| **Total Dropdown Options** | 286+ |

### What This Agent Knows

- **Complete CRM Structure**: All sections, tabs, and navigation
- **All Interactive Elements**: Every button, input field, dropdown, and control
- **All Selectors**: data-testid, ID, class, and best-practice selectors for each element
- **Complete Dropdown Options**: All 54 lenders, 63 property types, 19 agents, etc.
- **Validated Workflows**: Step-by-step instructions for common tasks
- **Modal Behavior**: Which elements trigger modals and their dependencies
- **Hidden Elements**: Elements that appear only after triggers
- **Framework Detection**: Froala editors, AG-Grid, React-Select components

---

## Complete Element Directory by Section

### Attachments Section

**Purpose**: Upload and manage loan application documents
**Total Elements**: 1

#### Elements

| Element | Type | Selector | Description | Notes |
|---------|------|----------|-------------|-------|
| **file_upload** | input | `#file` | File upload input | Hidden (`display:none`), triggered by Add button |

**Selector Details**:
```
ID: file
Type: file
Hidden: Yes (display:none but accessible via send_keys)
Trigger: [data-testid="Add"] button
```

**Usage**:
```python
# Must navigate to Attachments tab first
driver.find_element(By.ID, "attachments").click()
time.sleep(2)

# Click Add button to activate file input
driver.find_element(By.CSS_SELECTOR, "[data-testid='Add']").click()

# Send file path to hidden input
file_input = driver.find_element(By.ID, "file")
file_input.send_keys(r"C:\path\to\document.pdf")
```

---

### BID & NCCP Section

**Purpose**: Compliance workflow for Best Interests Duty and NCCP requirements
**Total Elements**: 3

#### Elements

| Element | Type | Selector | Label |
|---------|------|----------|-------|
| **compliance_stage_1** | button | `[data-testid="CREDIT_GUIDE"]` | Stage 1 - Credit Guide |
| **compliance_stage_2** | button | `[data-testid="PRELIM_ASSESSMENT"]` | Stage 2 - Preliminary Assessment |
| **compliance_stage_3** | button | `[data-testid="CPD_AND_SUBMISSION"]` | Stage 3 - SoRCP and Submission |

**Workflow**:
1. Click Stage 1 to complete Credit Guide
2. Click Stage 2 for Preliminary Assessment
3. Click Stage 3 for Statement of Reasons and Submission

**Access**: Navigate via `#newCompliance` tab

---

### Details Section

**Purpose**: Core applicant and loan details
**Total Elements**: 5

#### Elements

| Element | Type | Selector | Label | Purpose |
|---------|------|----------|-------|---------|
| **details** | button | `#details` | Details Tab | Navigate to details section |
| **employment** | button | `#employment` | Employment Tab | Navigate to employment info |
| **incomes** | button | `#incomes` | Incomes Tab | Navigate to income details |
| **amount** | input | `#amount` | Amount | Enter loan or income amount |
| **Add Income** | button | `[data-testid="Add"]` | Add Income | Add new income source |

**Section Navigation**:
```
#details → Main applicant details
#employment → Employment information
#incomes → Income sources and amounts
```

---

### Financials Section

**Purpose**: Comprehensive financial assessment including assets, liabilities, expenses
**Total Elements**: 38

#### Navigation Buttons (4)

| Element | Selector | Purpose |
|---------|----------|---------|
| **financials** | `#financials` | Main Financials tab |
| **realEstateAssets** | `#realEstateAssets` | Real estate assets sub-section |
| **otherAssets** | `#otherAssets` | Other assets sub-section |
| **liabilities** | `#liabilities` | Liabilities sub-section |

#### Expense Category Buttons (3)

| Element | Selector | Category |
|---------|----------|----------|
| **btn_Living_Expense** | `[text="Living Expense"]` | Living expenses |
| **btn_Childcare** | `[text="Childcare"]` | Childcare expenses |
| **btn_Child_&_Spouse_Maintenance** | `[text="Child & Spouse Maintenance"]` | Maintenance payments |

#### Add/Action Buttons (4)

| Element | Selector | Purpose |
|---------|----------|---------|
| **Add Real Estate** | `[data-testid="Add"]` (in Real Estate section) | Add property |
| **Add Loan** | `[data-testid="Add Loan"]` | Add loan to property |
| **Add Other Asset** | `[data-testid="Add"]` (in Other Assets) | Add non-real estate asset |
| **Add Liability** | `[data-testid="Add"]` (in Liabilities) | Add new liability |

#### Real Estate Fields (11)

| Element | Type | Selector | Options/Purpose |
|---------|------|----------|-----------------|
| **propertyType** | select | `#propertyType` | 63 property types |
| **propertyTitleType** | select | `#propertyTitleType` | 15 title types |
| **propertyStatus** | select | `#propertyStatus` | 5 status options |
| **realEstateZoning** | select | `#realEstateZoning` | 4 zoning types |
| **realEstatePurpose** | select | `#realEstatePurpose` | 2 purpose options |
| **valueBasis** | select | `#valueBasis` | 4 valuation methods |
| **realEstateUseAsSecurity** | input | `[name="realEstateUseAsSecurity"]` | Checkbox |
| **realEstateToBePurchased** | input | `[name="realEstateToBePurchased"]` | Checkbox |
| **value** | button | `#value` | Property value field |
| **OwnershipAllocate** | button | `[data-testid="ownershipComponent"]` | Ownership allocation |
| **input_form-control** | button | `[class="form-control"]` | Generic form input |

#### Loan/Account Fields (8)

| Element | Selector | Purpose |
|---------|----------|---------|
| **institution** | `#institution` | Financial institution |
| **accountName** | `#accountName` | Account name |
| **accountBSB** | `#accountBSB` | BSB number |
| **accountNumber** | `#accountNumber` | Account number |
| **interestRate** | `#interestRate` | Interest rate |
| **accountRepayment** | `#accountRepayment` | Repayment amount |
| **limit** | `#limit` | Credit limit |
| **accountRepaymentFrequency** | `#accountRepaymentFrequency` | 5 frequency options |

#### Liability Fields (3)

| Element | Type | Selector | Options/Purpose |
|---------|------|----------|-----------------|
| **name** | select | `#name` | 19 liability types |
| **priority** | select | `#priority` | 4 priority options |
| **accountClearingFromLoan** | input | `[name="accountClearingFromLoan"]` | Clearing checkbox |

#### Other Income Fields (2)

| Element | Type | Selector | Options |
|---------|------|----------|---------|
| **frequency** | select | `#frequency` | 5 frequency options |
| **type** | select | `#type` | 5 income types |

#### Additional Components (3)

| Element | Selector | Purpose |
|---------|----------|---------|
| **input_custom-control-input** | `[class="custom-control-input"]` | Custom checkbox |
| **input_rbt-input-main** | `[class="rbt-input-main"]` | React Bootstrap Typeahead |
| **Liability Tab Container** | `[data-testid="financials-liability-tab-container"]` | Liability container |

---

### Navigation Section

**Purpose**: Tab navigation between major CRM sections
**Total Elements**: 3

#### Elements

| Element | Type | Selector | Destination |
|---------|------|----------|-------------|
| **attachments_tab** | tab | `#attachments` | Attachments section |
| **questionnaires_tab** | tab | `#questionnaires` | Questionnaires section |
| **compliance_tab** | tab | `#newCompliance` | BID & NCCP compliance |

---

### Notes Section

**Purpose**: Add notes and communications to the opportunity
**Total Elements**: 5

#### Elements

| Element | Type | Selector | Options/Purpose |
|---------|------|----------|-----------------|
| **add_note_button** | button | `#btn_[uuid]` | Triggers note modal |
| **create_note_button** | button | `[data-testid="createNote"]` | Submit note |
| **note_type** | select | `#noteType` | 13 note types |
| **user_id** | select | `#userID` | User selection (dynamic) |
| **note_content** | rich_text | `.fr-element.fr-view` | Froala rich text editor |

**Note Types (13)**:
1. Appointment
2. Compliance
3. Email In
4. Email Out
5. Fax In
6. Fax Out
7. General Note
8. Letter In
9. Letter Out
10. Phone In
11. Phone Out
12. SMS
13. Voicemail Message

**Usage**:
```python
# Click add note button
driver.find_element(By.CSS_SELECTOR, "[data-testid='addNoteToOpportunity']").click()
time.sleep(1)

# Select note type
Select(driver.find_element(By.ID, "noteType")).select_by_visible_text("Phone Out")

# Add content via JavaScript (Froala editor)
driver.execute_script("""
    document.querySelector('.fr-element.fr-view').innerHTML = 'Called client to discuss loan options';
""")

# Submit
driver.find_element(By.CSS_SELECTOR, "[data-testid='createNote']").click()
```

---

### Questionnaires Section

**Purpose**: Complete required questionnaires for loan application
**Total Elements**: 1

#### Elements

| Element | Type | Selector | Framework | Purpose |
|---------|------|----------|-----------|---------|
| **questionnaire_grid** | ag_grid | `.ag-cell` | AG-Grid | Select questionnaire from grid |

**Available Questionnaires**:
- Home Loan - Needs Analysis
- Asset Finance - Needs Analysis
- Personal Loan - Needs Analysis
- Consent to perform a Credit Check

**Usage**:
```python
# Navigate to questionnaires
driver.find_element(By.ID, "questionnaires").click()
time.sleep(2)

# Click Add
driver.find_element(By.CSS_SELECTOR, "[data-testid='Add']").click()
time.sleep(1)

# Find and click questionnaire in AG-Grid
cells = driver.find_elements(By.CLASS_NAME, "ag-cell")
for cell in cells:
    if "Home Loan - Needs Analysis" in cell.text:
        cell.click()
        break

# Click Choose
driver.find_element(By.CSS_SELECTOR, "[data-testid='Choose']").click()
time.sleep(3)
```

---

### Unknown/Dashboard Section

**Purpose**: Dashboard and main opportunity controls
**Total Elements**: 16

#### Dashboard Buttons (3)

| Element | Selector | Label |
|---------|----------|-------|
| **btn_Opportunity** | `[text="Opportunity"]` | Opportunity button |
| **btn_Home_Loans** | `[text="Home Loans"]` | Home Loans section |
| **btn_Product_and_Security** | `[data-testid="formFeedback-undefined"]` | Product and Security |

#### Loan Details Fields (4)

| Element | Selector | Purpose |
|---------|----------|---------|
| **loanAmount** | `#loanAmount` | Loan amount |
| **existingAmountText** | `#existingAmountText` | Existing loan amount |
| **securityValueText** | `#securityValueText` | Security value |
| **lmiText** | `#lmiText` | LMI amount |

#### Dropdown Fields (7)

| Element | Type | Selector | Options |
|---------|------|----------|---------|
| **agent** | select | `#agent` | 19 agents/brokers |
| **personResponsible** | select | `#personResponsible` | 15 staff members |
| **lender** | select | `#lender` | 54 lenders |
| **settlementOfficer** | select | `#settlementOfficer` | 15 staff members |
| **tranxType** | select | `#tranxType` | 6 transaction types |
| **transactionType** | select | `#transactionType` | 4 loan types |
| **campaignId** | select | `#campaignId` | Campaign selection |

#### Other Elements (2)

| Element | Type | Selector | Purpose |
|---------|------|----------|---------|
| **react-select-2-input** | button | `#react-select-2-input` | React-Select component |
| **sitRep** | input | `#sitRep` | Situation report field |

---

## All Dropdown Fields with Complete Options

### 1. Lender (54 options)
**Selector**: `#lender`
**Section**: Dashboard

```
1.  AMP
2.  ANZ
3.  Aussie Bonds
4.  Australian Military Bank
5.  Auswide Bank
6.  Bank of China
7.  Bank of Melbourne
8.  Bank of Queensland
9.  Bank SA
10. Bankwest
11. Better Choice Home Loans
12. Better Mortgage Management
13. Bluebay Home Loans
14. Commonwealth Bank
15. Connective Advance (Thinktank)
16. Connective Bridge (Bridgit)
17. Connective Complete (Connective)
18. Connective Elevate (Bluestone)
19. Connective Essentials (Advantedge)
20. Connective Home Loan Essentials
21. Connective Horizon (Brighten)
22. Connective Reverse (Household Capital)
23. Connective Select (Bendigo Bank)
24. Connective Solutions (Pepper Money)
25. Deposit Assure
26. Deposit Power (Deposit Bonds)
27. Firefighters Mutual Bank
28. Firstmac
29. Gateway Bank
30. Granite Home Loans
31. Health Professionals Bank
32. Heritage Bank
33. HomeStart Finance
34. ING
35. Keystart Home Loans
36. La Trobe Financial
37. Macquarie Bank
38. ME Bank
39. MyState
40. NAB
41. Newcastle Permanent
42. OwnHome
43. P & N Bank
44. Paramount Mortgage Services
45. People's Choice Credit Union
46. Pepper Money
47. RedZed
48. Resimac
49. St George Bank
50. Suncorp Bank
51. Teachers Mutual Bank
52. Ubank
53. UniBank
54. Westpac
```

### 2. Property Type (63 options)
**Selector**: `#propertyType`
**Section**: Financials

```
1.  Property Type...
2.  Apartment/Unit/Flat
3.  Bedsitter Bachelor
4.  Boarding House
5.  Combi Shop Residence
6.  Commercial
7.  Company Title Unit
8.  Converted Commercial Property
9.  Converted Industrial Property
10. Converted Motel Units
11. Converted Property
12. Display Home
13. Duplex
14. Fully Detached House
15. Govt Rental Guarantee
16. Hobby Farm
17. Holiday Home
18. Holiday Rental
19. Industrial
20. Inner City Apartment
21. Kit Home
22. Licenced Builder House Construction
23. Luxury House
24. Luxury Other
25. Multiple On Title
26. New Strata Title Unit
27. Nursing Home
28. Owner Builder House Construction
29. Property Development
30. Relocatable Home
31. Rental Guarantee
32. Resort Unit
33. Retirement Unit
34. Semi Detached House
35. Serviced Apt
36. Single Bedroom Less 50m2
37. Snowlease
38. Strata Title Unit
39. Student Accommodation
40. Studio Warehouse Apt
41. Terrace
42. Timeshare
43. Townhouse
44. TransportableHome
45. Unit Student Accom
46. Vacant Land
47. Villa
48. Warehouse Conversion
49. Prof Chambers
50. Offices
51. Factory
52. Warehouse
53. Vacant Land (duplicate)
54. Retirement Village
55. Non Specialised Commercial
56. Residential Commercial
57. Other
58. Non Specialised Industrial
59. Light Industrial
60. Other (duplicate)
61. 8 Hectares Or Less
62. Over 8 Less Than 40 Hectares
63. Over 40 Hectares
```

### 3. Agent/Broker (19 options)
**Selector**: `#agent`
**Section**: Dashboard

```
1.  Benjamin Hawley
2.  Thomas Hawley
3.  Avril Clutterbuck
4.  Benjamin Ringer
5.  Corey Wild
6.  Dean Joffe
7.  Dom Dzakula
8.  Elia Theodore
9.  Harrison Favetti
10. James Curtis
11. James Ryan
12. Max Connley
13. Maximilian Harris
14. Nicholas  OSullivan
15. Oliver Studdy
16. Reuben Way
17. Thomas Dunkley
18. Timothy Perry
19. Tristan Cleggett
```

### 4. Liability Type (19 options)
**Selector**: `#name`
**Section**: Financials

```
1.  Buy Now Pay Later
2.  Car Loan
3.  Commercial Bill
4.  Credit Card
5.  HECS
6.  Hire Purchase
7.  Lease
8.  Line Of Credit
9.  Loan As Guarantor
10. Mortgage Loan
11. Other Loan
12. Outstanding Taxation
13. Overdraft
14. Personal Loan
15. Business Loan
16. Store Card
17. Term Loan
18. Other
```

### 5. Person Responsible (15 options)
**Selector**: `#personResponsible`
**Section**: Dashboard

```
1.  Benjamin Hawley
2.  Cat Manipol
3.  Christina Phan
4.  Genie Nguyen
5.  Isabelle Dib
6.  James Larkey
7.  Jay Huang
8.  Lyka Garcia
9.  Madeleine Konstan
10. Madeline Owees
11. Meg Robinson
12. Pra Mansour
13. Romer Andrews
14. Thomas Hawley
15. Select Other...
```

### 6. Settlement Officer (15 options)
**Selector**: `#settlementOfficer`
**Section**: Dashboard

```
1.  Benjamin Hawley
2.  Cat Manipol
3.  Christina Phan
4.  Genie Nguyen
5.  Isabelle Dib
6.  James Larkey
7.  Jay Huang
8.  Lyka Garcia
9.  Madeleine Konstan
10. Madeline Owees
11. Meg Robinson
12. Pra Mansour
13. Romer Andrews
14. Thomas Hawley
15. Select Other...
```

### 7. Property Title Type (15 options)
**Selector**: `#propertyTitleType`
**Section**: Financials

```
1.  Community Title
2.  Company Title
3.  Crown Land
4.  Crown Lease
5.  Freehold
6.  Group Titles Plan
7.  Leasehold
8.  Moiety Title
9.  None
10. Other Title
11. Purple Title
12. Strata Title
13. Stratum Title
14. Unit Title
```

### 8. Note Type (13 options)
**Selector**: `#noteType`
**Section**: Notes

```
1.  Appointment
2.  Compliance
3.  Email In
4.  Email Out
5.  Fax In
6.  Fax Out
7.  General Note
8.  Letter In
9.  Letter Out
10. Phone In
11. Phone Out
12. SMS
13. Voicemail Message
```

### 9. Transaction Type - Loan Type (6 options)
**Selector**: `#tranxType`
**Section**: Dashboard

```
1. FHO
2. Pre-Approval
3. Purchase
4. Refinance
5. Top up
6. Variation
```

### 10. Payment Frequency (5 options)
**Selector**: `#frequency`
**Section**: Financials

```
1. Annual
2. Monthly
3. Fortnightly
4. Weekly
```

### 11. Income/Other Type (5 options)
**Selector**: `#type`
**Section**: Financials

```
1. Dividends
2. Family Allowance
3. Maintenance
4. Other
```

### 12. Property Status (5 options)
**Selector**: `#propertyStatus`
**Section**: Financials

```
1. New Building
2. To Be Built
3. Established
4. Vacant Land
```

### 13. Real Estate Zoning (5 options)
**Selector**: `#realEstateZoning`
**Section**: Financials

```
1. Residential
2. Commercial
3. Industrial
4. Rural
```

### 14. Loan Priority (5 options)
**Selector**: `#priority`
**Section**: Financials

```
1. First
2. Second
3. Third
4. Fourth
```

### 15. Account Repayment Frequency (5 options)
**Selector**: `#accountRepaymentFrequency`
**Section**: Financials

```
1. Annual
2. Monthly
3. Fortnightly
4. Weekly
```

### 16. Transaction Type - Loan Category (4 options)
**Selector**: `#transactionType`
**Section**: Dashboard

```
1. Home Loans
2. Commercial Loans
3. Asset Finance
4. Business Loans
```

### 17. Valuation Basis (4 options)
**Selector**: `#valueBasis`
**Section**: Financials

```
1. Applicant Estimate
2. Certified Valuation
3. Actual Value
```

### 18. Real Estate Purpose (3 options)
**Selector**: `#realEstatePurpose`
**Section**: Financials

```
1. Owner Occupied
2. Investment
```

### 19. User ID (Dynamic)
**Selector**: `#userID`
**Section**: Notes

```
Format: CA109034:James Larkey (CA number followed by name)
Options are dynamically populated based on active users
```

---

## Validated Workflows

### Workflow 1: Add Note to Opportunity

**Status**: Validated
**Triggers Modal**: Yes

**Steps**:

1. **Click Add Note Button**
   - Selector: `[data-testid="addNoteToOpportunity"]`
   - Action: Click
   - Wait: Modal to appear

2. **Select Note Type**
   - Selector: `#noteType`
   - Action: Select from dropdown
   - Options: 13 note types available

3. **Select User (Optional)**
   - Selector: `#userID`
   - Action: Select from dropdown
   - Note: Auto-detected if not specified

4. **Enter Note Content**
   - Selector: `.fr-element.fr-view`
   - Action: Set innerHTML via JavaScript
   - Framework: Froala rich text editor
   ```javascript
   document.querySelector('.fr-element.fr-view').innerHTML = 'Your note content here';
   ```

5. **Submit Note**
   - Selector: `[data-testid="createNote"]`
   - Action: Click
   - Wait: Modal to close

**Complete Example**:
```python
# Step 1
driver.find_element(By.CSS_SELECTOR, "[data-testid='addNoteToOpportunity']").click()
time.sleep(1)

# Step 2
Select(driver.find_element(By.ID, "noteType")).select_by_visible_text("Phone Out")

# Step 3 (optional)
# Select(driver.find_element(By.ID, "userID")).select_by_visible_text("CA109034:James Larkey")

# Step 4
driver.execute_script("""
    document.querySelector('.fr-element.fr-view').innerHTML =
    'Discussed loan application with client. Client confirmed employment details.';
""")

# Step 5
driver.find_element(By.CSS_SELECTOR, "[data-testid='createNote']").click()
time.sleep(2)
```

---

### Workflow 2: Upload File to Attachments

**Status**: Validated
**Triggers Modal**: No
**Hidden Element**: Yes

**Steps**:

1. **Navigate to Attachments**
   - Selector: `#attachments`
   - Action: Click tab
   - Wait: 2 seconds for section to load

2. **Click Add Button**
   - Selector: `[data-testid="Add"]`
   - Action: Click
   - Note: Activates hidden file input

3. **Send File Path**
   - Selector: `#file`
   - Action: send_keys
   - Note: Input is `display:none` but accessible
   ```python
   file_input.send_keys(absolute_path_to_file)
   ```

**Complete Example**:
```python
# Step 1
driver.find_element(By.ID, "attachments").click()
time.sleep(2)

# Step 2
driver.find_element(By.CSS_SELECTOR, "[data-testid='Add']").click()

# Step 3
file_path = r"C:\Documents\payslip.pdf"
file_input = driver.find_element(By.ID, "file")
file_input.send_keys(file_path)

# File uploads automatically after send_keys
time.sleep(3)  # Wait for upload to complete
```

---

### Workflow 3: Complete Questionnaire

**Status**: Validated
**Triggers Modal**: Yes
**Framework**: AG-Grid

**Steps**:

1. **Navigate to Questionnaires**
   - Selector: `#questionnaires`
   - Action: Click tab
   - Wait: 2 seconds

2. **Click Add Button**
   - Selector: `[data-testid="Add"]`
   - Action: Click
   - Wait: Modal with AG-Grid to appear

3. **Select Questionnaire from Grid**
   - Selector: `.ag-cell`
   - Action: Click cell containing questionnaire name
   - Framework: AG-Grid
   - Available: Home Loan, Asset Finance, Personal Loan, Credit Check

4. **Click Choose Button**
   - Selector: `[data-testid="Choose"]`
   - Action: Click
   - Wait: 3 seconds for form to load

5. **Expand Sections and Fill Form**
   - Action: Expand accordion sections
   - Action: Fill form fields
   - Note: Form structure varies by questionnaire type

**Complete Example**:
```python
# Step 1
driver.find_element(By.ID, "questionnaires").click()
time.sleep(2)

# Step 2
driver.find_element(By.CSS_SELECTOR, "[data-testid='Add']").click()
time.sleep(1)

# Step 3
cells = driver.find_elements(By.CLASS_NAME, "ag-cell")
for cell in cells:
    if "Home Loan - Needs Analysis" in cell.text:
        cell.click()
        break

# Step 4
driver.find_element(By.CSS_SELECTOR, "[data-testid='Choose']").click()
time.sleep(3)

# Step 5
# Expand sections and fill based on questionnaire type
# (Form structure varies)
```

---

## Quick Reference Tables

### Most Common Selectors

| Purpose | Selector | Type | Notes |
|---------|----------|------|-------|
| Add Note | `[data-testid="addNoteToOpportunity"]` | button | Triggers modal |
| Create Note | `[data-testid="createNote"]` | button | Submit in modal |
| Note Content | `.fr-element.fr-view` | rich_text | Froala editor |
| File Upload | `#file` | input | Hidden, use send_keys |
| Add Button (generic) | `[data-testid="Add"]` | button | Context-dependent |
| Choose Button | `[data-testid="Choose"]` | button | Confirm selection |
| AG-Grid Cell | `.ag-cell` | ag_grid | Questionnaire grid |

### Tab Navigation

| Tab | Selector | Destination |
|-----|----------|-------------|
| Details | `#details` | Applicant details |
| Employment | `#employment` | Employment info |
| Incomes | `#incomes` | Income sources |
| Financials | `#financials` | Financial assessment |
| Real Estate Assets | `#realEstateAssets` | Property assets |
| Other Assets | `#otherAssets` | Non-property assets |
| Liabilities | `#liabilities` | Debts and liabilities |
| Attachments | `#attachments` | Document uploads |
| Questionnaires | `#questionnaires` | Questionnaires |
| Compliance | `#newCompliance` | BID & NCCP |

### Selector Priority Guide

**Use in this order** (most reliable first):

1. **data-testid** - Never changes, most reliable
   - Example: `[data-testid="addNoteToOpportunity"]`

2. **ID** - Reliable if not UUID
   - Example: `#lender`, `#propertyType`
   - Avoid: `#btn_xxxxx-xxxx-xxxx` (dynamic UUIDs)

3. **Text content** - For buttons with consistent labels
   - Example: `[text="Living Expense"]`

4. **Class** - Less reliable, can change
   - Example: `.fr-element.fr-view`

5. **XPath** - Last resort only
   - Use only when no other option available

---

## Usage Examples

### Example 1: Complete Financial Assessment

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()

# Navigate to Financials
driver.find_element(By.ID, "financials").click()
time.sleep(2)

# Add Real Estate Asset
driver.find_element(By.ID, "realEstateAssets").click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "[data-testid='Add']").click()
time.sleep(1)

# Fill property details
Select(driver.find_element(By.ID, "propertyType")).select_by_visible_text("Fully Detached House")
Select(driver.find_element(By.ID, "propertyStatus")).select_by_visible_text("Established")
Select(driver.find_element(By.ID, "realEstatePurpose")).select_by_visible_text("Owner Occupied")
Select(driver.find_element(By.ID, "realEstateZoning")).select_by_visible_text("Residential")
Select(driver.find_element(By.ID, "propertyTitleType")).select_by_visible_text("Freehold")

# Add liability
driver.find_element(By.ID, "liabilities").click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "[data-testid='Add']").click()
time.sleep(1)

Select(driver.find_element(By.ID, "name")).select_by_visible_text("Mortgage Loan")
Select(driver.find_element(By.ID, "priority")).select_by_visible_text("First")
Select(driver.find_element(By.ID, "accountRepaymentFrequency")).select_by_visible_text("Monthly")
```

### Example 2: Set Loan Details

```python
# Set lender
Select(driver.find_element(By.ID, "lender")).select_by_visible_text("Commonwealth Bank")

# Set transaction type
Select(driver.find_element(By.ID, "tranxType")).select_by_visible_text("Purchase")

# Set loan type
Select(driver.find_element(By.ID, "transactionType")).select_by_visible_text("Home Loans")

# Set agent
Select(driver.find_element(By.ID, "agent")).select_by_visible_text("James Curtis")

# Set person responsible
Select(driver.find_element(By.ID, "personResponsible")).select_by_visible_text("James Larkey")

# Set settlement officer
Select(driver.find_element(By.ID, "settlementOfficer")).select_by_visible_text("James Larkey")
```

### Example 3: Add Multiple Notes

```python
notes = [
    ("Phone Out", "Called client to confirm employment details"),
    ("Email Out", "Sent loan documents for review"),
    ("Phone In", "Client called with questions about LMI")
]

for note_type, note_content in notes:
    # Click add note
    driver.find_element(By.CSS_SELECTOR, "[data-testid='addNoteToOpportunity']").click()
    time.sleep(1)

    # Select type
    Select(driver.find_element(By.ID, "noteType")).select_by_visible_text(note_type)

    # Add content
    driver.execute_script(f"""
        document.querySelector('.fr-element.fr-view').innerHTML = '{note_content}';
    """)

    # Submit
    driver.find_element(By.CSS_SELECTOR, "[data-testid='createNote']").click()
    time.sleep(2)
```

### Example 4: Upload Multiple Documents

```python
documents = [
    r"C:\Documents\payslip1.pdf",
    r"C:\Documents\payslip2.pdf",
    r"C:\Documents\bank_statement.pdf",
    r"C:\Documents\id_document.pdf"
]

# Navigate to attachments
driver.find_element(By.ID, "attachments").click()
time.sleep(2)

for doc_path in documents:
    driver.find_element(By.CSS_SELECTOR, "[data-testid='Add']").click()
    file_input = driver.find_element(By.ID, "file")
    file_input.send_keys(doc_path)
    time.sleep(3)  # Wait for upload
```

---

## Common Patterns and Tips

### Modal-Based Architecture

**Pattern**: Many elements don't exist until triggered

```python
# Element doesn't exist yet
element = driver.find_element(By.ID, "someField")  # Will fail

# Correct approach:
trigger_button.click()
time.sleep(1)  # Wait for modal
element = driver.find_element(By.ID, "someField")  # Now exists
```

**Elements that trigger modals**:
- Add Note button
- Add buttons in Financials sections
- Questionnaire Add button

### Hidden Elements

**Pattern**: Element exists in DOM but `display:none`

```python
# File upload is hidden but accessible
file_input = driver.find_element(By.ID, "file")
# Don't try to click - use send_keys directly
file_input.send_keys(file_path)
```

### Froala Rich Text Editor

**Pattern**: Can't use send_keys, must use JavaScript

```python
# Wrong:
editor.send_keys("text")  # Won't work

# Correct:
driver.execute_script("""
    document.querySelector('.fr-element.fr-view').innerHTML = 'text';
""")
```

### AG-Grid Selection

**Pattern**: Find cells, match by text content

```python
cells = driver.find_elements(By.CLASS_NAME, "ag-cell")
for cell in cells:
    if target_text in cell.text:
        cell.click()
        break
```

### Dynamic UUIDs

**Pattern**: Avoid selectors with UUIDs that change

```python
# Bad (UUID changes):
btn = driver.find_element(By.ID, "btn_7c86c163-cef1-4061-b70a-0c2f7c4beda3")

# Good (stable):
btn = driver.find_element(By.CSS_SELECTOR, "[data-testid='Add Loan']")
```

---

## PowerShell Usage Fix

### Error
```
use_enhanced_agent.py : The term 'use_enhanced_agent.py' is not recognized
```

### Solutions

```powershell
# Option 1: Add .\ prefix
.\demo_agent.py

# Option 2: Use python command
python demo_agent.py

# Option 3: Explicit python with path
python .\use_enhanced_agent.py
```

**Why**: PowerShell doesn't execute scripts from current directory by default.

---

## Python API Access

### Load the Agent

```python
from use_enhanced_agent import load_enhanced_agent

# Load all 74 elements + workflows
agent = load_enhanced_agent()

print(f"Total elements: {len(agent.elements)}")
print(f"Sections: {len(agent.sections)}")
print(f"Workflows: {len(agent.workflows)}")
```

### Access Elements

```python
# Find element by name
lender = [e for e in agent.elements.values() if e.name == 'lender'][0]
print(f"Lender has {len(lender.options)} options")
print(lender.options[:5])  # First 5 lenders

# Get all elements in a section
financials = agent.get_section_elements("Financials")
print(f"Financials has {len(financials)} elements")

# Get all dropdowns
dropdowns = [e for e in agent.elements.values() if e.options]
for dd in dropdowns:
    print(f"{dd.name}: {len(dd.options)} options")
```

### Validate Values

```python
# Check if lender is valid
lender_elem = [e for e in agent.elements.values() if e.name == 'lender'][0]
user_input = "Commonwealth Bank"

if user_input in lender_elem.options:
    print("Valid lender!")
else:
    print(f"Invalid. Choose from: {lender_elem.options}")
```

---

**This reference contains complete knowledge of the Connective CRM system extracted from 74 elements across 8 sections!**
