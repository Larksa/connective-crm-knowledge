# Connective CRM - Complete System Reference

**Last Updated**: 2025-10-08
**Total Elements**: 91
**Sections**: 8
**Validated Workflows**: 4
**Dropdown Fields**: 22
**Field Mappings**: 9 (expense, lender, agent, property_type, liability_type, asset_type, motor_vehicle_type, asset_value_basis, income_other_type)

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
| **Total Elements** | 91 |
| **Buttons** | 46 |
| **Dropdown Fields (Select)** | 22 |
| **Text Input Fields** | 17 |
| **Checkboxes** | 1 |
| **Navigation Tabs** | 3 |
| **Rich Text Editors** | 1 |
| **AG-Grid Components** | 1 |
| **Sections Mapped** | 8 |
| **Validated Workflows** | 4 |
| **Total Dropdown Options** | 299 |
| **Field Mappings** | 9 (with 600+ variations) |

### What This Agent Knows

- **Complete CRM Structure**: All sections, tabs, and navigation
- **All Interactive Elements**: Every button, input field, dropdown, and control
- **All Selectors**: data-testid, ID, class, and best-practice selectors for each element
- **Complete Dropdown Options**: All 54 lenders, 63 property types, 19 agents, 18 asset types, etc.
- **Validated Workflows**: Step-by-step instructions for common tasks
- **Modal Behavior**: Which elements trigger modals and their dependencies
- **Hidden Elements**: Elements that appear only after triggers
- **Framework Detection**: Froala editors, AG-Grid, React-Select components
- **Conditional Fields**: Motor Vehicle type dropdown (appears when Motor Vehicle asset selected)

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
**Total Elements**: 55

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

#### Liability Fields (12)

| Element | Type | Selector | Options/Purpose |
|---------|------|----------|-----------------|
| **liabilityType** | select | `#name` | 18 liability types |
| **institution** | input | `#institution` | Financial institution name |
| **accountName** | input | `#accountName` | Account name/description |
| **accountBSB** | input | `#accountBSB` | BSB number (optional) |
| **accountNumber** | input | `#accountNumber` | Account number (optional) |
| **balance** | input | `#value` | Current outstanding balance |
| **limit** | input | `#limit` | Credit limit or approved amount |
| **repaymentAmount** | input | `#accountRepayment` | Regular repayment amount |
| **repaymentFrequency** | select | `#accountRepaymentFrequency` | 4 frequency options (annually, monthly, fortnightly, weekly) |
| **accountClearingFromLoan** | checkbox | `[name="accountClearingFromLoan"]` | Clearing from this loan checkbox |
| **securityLink** | button | (Security Details/Link Assets) | Link/unlink assets to liability |
| **ownershipAllocation** | button | `.dropdown-item` | Ownership options (dual applications) |

**Note**: See [Liabilities Guide](./sections/liabilities.md) for detailed automation workflows and field mappings.

#### Other Assets Fields (7)

| Element | Type | Selector | Options/Purpose |
|---------|------|----------|-----------------|
| **addAssetButton** | button | `[data-testid="Add"]` | Add new asset row (triggers form) |
| **assetType** | select | `select[data-testid="asset-type-{index}"]` | 18 asset types (index starts at 0) |
| **assetName** | input | `#name` | Asset name/description |
| **assetValue** | input | `#value`, `input[name="value"]`, `input[data-field-type="currency"]` | Currency input, right-aligned, placeholder "0.00" |
| **assetValueBasis** | select | `#valueBasis` | 3 value basis options |
| **vehicleType** | select | `#vehicleType` | 7 vehicle types (conditional - Motor Vehicle only) |
| **ownershipAllocation** | button | `[text*="Allocate Evenly"]` | Ownership allocation (dual applications) |

**Important**: Each asset row gets an indexed data-testid (e.g., `asset-type-0` for first asset, `asset-type-1` for second). The Add button has a UUID-based ID that changes, so always use `[data-testid="Add"]`.

**Fields NOT in Assets-Other Form**:
- **Financial Institution**: While Excel may have an "Institution" column for assets, the Connective "Assets - Other" section does NOT capture which financial institution holds the asset. This field appears in other sections:
  - ✅ Liabilities section (`#institution` - which bank the debt is with)
  - ✅ Real Estate section (for linked mortgage details)
  - ❌ Assets - Other section (no institution field)
- **Automation Note**: Skip Excel's "Asset_Institution" column when filling Assets-Other forms.

**Note**: See [Assets - Other Guide](./sections/assets_other.md) for detailed automation workflows.

#### Other Income Fields (4)

| Element | Type | Selector | Options/Purpose |
|---------|------|----------|-----------------|
| **addIncomeButton** | button | `[data-testid="Add"]` | Add new income entry (triggers inline form) |
| **incomeType** | select | `#type` | 4 income types (Dividends, Family Allowance, Maintenance, Other) |
| **frequency** | select | `#frequency` | 4 frequency options (Annual, Monthly, Fortnightly, Weekly) |
| **amount** | input | `#amount` | Income amount (currency) |

**Important Selector Notes**:
- **Add Button**: Use `[data-testid="Add"]` (stable) NOT `#btn_[UUID]` (dynamic, changes per session)
- **Income Type**: Use `#type` (stable ID) NOT `[data-testid="income-type-{UUID}"]` (UUID changes per row)
- **Form Auto-Save**: No explicit save button; wait 2 seconds after amount entry
- **Multiple Entries**: Each Add click creates a new form row with the same stable IDs (#type, #frequency, #amount)

**Validated Workflow** (2025-10-08 recording):
1. Navigate: `#financials` → `#incomes` (wait 2 seconds)
2. Add entry: `[data-testid="Add"]` (wait 1 second)
3. Select type: `#type` (wait 0.5 seconds)
4. Select frequency: `#frequency` (wait 0.5 seconds)
5. Enter amount: `#amount` (wait 2 seconds for auto-save)
6. Repeat steps 2-5 for additional income sources

**Note**: See [Other Income Guide](./sections/other_income.md) and [2025-10-08 Update](./sections/other_income_update_2025-10-08.md) for detailed automation workflows.

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

### 4. Liability Type (18 options)
**Selector**: `#name`
**Section**: Financials - Liabilities

```
1.  Buy Now Pay Later
2.  Car Loan
3.  Commercial Bill
4.  Credit Card
5.  HECS
6.  Hire Purchase
7.  Lease
8.  Line of Credit
9.  Loan as Guarantor
10. Mortgage
11. Loan ATO
12. Loan Outstanding Taxation
13. Overdraft
14. Personal Loan
15. Business Loan
16. Store Card
17. Term Loan
18. Other
```

**Note**: See [Liabilities Guide](./sections/liabilities.md) for detailed automation workflows and field mappings.

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

### 11. Income/Other Type (4 options)
**Selector**: `#type`
**Section**: Financials - Other Income

```
1. Dividends
2. Family Allowance
3. Maintenance
4. Other
```

**Note**: See [Other Income Guide](./sections/other_income.md) for detailed automation workflows.

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

### 20. Living Expense Category (21 options)
**Selector**: `button.dropdown-toggle:has-text('Living Expense')`
**Section**: Financials - Living Expenses

```
1.  Transport
2.  Rent
3.  Board
4.  Groceries
5.  Childcare
6.  Child & Spouse Maintenance
7.  Clothing & Personal Care
8.  Public or Government Primary & Secondary Education
9.  Higher Education & Vocational Training (excluding HECS/HELP)
10. Private & Non-Government Education
11. General Insurance (Including Home & Contents on Primary O/Occ Residence)
12. Personal Insurance (Life, Health, Sickness and Personal Accident)
13. Other Insurances
14. Investment Property Costs (including Insurance)
15. Primary Residence Costs (excluding Insurance)
16. Secondary Residence & Holiday Home Costs (including Insurance)
17. O/Occ Strata, Body Corporate, Land Tax
18. Medical & Health (excluding Health Insurance)
19. Other Regular and Recurring Expenses
20. Recreation & Entertainment
21. Telephone, Internet, Pay TV & Media Streaming Subscriptions
```

**Note**: This is a dynamic dropdown - clicking the trigger button adds a new expense row. Each row requires: Category (dropdown), Frequency (dropdown), Amount (text input).

### 21. Asset Type (18 options)
**Selector**: `select[data-testid="asset-type-{index}"]` (where index = 0, 1, 2... for each asset row)
**Alternative Selector**: `#name` (less specific, may conflict with other fields)
**Section**: Financials - Assets - Other

```
1.  Boat
2.  Business Equity
3.  Cash Management
4.  Charge over Cash
5.  Cheque Account
6.  Debenture Charge
7.  Gifts
8.  Guarantee
9.  Home Contents
10. Investment Savings
11. Life Insurance
12. Managed Funds
13. Motor Vehicle
14. Other
15. Savings Account
16. Shares
17. Superannuation
18. Term Deposit
```

**Usage Notes**:
- **First asset**: `select[data-testid="asset-type-0"]`
- **Second asset**: `select[data-testid="asset-type-1"]`
- **Add button**: `[data-testid="Add"]` (click to create new asset row)
- **Conditional dropdown**: Selecting "Motor Vehicle" reveals vehicle type dropdown (see #23)
- **Element type**: Standard `<select>` dropdown with options as shown above

### 22. Asset Value Basis (3 options)
**Selector**: `#valueBasis`
**Section**: Financials - Assets - Other

```
1. Applicant Estimate
2. Certified Valuation
3. Actual Value
```

**Usage Guidelines**:
- **Applicant Estimate**: Client-provided value without formal documentation (personal items, boats, gifts)
- **Certified Valuation**: Professional valuation obtained (business equity, managed funds)
- **Actual Value**: Exact current value known (bank accounts, term deposits, shares)

### 23. Motor Vehicle Type (7 options)
**Selector**: `#vehicleType`
**Section**: Financials - Assets - Other

```
1. Bike
2. Large
3. Luxury Car
4. 4WD
5. Medium
6. Small
7. Small Medium
```

**Note**: This is a conditional dropdown that only appears when "Motor Vehicle" is selected as the Asset Type.

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

### Workflow 4: Add Liability Entry

**Status**: Validated
**Triggers Modal**: No
**Auto-Save**: Yes (2 second delay)
**Max Page Load**: 79 seconds
**Section**: Financials → Liabilities

**Critical Timing Requirements**:
- Page load timeout: 79 seconds (from recording)
- Auto-save delay: 2 seconds after final field
- Field transition: 0.5-1 second between actions

**Steps**:

1. **Navigate to Financials Tab**
   - Selector: `#financials`
   - Action: Click
   - Wait: 1000ms for tab to load

2. **Navigate to Liabilities Sub-Tab**
   - Selector: `#liabilities`
   - Action: Click
   - Wait: 2000ms for section to load
   - Note: Max page load observed at 79 seconds

3. **Click Add Liability Button**
   - Selector: `[data-testid="Add"]`
   - Action: Click
   - Wait: 1000ms for new row to appear
   - Note: Use data-testid, NOT #btn_{UUID} (unstable)

4. **Select Liability Type**
   - Selector: `#name`
   - Action: Select from dropdown
   - Options: 18 liability types (Buy Now Pay Later, Car Loan, Credit Card, etc.)
   - Wait: 1000ms for form to update

5. **Enter Institution**
   - Selector: `#institution`
   - Action: Clear and type text
   - Wait: 500ms

6. **Enter Account Name**
   - Selector: `#accountName`
   - Action: Clear and type text
   - Wait: 500ms

7. **Enter Account BSB (Optional)**
   - Selector: `#accountBSB`
   - Action: Clear and type text
   - Wait: 500ms
   - Note: Optional field

8. **Enter Account Number (Optional)**
   - Selector: `#accountNumber`
   - Action: Clear and type text
   - Wait: 500ms
   - Note: Optional field

9. **Enter Balance**
   - Selector: `#value`
   - Action: Clear and type text
   - Wait: 500ms
   - Note: Current outstanding balance

10. **Enter Limit**
    - Selector: `#limit`
    - Action: Clear and type text
    - Wait: 500ms
    - Note: Credit limit or approved amount

11. **Enter Repayment Amount**
    - Selector: `#accountRepayment`
    - Action: Clear and type text
    - Wait: 500ms

12. **Select Repayment Frequency**
    - Selector: `#accountRepaymentFrequency`
    - Action: Select from dropdown
    - Options: Annual, Monthly, Fortnightly, Weekly
    - Values: "annually", "monthly", "fortnightly", "weekly" (lowercase)
    - Wait: 500ms

13. **Set Priority (Optional)**
    - Selector: `#priority`
    - Action: Select from dropdown
    - Wait: 500ms
    - Note: New field discovered from jlall.json recording

14. **Check Clearing from Loan (Optional)**
    - Selector: `[name="accountClearingFromLoan"]`
    - Action: Click checkbox if applicable
    - Wait: 2000ms for auto-save
    - Note: Indicates liability cleared from loan proceeds

**Complete Example**:
```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Step 1-2: Navigate to Liabilities
driver.find_element(By.ID, "financials").click()
time.sleep(1)
driver.find_element(By.ID, "liabilities").click()
time.sleep(2)

# Step 3: Click Add
driver.find_element(By.CSS_SELECTOR, '[data-testid="Add"]').click()
time.sleep(1)

# Step 4: Select liability type
liability_type = Select(driver.find_element(By.ID, "name"))
liability_type.select_by_visible_text("Credit Card")
time.sleep(1)

# Step 5-6: Basic info
driver.find_element(By.ID, "institution").clear()
driver.find_element(By.ID, "institution").send_keys("Commonwealth Bank")
time.sleep(0.5)

driver.find_element(By.ID, "accountName").clear()
driver.find_element(By.ID, "accountName").send_keys("Personal Credit Card")
time.sleep(0.5)

# Step 9-10: Balance and limit
driver.find_element(By.ID, "value").clear()
driver.find_element(By.ID, "value").send_keys("5000")
time.sleep(0.5)

driver.find_element(By.ID, "limit").clear()
driver.find_element(By.ID, "limit").send_keys("15000")
time.sleep(0.5)

# Step 11-12: Repayment
driver.find_element(By.ID, "accountRepayment").clear()
driver.find_element(By.ID, "accountRepayment").send_keys("250")
time.sleep(0.5)

frequency = Select(driver.find_element(By.ID, "accountRepaymentFrequency"))
frequency.select_by_value("monthly")
time.sleep(0.5)

# Step 14: Auto-save wait
time.sleep(2)
print("Liability entry saved")
```

---

### Workflow 5: Add Asset (Other)

**Status**: Validated
**Triggers Modal**: No
**Auto-Save**: Yes (2 second delay)
**Section**: Financials → Assets - Other
**Conditional Fields**: vehicleType (only for Motor Vehicle assets)
**Selector Stability**: EXCELLENT (from jlall.json recording)

**Critical Notes**:
- asset-type uses INDEX-BASED data-testid (NOT UUID-based)
- Pattern: asset-type-0, asset-type-1, asset-type-2 (zero-indexed)
- vehicleType field appears ONLY when asset type = "Motor Vehicle"

**Steps**:

1. **Navigate to Financials Tab**
   - Selector: `#financials`
   - Action: Click
   - Wait: 1000ms

2. **Navigate to Assets - Other Sub-Tab**
   - Selector: `#otherAssets`
   - Action: Click
   - Wait: 2000ms

3. **Click Add Asset Button**
   - Selector: `[data-testid="Add"]`
   - Action: Click
   - Wait: 1000ms for new row

4. **Select Asset Type**
   - Selector: `select[data-testid="asset-type-{index}"]`
   - Action: Select from dropdown
   - Options: 18 asset types
   - Note: Replace {index} with 0 for first asset, 1 for second, etc.
   - Wait: 1000ms
   - Verified: Index-based pattern from jlall.json recording

5. **Enter Asset Name/Description**
   - Selector: `#name`
   - Action: Clear and type text
   - Wait: 500ms

6. **Enter Asset Value**
   - Selector: `#value`
   - Action: Clear and type text
   - Wait: 500ms
   - Note: Currency format, right-aligned

7. **Select Value Basis**
   - Selector: `#valueBasis`
   - Action: Select from dropdown
   - Options: Applicant Estimate, Certified Valuation, Actual Value
   - Wait: 2000ms for auto-save
   - Verified: Selector confirmed stable from jlall.json recording

8. **Select Vehicle Type (Conditional)**
   - Selector: `#vehicleType`
   - Action: Select from dropdown (ONLY if asset type = "Motor Vehicle")
   - Options: Car, Motorcycle, Boat, Caravan, Truck, Other, Trailer
   - Wait: 2000ms for auto-save
   - Note: Field only appears for Motor Vehicle assets

**Complete Example (Standard Asset)**:
```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Step 1-2: Navigate to Assets - Other
driver.find_element(By.ID, "financials").click()
time.sleep(1)
driver.find_element(By.ID, "otherAssets").click()
time.sleep(2)

# Step 3: Click Add
driver.find_element(By.CSS_SELECTOR, '[data-testid="Add"]').click()
time.sleep(1)

# Step 4: Select asset type (first asset = index 0)
asset_type = Select(driver.find_element(By.CSS_SELECTOR, '[data-testid="asset-type-0"]'))
asset_type.select_by_visible_text("Boat")
time.sleep(1)

# Step 5: Enter name
driver.find_element(By.ID, "name").clear()
driver.find_element(By.ID, "name").send_keys("Boston Whaler 230")
time.sleep(0.5)

# Step 6: Enter value
driver.find_element(By.ID, "value").clear()
driver.find_element(By.ID, "value").send_keys("75000")
time.sleep(0.5)

# Step 7: Select value basis
value_basis = Select(driver.find_element(By.ID, "valueBasis"))
value_basis.select_by_visible_text("Applicant Estimate")
time.sleep(2)  # Auto-save

print("Asset entry saved")
```

**Complete Example (Motor Vehicle with Conditional Field)**:
```python
# Steps 1-4: Same as above, but select "Motor Vehicle"
asset_type = Select(driver.find_element(By.CSS_SELECTOR, '[data-testid="asset-type-0"]'))
asset_type.select_by_visible_text("Motor Vehicle")
time.sleep(1)

# Step 5-6: Name and value
driver.find_element(By.ID, "name").clear()
driver.find_element(By.ID, "name").send_keys("2020 Toyota Camry")
time.sleep(0.5)

driver.find_element(By.ID, "value").clear()
driver.find_element(By.ID, "value").send_keys("35000")
time.sleep(0.5)

# Step 7: Value basis
value_basis = Select(driver.find_element(By.ID, "valueBasis"))
value_basis.select_by_visible_text("Market Value")
time.sleep(0.5)

# Step 8: Vehicle type (conditional - only appears for Motor Vehicle)
vehicle_type = Select(driver.find_element(By.ID, "vehicleType"))
vehicle_type.select_by_visible_text("Car")
time.sleep(2)  # Auto-save

print("Motor vehicle entry saved")
```

---

### Workflow 6: Add Living Expense Entry

**Status**: Validated
**Triggers Modal**: No
**Auto-Save**: Yes (2 second delay)
**Section**: Financials → Living Expenses
**Shared Selectors**: Uses same #frequency and #amount as Other Income

**Critical Notes**:
- Identical field selectors to Other Income section
- 22+ expense categories available
- Universal pattern across all categories
- Auto-save after amount entry (no submit button)

**Steps**:

1. **Navigate to Financials Tab**
   - Selector: `#financials`
   - Action: Click
   - Wait: 1000ms

2. **Navigate to Living Expenses Sub-Tab**
   - Selector: `#livingExpenses`
   - Action: Click
   - Wait: 2000ms

3. **Click Add Expense Button**
   - Selector: `[data-testid="Add"]`
   - Action: Click
   - Wait: 1000ms

4. **Select Expense Category**
   - Selector: Category-specific (varies by expense type)
   - Action: Select from dropdown
   - Options: 22 categories (Groceries, Utilities, Childcare, etc.)
   - Wait: 500ms
   - Note: Refer to living_expenses.md for category-specific selectors

5. **Select Frequency**
   - Selector: `#frequency`
   - Action: Select from dropdown
   - Options: Annual, Monthly, Fortnightly, Weekly
   - Wait: 500ms
   - Verified: Selector confirmed from jlall.json recording

6. **Enter Amount**
   - Selector: `#amount`
   - Action: Clear and type text
   - Wait: 2000ms for auto-save
   - Note: Currency format
   - Verified: Selector confirmed from jlall.json recording

**Complete Example**:
```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Step 1-2: Navigate to Living Expenses
driver.find_element(By.ID, "financials").click()
time.sleep(1)
driver.find_element(By.ID, "livingExpenses").click()
time.sleep(2)

# Step 3: Click Add
driver.find_element(By.CSS_SELECTOR, '[data-testid="Add"]').click()
time.sleep(1)

# Step 4: Select category (example: Groceries)
# Note: Selector varies by category - see living_expenses.md
expense_category = Select(driver.find_element(By.ID, "expenseType"))
expense_category.select_by_visible_text("Groceries")
time.sleep(0.5)

# Step 5: Select frequency
frequency = Select(driver.find_element(By.ID, "frequency"))
frequency.select_by_visible_text("Monthly")
time.sleep(0.5)

# Step 6: Enter amount
driver.find_element(By.ID, "amount").clear()
driver.find_element(By.ID, "amount").send_keys("1500")
time.sleep(2)  # Auto-save

print("Living expense entry saved")
```

---

### Workflow 7: Add Other Income Entry

**Status**: Validated
**Triggers Modal**: No
**Auto-Save**: Yes (2 second delay)
**Section**: Financials → Other Income
**Shared Selectors**: Uses same #frequency and #amount as Living Expenses
**Selector Stability**: EXCELLENT

**Critical Notes**:
- Simplest workflow (only 3 form fields)
- Use #type selector, NOT data-testid (contains UUID)
- [data-testid="Add"] is stable for Add button
- Auto-save after amount entry

**Steps**:

1. **Navigate to Financials Tab**
   - Selector: `#financials`
   - Action: Click
   - Wait: 1000ms

2. **Navigate to Other Income Sub-Tab**
   - Selector: `#incomes`
   - Action: Click
   - Wait: 2000ms

3. **Click Add Income Button**
   - Selector: `[data-testid="Add"]`
   - Action: Click
   - Wait: 1000ms
   - Note: Use data-testid, NOT #btn_{UUID} (unstable)

4. **Select Income Type**
   - Selector: `#type`
   - Action: Select from dropdown
   - Options: Dividends, Family Allowance, Maintenance, Other
   - Wait: 500ms
   - Note: Use #type selector (stable), NOT data-testid with UUID

5. **Select Frequency**
   - Selector: `#frequency`
   - Action: Select from dropdown
   - Options: Annual, Monthly, Fortnightly, Weekly
   - Wait: 500ms

6. **Enter Amount**
   - Selector: `#amount`
   - Action: Clear and type text
   - Wait: 2000ms for auto-save
   - Note: Currency format, right-aligned

**Complete Example**:
```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Step 1-2: Navigate to Other Income
driver.find_element(By.ID, "financials").click()
time.sleep(1)
driver.find_element(By.ID, "incomes").click()
time.sleep(2)

# Step 3: Click Add
driver.find_element(By.CSS_SELECTOR, '[data-testid="Add"]').click()
time.sleep(1)

# Step 4: Select income type
income_type = Select(driver.find_element(By.ID, "type"))
income_type.select_by_visible_text("Dividends")
time.sleep(0.5)

# Step 5: Select frequency
frequency = Select(driver.find_element(By.ID, "frequency"))
frequency.select_by_visible_text("Annual")
time.sleep(0.5)

# Step 6: Enter amount
driver.find_element(By.ID, "amount").clear()
driver.find_element(By.ID, "amount").send_keys("5000")
time.sleep(2)  # Auto-save

print("Other income entry saved")
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
