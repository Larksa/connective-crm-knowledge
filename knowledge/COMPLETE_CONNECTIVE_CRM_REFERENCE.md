# Connective CRM - Complete System Reference

**Last Updated**: 2025-10-10
**Total Elements**: 141 (91 original + 50 Calculations)
**Sections**: 9
**Validated Workflows**: 10
**Dropdown Fields**: 22
**Field Mappings**: 9 (expense, lender, agent, property_type, liability_type, asset_type, motor_vehicle_type, asset_value_basis, income_other_type)

---

## Table of Contents

1. [Executive Summary](#executive-summary)
2. [Complete Element Directory by Section](#complete-element-directory-by-section)
   - [Attachments Section](#attachments-section)
   - [BID & NCCP Section](#bid--nccp-section)
   - [Calculations Section](#calculations-section)
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
| **Total Elements** | 141 |
| **Buttons** | 51 (46 + 5 Calculations) |
| **Dropdown Fields (Select)** | 27 (22 + 5 Calculations) |
| **Text Input Fields** | 56 (17 + 39 Calculations) |
| **Checkboxes** | 4 (1 + 3 Calculations) |
| **Navigation Tabs** | 4 (3 + 1 Calculations) |
| **Rich Text Editors** | 1 |
| **AG-Grid Components** | 1 |
| **Sections Mapped** | 9 |
| **Validated Workflows** | 9 |
| **Total Dropdown Options** | 330 (299 + 31 Calculations) |
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

### Login and Dashboard Section

**Purpose**: Authentication, navigation, and main dashboard controls
**Total Elements**: 32 (16 original + 16 login/navigation)

**Related Workflow**: [Workflow 10: Login and Dashboard Navigation](./LOGIN_AND_DASHBOARD_WORKFLOW.md)

#### Authentication Fields (3)

| Element | Selector | Type | Purpose | Pattern | Notes |
|---------|----------|------|---------|---------|-------|
| **logname** | `#logname` | text | Username/email | Excel to Paste | Login form |
| **password** | `#password` | password | Password | Excel to Paste | Login form |
| **submit_login** | `button[type="submit"]` | button | Submit login | Navigation Click | Login form submit |

**Login URL**: `https://login.connective.com.au/`
**Post-Login URL**: `https://apps.connective.com.au/`
**Email Verification**: 30-60 second wait on first login, cookies skip on subsequent logins

#### CRM Navigation Elements (4)

| Element | Selector | Type | Purpose | Notes |
|---------|----------|------|---------|-------|
| **appTile_CRM** | `#appTile_CRM` | button | Navigate to CRM | Opens new tab |
| **universal_search** | `input.form-control[placeholder="Search"]` | text | Universal search bar | Keyboard typing required for autocomplete |
| **search_result** | `a.list-group-item` | link | Search result item | Click to open record |
| **crm_tab** | (tab context) | tab | CRM browser tab | Switch after CRM tile click |

**CRM URL Pattern**: `https://crm.connective.com.au/#/`
**Search Capabilities**: Clients, Leads, Contacts, Opportunities (universal)

#### Dashboard Action Buttons (8)

| Element | Selector | Label | Opens | Notes |
|---------|----------|-------|-------|-------|
| **btn_Opportunity** | `button.dropdown-toggle:has-text('Opportunity')` | Opportunity | Dropdown menu | Bootstrap dropdown pattern |
| **btn_Person** | `button:has-text('Person')` | Person | Add Person modal | Dashboard action |
| **btn_Task** | `button:has-text('Task')` | Task | Add Task modal | Dashboard action |
| **btn_Doc_Request** | `button:has-text('Doc Request')` | Doc Request | Document Request form | Dashboard action |
| **btn_Funding_Position** | `button:has-text('Funding Position')` | Funding Position | Funding form | Dashboard action |
| **btn_Borrowing_Capacity** | `button:has-text('Borrowing Capacity')` | Borrowing Capacity | Calculator | Dashboard action |
| **btn_Product_Comparison** | `button:has-text('Product Comparison')` | Product Comparison | Comparison tool | Dashboard action |
| **btn_Home_Loans** | `[text="Home Loans"]` | Home Loans | Opportunity form | Legacy selector |

**Dashboard Action Pattern**: All buttons use consistent `button:has-text('{action}')` selector structure

#### Opportunity Type Dropdown (4 options)

**Triggered By**: Clicking Opportunity button
**Selector**: `button.dropdown-item` within `.dropdown-menu.show`
**Pattern**: Bootstrap dropdown

```
1. Home Loans ✅ (validated)
2. Commercial Loans
3. Asset Finance
4. Business Loans
```

**Fuzzy Matching**: Enabled with 80% threshold (e.g., "Home Loan" → "Home Loans")

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

### Calculations Section

**Purpose**: Borrowing capacity calculations and financial assessments
**Total Elements**: 50

#### Navigation

| Element | Type | Selector | Purpose |
|---------|------|----------|---------|
| **calculations_tab** | tab | `#calculations` | Navigate to calculations section |
| **add_dropdown** | button | `button.dropdown-toggle.btn.btn-light.btn-sm` | Add new calculation |
| **borrowing_capacity_option** | button | `button.dropdown-item:nth-of-type(2)` | Select Borrowing Capacity calc |
| **proceed_button** | button | `.btn.btn-outline-primary` | Confirm calculation start |
| **calculate_button** | button | `[data-testid="calculate"]` | Execute calculation |

#### Basic Settings Fields (7)

| Element | Type | Selector | Purpose | Notes |
|---------|------|----------|---------|-------|
| **loanTerm** | input | `#loanTerm` | Loan term (years) | Number input |
| **realEstatePurpose** | select | `#realEstatePurpose` | Owner Occupied/Investment | 2 options |
| **lvrText** | input | `#lvrText` | LVR percentage | Number, may need double-click |
| **hasProfessionalPack** | checkbox | `input[name="hasProfessionalPack"]` | Professional pack flag | Dynamic UUID in ID |
| **loanRequested** | input | `#loanRequested` | Loan amount | Currency input |
| **dependants** | input | `#dependants` | Number of dependants | Number input |
| **multipleHouseholds** | checkbox | `input[name="multipleHouseholds"]` | Multiple households flag | Dynamic UUID in ID |

#### Income/Expense Modal Fields

| Element | Type | Selector | Options/Purpose | Notes |
|---------|------|----------|-----------------|-------|
| **type** | select | `#type` | Income or Expense type | Context-dependent |
| **frequency** | select | `#frequency` | Annual/Monthly/Fortnightly/Weekly | 4 options |
| **amountText** | input | `#amountText` | Amount | Currency input |
| **householdId** | select | `#householdId` | Select household | Dynamic options |

#### Self-Employed Specific Fields (18+)

**Operating Structure**
- Selector: `#operatingStructure`
- Options: Sole Trader/Partnership, Company

**Financial Year**
- Selector: `#recentFY`
- Options: FY25, FY24, FY23, FY22

**Current/Previous FY Field Pairs** (all use `#[fieldName]Cfy` and `#[fieldName]Pfy`):
- `currentFYAmount` / `previousFYAmount` - Net Profit Before Tax
- `depreciationCfy` / `depreciationPfy` - Depreciation
- `amortisationCfy` / `amortisationPfy` - Amortisation
- `interestCfy` / `interestPfy` - Interest
- `superannuationCfy` / `superannuationPfy` - Extra Super Contributions
- `hirePurchaseCfy` / `hirePurchasePfy` - Hire Purchase
- `leaseCfy` / `leasePfy` - Lease
- `nonRecurringIncomesCfy` / `nonRecurringIncomesPfy` - Non-Recurring Income
- `nonRecurringExpensesCfy` / `nonRecurringExpensesPfy` - Non-Recurring Expense

**Note**: Self-employed fields only appear when "Self Employed" income type is selected

#### Liability/Expense Fields

| Element | Selector | Purpose | Notes |
|---------|----------|---------|-------|
| **creditLimitText** | `#creditLimitText` | Credit card limit | Credit Card type only |
| **balance** | `#balance` | Liability balance | Currency input |
| **term** | `#term` | Remaining term (months) | Number input |
| **interestRate** | `#interestRate` | Interest rate | Number input |
| **loanTerm** | `#loanTerm` | Loan term | Number input |
| **taxBenefit** | `#taxBenefit` | Tax benefit percentage | May need double-click |

#### Asset/Property Fields

| Element | Selector | Purpose | Notes |
|---------|----------|---------|-------|
| **value** | `#value` | Property value | Currency input |
| **realEstateRentalIncome** | `#realEstateRentalIncome` | Rental income amount | Investment properties |
| **realEstateRentalIncomeFrequency** | `#realEstateRentalIncomeFrequency` | Rental frequency | 4 options |
| **investmentCost** | `#investmentCost` | Investment costs | Currency input |
| **investmentCostFrequency** | `#investmentCostFrequency` | Cost frequency | 4 options |
| **ownership** | `#ownership` | Ownership percentage | Number input |
| **realEstatePurpose** | `input[name="realEstatePurpose"][value="Investment"]` | Purpose radio | Dynamic UUID in ID |
| **realEstateToBePurchased** | `input[name="realEstateToBePurchased"]` | To be purchased | Dynamic UUID in ID |
| **realEstateUseAsSecurity** | `input[name="realEstateUseAsSecurity"]` | Use as security | Dynamic UUID in ID |

#### Action Buttons

| Element | Selector | Purpose | Notes |
|---------|----------|---------|-------|
| **btnAddIncome** | `[data-testid^="btnAddIncome_"]` | Add income entry | UUID in testid |
| **btnAddExpense** | `[data-testid="btnAddExpense"]` | Add expense entry | Stable testid |
| **seIncomeWizard** | `[data-testid="seIncomeWizard"]` | Self-employed wizard | Opens SE fields |
| **calculate** | `[data-testid="calculate"]` | Calculate result | Final step |

#### Special Behaviors

**1. Confirmation Modal After Add**
- When clicking Add Income or Add Expense, a confirmation modal appears
- Selector: `button:contains("Okay")` or `button:contains("OK")`
- Handle with try/except as it may not always appear

**2. Percent Field Quirk**
- Fields like `#taxBenefit` and `#ownership` may require double-clicking
- Zero placeholder may remain visible until properly focused
- Workaround: Click twice with small delay between clicks

**3. Dynamic Field Visibility**
- Self-employed fields only appear when "Self Employed" income type selected
- Credit card fields differ from other liability types
- HECS shows percentage/balance fields

**4. UUID-Based IDs**
- Checkboxes and radio buttons often have UUID-based IDs
- Use `name` attribute selectors instead (e.g., `input[name="hasProfessionalPack"]`)
- Data-testid attributes are more stable where available

#### Income Type Dropdown Options (13)

**Selector**: `#type` (in income context)

- Bonus
- Commissions
- Dividends
- Family Allowance
- Maintenance
- Overtime
- Government Pension
- Superannuation Funds
- Salary
- Self Employed (triggers additional fields)
- OTHER
- Other (Tax Free)

#### Expense/Liability Type Dropdown Options (18)

**Selector**: `#type` (in expense context)

- Credit Card (shows Limit field)
- Car Loan
- Rent Paid
- Personal Loan
- Basic/Standard Living Expenses
- Additional Living Expenses
- Commercial Bill
- HECS (shows percentage/balance fields)
- Hire Purchase
- Lease
- Line Of Credit
- Loan As Guarantor
- Other Loan
- Outstanding Taxation
- Overdraft
- Store Card
- Term Loan

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

### Workflow 8: Add Real Estate Asset

**Status**: Validated
**Triggers Modal**: No
**Auto-Save**: Yes (implicit)
**Section**: Financials → Assets - Real Estate
**Complexity**: Extremely Complex (Score: 205.37)
**Recording Date**: 2025-10-09
**Duration**: 5 minutes 29 seconds

**Critical Challenges**:
- **Address Autocomplete**: React Bootstrap Typeahead with dynamic dropdown
- **No Stable ID** for address input (class-based selectors only)
- **Dynamic UUID Selectors** on checkboxes
- **Timing Sensitive**: Autocomplete requires specific interaction patterns

**Critical Notes**:
- Address field has NO stable ID - use `.rbt-input-main.form-control.rbt-input` or role/placeholder
- Must select from autocomplete dropdown (cannot type full address manually)
- Checkbox selectors contain dynamic UUIDs - use name attribute or partial ID matching
- Wait for `aria-expanded="true"` before selecting from dropdown

**Steps**:

1. **Navigate to Financials Tab**
   - Selector: `#financials`
   - Action: Click
   - Wait: 1000ms for tab to load
   - Full Selector: `button#financials.TabButton-module_tab-button__LmGvF`

2. **Navigate to Assets - Real Estate Sub-Tab**
   - Selector: `#realEstateAssets`
   - Action: Click
   - Wait: 9000ms for section to load
   - Classes: `css-ed1oc7 btn btn-secondary`

3. **Click Add Real Estate Asset Button**
   - Selector: `[data-testid="Add"]`
   - Action: Click
   - Wait: 6000ms for new row to appear
   - Full ID: `#btn_61c06b1f-9045-4817-a8ed-79408286395f` (UUID-based, use data-testid instead)
   - Label: "Real Estate Asset"

**🆕 NEW DISCOVERY: Address Format Selection**

Before entering the address, you can choose from THREE address entry methods via radio buttons:

- **Option A: Standard Address** (`#format_standard`) - DEFAULT
  - Uses autocomplete/structured fields (documented in steps 4-5 below)
  - Best for standard Australian addresses

- **Option B: Non-Standard Address** (`#format_nonStandard`)
  - Enables manual/freeform address entry
  - Bypasses autocomplete entirely
  - Use for rural properties, international addresses, or complex address formats
  - See "Alternative: Manual Address Entry" section below

- **Option C: PO Box** (`#format_poBox`)
  - Specialized fields for PO Box addresses
  - Use when property is identified by PO Box

**Standard Address Entry (Default)** - Steps 4-5 below show this method

4. **Enter Property Address (React Bootstrap Typeahead - Standard Format)**
   - Selector: `.rbt-input-main.form-control.rbt-input` (NO stable ID!)
   - Alternative: `input[role="combobox"][placeholder="Search for property address..."]`
   - Action: Click to focus, then type incrementally
   - Wait: 3300ms after click
   - ARIA Attributes:
     - `aria-autocomplete="both"`
     - `aria-expanded="false"` (changes to `"true"` when dropdown appears)
     - `aria-haspopup="listbox"`
   - **Critical**: Type slowly to trigger autocomplete (0.5-1s between keystrokes)
   - **Autocomplete Behavior**:
     - Dropdown appears after ~4 characters
     - Wait for `aria-expanded="true"` attribute
     - Addresses shown in UPPERCASE standardized format
     - Must wait ~4.2 seconds before selecting from dropdown
   - Example typing pattern:
     ```python
     address_input.send_keys("11 Cam")  # Wait for dropdown
     time.sleep(2)
     # Wait for aria-expanded="true"
     ```

5. **Select Address from Autocomplete Dropdown**
   - Selector: `#rbt-menu-item-1 > a.dropdown-item > option` (dynamic menu ID)
   - Alternative Pattern: `li[id^='rbt-menu-item-'] > a.dropdown-item > option`
   - Action: Click the OPTION element (not the container)
   - Wait: 3300ms after selection
   - **Critical**: Must click the `<option>` element inside dropdown item
   - **Wrong**: Click `#rbt-menu-item-1` or `.dropdown-item`
   - **Correct**: Click `#rbt-menu-item-1 > a.dropdown-item > option`
   - Format: "11 CAMERON AVENUE ARTARMON 2064 NSW" (uppercase, no commas)

**🆕 ALTERNATIVE: Manual Address Entry (Non-Standard Format)**

If autocomplete is problematic or the address doesn't fit standard format, use this method instead:

5a. **Select Non-Standard Address Format**
   - Selector: `#format_nonStandard`
   - Type: radio button
   - Name: `format`
   - Value: `nonStandard`
   - Action: Click radio button
   - Result: Form switches to manual address entry fields

5b. **Enter Address Manually (Structured Fields)**
   - **Street Number**: `#streetNumber` - Enter street number
   - **Street Name**: `#streetName` - Enter street name
   - **Street Type**: `#streetType` - Select from 217 options (Street, Road, Avenue, Court, etc.)
   - **City/Suburb**: `#city` - Enter city or suburb
   - **State**: `#state` - Select from NSW, VIC, QLD, SA, WA, TAS, NT, ACT
   - **Postcode**: `#postcode` - Enter 4-digit postcode
   - **Country**: `#country` - Select country (default: Australia)
   - Note: All fields are standard text/select inputs, no autocomplete complexity

**When to Use Manual Entry**:
- Autocomplete not finding the address
- Rural properties with non-standard addressing
- New developments not yet in address database
- International properties
- Complex address formats (e.g., "Via X Road", "C/- Address")

6. **Enter Property Value**
   - Selector: `#value`
   - Action: Clear and type text
   - Wait: 3300ms after click, 1300ms after entry
   - Type: Currency input (auto-formats)
   - Attributes: `data-field-type="currency"`
   - Alignment: Right-aligned
   - Placeholder: Dynamic (updates as you type)
   - Example: "6000000"

7. **Select Valuation Basis**
   - Selector: `#valueBasis`
   - Action: Select from dropdown
   - Wait: 1300ms after value entry, 1400ms after selection
   - Options:
     - `""` - "<Clear Valuation Basis>"
     - "Applicant Estimate"
     - "Certified Valuation"
     - "Actual Value"
   - Type: Native select dropdown
   - **Note**: User may click dropdown twice (double-click pattern observed)

8. **Select Primary Purpose**
   - Selector: `#realEstatePurpose`
   - Action: Select from dropdown
   - Wait: 1400ms after valuation basis, 1300ms after selection
   - Options:
     - `""` - "<Clear Primary Purpose>"
     - "Owner Occupied"
     - "Investment"
   - Type: Native select dropdown

9. **Toggle "Used as Security" Checkbox (Optional)**
   - Selector: `#security_{UUID}_realEstateUseAsSecurity` (UUID varies)
   - Better Selector: `input[name="realEstateUseAsSecurity"]`
   - Alternative: `input[id*="_realEstateUseAsSecurity"]` (partial ID match)
   - Action: Click checkbox or label
   - Wait: 500ms between toggles
   - Type: Custom checkbox
   - Classes: `custom-control-input`
   - Label Selector: `label.custom-control-label[for*="security"]`
   - **Note**: Can click either checkbox or label element
   - **UUID Pattern**: `security_9d3d9849-a4c5-11f0-9423-005056b5e136_realEstateUseAsSecurity`

10. **Toggle "To be Purchased" Checkbox (Optional)**
    - Selector: `#purchased_{UUID}_realEstateToBePurchased` (UUID varies)
    - Better Selector: `input[name="realEstateToBePurchased"]`
    - Alternative: `input[id*="_realEstateToBePurchased"]` (partial ID match)
    - Action: Click checkbox or label
    - Wait: 500ms between toggles
    - Type: Custom checkbox
    - Classes: `custom-control-input`
    - Label Selector: `label.custom-control-label[for*="purchased"]`
    - **Note**: Wait 7300ms before first interaction with this checkbox

11. **Auto-Save**
    - Wait: 2000ms after final field for implicit auto-save
    - Validation: Check `hasActiveRequests: false` and `readyState: "complete"`

**Address Autocomplete - Detailed Implementation**:

The address autocomplete is the most technically challenging aspect. Here's the complete pattern:

```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Locate address input (no stable ID!)
address_input = driver.find_element(
    By.CSS_SELECTOR,
    "input.rbt-input-main[placeholder='Search for property address...']"
)

# Click to focus
address_input.click()
time.sleep(1)

# Type incrementally (simulate human typing)
partial_address = "11 Cameron Avenue"
for char in partial_address:
    address_input.send_keys(char)
    time.sleep(0.1)  # Small delay between characters

# Wait for dropdown to appear (aria-expanded changes to "true")
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((
        By.CSS_SELECTOR,
        "input.rbt-input-main[aria-expanded='true']"
    ))
)
time.sleep(2)  # Extra buffer for dropdown rendering

# Select from dropdown (must click the option element)
dropdown_option = driver.find_element(
    By.CSS_SELECTOR,
    "li[id^='rbt-menu-item-'] > a.dropdown-item > option"
)
dropdown_option.click()
time.sleep(3)  # Wait for selection to register

# Verify selection
selected_value = address_input.get_attribute("value")
print(f"Selected address: {selected_value}")
```

**Complete Example**:
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Steps 1-2: Navigate to Real Estate Assets
driver.find_element(By.ID, "financials").click()
time.sleep(1)
driver.find_element(By.ID, "realEstateAssets").click()
time.sleep(9)

# Step 3: Click Add
driver.find_element(By.CSS_SELECTOR, '[data-testid="Add"]').click()
time.sleep(6)

# Step 4-5: Address with autocomplete
address_input = driver.find_element(
    By.CSS_SELECTOR,
    "input.rbt-input-main.form-control.rbt-input"
)
address_input.click()
time.sleep(3)

# Type incrementally
partial_address = "11 Cameron Avenue"
for char in partial_address:
    address_input.send_keys(char)
    time.sleep(0.1)

# Wait for dropdown
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((
        By.CSS_SELECTOR,
        "input[aria-expanded='true']"
    ))
)
time.sleep(2)

# Select from dropdown
dropdown_option = driver.find_element(
    By.CSS_SELECTOR,
    "li[id^='rbt-menu-item-'] > a.dropdown-item > option"
)
dropdown_option.click()
time.sleep(3)

# Step 6: Property value
driver.find_element(By.ID, "value").clear()
driver.find_element(By.ID, "value").send_keys("6000000")
time.sleep(1)

# Step 7: Valuation basis
value_basis = Select(driver.find_element(By.ID, "valueBasis"))
value_basis.select_by_visible_text("Applicant Estimate")
time.sleep(1)

# Step 8: Primary purpose
purpose = Select(driver.find_element(By.ID, "realEstatePurpose"))
purpose.select_by_visible_text("Owner Occupied")
time.sleep(1)

# Step 9-10: Checkboxes (using name selectors to avoid UUID issues)
security_checkbox = driver.find_element(By.NAME, "realEstateUseAsSecurity")
security_checkbox.click()
time.sleep(0.5)

purchased_checkbox = driver.find_element(By.NAME, "realEstateToBePurchased")
purchased_checkbox.click()
time.sleep(2)  # Auto-save

print("Real estate asset entry saved")
```

**🆕 Complete Example - Manual Address Entry (Simpler Alternative)**:
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Steps 1-2: Navigate to Real Estate Assets
driver.find_element(By.ID, "financials").click()
time.sleep(1)
driver.find_element(By.ID, "realEstateAssets").click()
time.sleep(9)

# Step 3: Click Add
driver.find_element(By.CSS_SELECTOR, '[data-testid="Add"]').click()
time.sleep(6)

# Step 3A: Select Non-Standard Address Format (to enable manual entry)
non_standard_radio = driver.find_element(By.ID, "format_nonStandard")
non_standard_radio.click()
time.sleep(1)

# Step 5b: Enter address manually (NO autocomplete complexity!)
driver.find_element(By.ID, "streetNumber").send_keys("11")
time.sleep(0.5)

driver.find_element(By.ID, "streetName").send_keys("Cameron Avenue")
time.sleep(0.5)

street_type = Select(driver.find_element(By.ID, "streetType"))
street_type.select_by_visible_text("Avenue")
time.sleep(0.5)

driver.find_element(By.ID, "city").send_keys("Artarmon")
time.sleep(0.5)

state = Select(driver.find_element(By.ID, "state"))
state.select_by_visible_text("NSW")
time.sleep(0.5)

driver.find_element(By.ID, "postcode").send_keys("2064")
time.sleep(0.5)

# Country defaults to Australia, no need to change

# Step 6: Property value
driver.find_element(By.ID, "value").clear()
driver.find_element(By.ID, "value").send_keys("6000000")
time.sleep(1)

# Step 7: Valuation basis
value_basis = Select(driver.find_element(By.ID, "valueBasis"))
value_basis.select_by_visible_text("Applicant Estimate")
time.sleep(1)

# Step 8: Primary purpose
purpose = Select(driver.find_element(By.ID, "realEstatePurpose"))
purpose.select_by_visible_text("Owner Occupied")
time.sleep(1)

# Step 9-10: Checkboxes
security_checkbox = driver.find_element(By.NAME, "realEstateUseAsSecurity")
security_checkbox.click()
time.sleep(0.5)

purchased_checkbox = driver.find_element(By.NAME, "realEstateToBePurchased")
purchased_checkbox.click()
time.sleep(2)  # Auto-save

print("Real estate asset entry saved (manual address method)")
```

**When to Use Manual Entry vs. Autocomplete**:

| Scenario | Recommended Method | Why |
|----------|-------------------|-----|
| Standard Australian address | Autocomplete | Faster if address is in database |
| Rural property | Manual Entry | Often not in autocomplete database |
| New development | Manual Entry | Address may not exist yet |
| Complex/non-standard address | Manual Entry | Avoids autocomplete issues |
| Automation reliability needed | Manual Entry | No dynamic dropdown handling |
| International property | Manual Entry | Autocomplete is AU-focused |

**Alternative Checkbox Selection (Partial ID Matching)**:
```python
# If name attribute is not available, use partial ID matching
security_checkbox = driver.find_element(
    By.CSS_SELECTOR,
    "input[id*='_realEstateUseAsSecurity']"
)

purchased_checkbox = driver.find_element(
    By.CSS_SELECTOR,
    "input[id*='_realEstateToBePurchased']"
)
```

**Troubleshooting Address Autocomplete**:

1. **Dropdown not appearing**:
   - Ensure input has focus (click first)
   - Type slowly (minimum 0.1s between characters)
   - Type at least 4-5 characters before expecting dropdown
   - Check `aria-expanded` attribute is `"true"`

2. **Cannot find dropdown option**:
   - Wait for dropdown rendering (minimum 2s after `aria-expanded="true"`)
   - Use generic selector: `li[id^='rbt-menu-item-']` to find all options
   - Ensure clicking the `<option>` element, not parent elements

3. **Selection not registering**:
   - Add 3-4s wait after clicking dropdown option
   - Verify selection by checking input's `value` attribute
   - Ensure not clicking too fast (autocomplete needs time to process)

**Timing Summary**:
- Total workflow duration: ~5 minutes 29 seconds (329 seconds)
- Critical waits:
  - After Financials tab: 1s
  - After Real Estate section: 9s (page load)
  - After Add button: 6s (form rendering)
  - Address autocomplete: 3s + 2s + 4.2s + 3s = ~12s total
  - Between fields: 1-3s
  - Auto-save: 2s at end

**Field Selectors Reference**:

| Field Name | Selector | Type | Notes |
|------------|----------|------|-------|
| **Navigation** |
| Financials Tab | `#financials` | button | Navigation |
| Real Estate Section | `#realEstateAssets` | button | Sub-navigation |
| Add Button | `[data-testid="Add"]` | button | Stable selector |
| **🆕 Address Format Selection** |
| Standard Address | `#format_standard` | radio | Default, enables autocomplete |
| Non-Standard Address | `#format_nonStandard` | radio | Enables manual entry |
| PO Box | `#format_poBox` | radio | Enables PO Box fields |
| **Address - Autocomplete (Standard)** |
| Address Input | `.rbt-input-main.form-control.rbt-input` | input | ⚠️ No stable ID |
| Address Dropdown | `li[id^='rbt-menu-item-'] > a > option` | option | Dynamic ID |
| **🆕 Address - Manual Entry (Non-Standard)** |
| Street Number | `#streetNumber` | input | Manual entry |
| Street Name | `#streetName` | input | Manual entry |
| Street Type | `#streetType` | select | 217 options |
| City/Suburb | `#city` | input | Manual entry |
| State | `#state` | select | NSW, VIC, QLD, etc. |
| Postcode | `#postcode` | input | 4 digits |
| Country | `#country` | select | Defaults to Australia |
| **Property Details** |
| Property Value | `#value` | input | Currency, right-aligned |
| Valuation Basis | `#valueBasis` | select | Native dropdown |
| Primary Purpose | `#realEstatePurpose` | select | Native dropdown |
| **🆕 Additional Fields** |
| Property Type | `#propertyType` | select | 63 options |
| Property Status | `#propertyStatus` | select | Options TBD |
| Real Estate Zoning | `#realEstateZoning` | select | Options TBD |
| Property Title Type | `#propertyTitleType` | select | Options TBD |
| Priority | `#priority` | input | Numeric |
| **Checkboxes** |
| Used as Security | `input[name="realEstateUseAsSecurity"]` | checkbox | ⚠️ UUID in ID |
| To be Purchased | `input[name="realEstateToBePurchased"]` | checkbox | ⚠️ UUID in ID |

**Validation Rules**:
- **Address (Autocomplete)**: Requires selection from dropdown
- **Address (Manual)**: Individual fields validated independently
- Value: Currency format, accepts numeric input
- Valuation Basis: Optional (has clear option)
- Primary Purpose: Optional (has clear option)
- Checkboxes: Optional, independent

---

### Workflow 9: Complete Borrowing Capacity Calculation

**Status**: Validated
**Triggers Modal**: Yes (for income/expense entries)
**Auto-Save**: Yes
**Section**: Calculations → Borrowing Capacity
**Complexity**: Extremely Complex (Score: 286.91)
**Recording Date**: 2025-10-09
**Duration**: 6 minutes 17 seconds
**Total Events**: 193 (126 clicks, 61 inputs)

**Description**: Complete borrowing capacity calculation for 2 applicants with multiple income sources (Salary, Dividends, Family Allowance, Commissions), multiple expenses (HECS, Credit Card, Rent), and a real estate investment asset.

**Critical Challenges**:
- **Dynamic UUID Selectors** on checkboxes and many buttons
- **Multiple Applicant Workflow**: Separate data entry for each borrower with collapsible sections
- **Modal-Based Income/Expense Entry**: Each item requires dropdown selections + amount entry
- **Nested Form Structure**: Applicants → Income/Expenses → Assets → Liabilities
- **Data-testid Attributes**: Present on "Add Income" and "Add Expense" buttons
- **Dynamic Content Loading**: Sections expand/collapse requiring wait times

**Critical Notes**:
- This workflow creates **2 applicants** (Borrower 1: "Andrew Effie", Borrower 2: Second applicant)
- Each applicant has collapsible sections for Incomes, Expenses, and ownership details
- Income types include: Salary, Dividends, Family Allowance, Commissions
- Expense types include: HECS, Credit Card, Rent Paid, Basic Living Expenses
- Assets section is shared across all applicants
- Professional Pack checkbox uses dynamic UUID: `#[UUID]_hasProfessionalPack_hasProfessionalPack`
- Multiple Households checkbox uses dynamic UUID: `#[UUID]_multipleHouseholds_multipleHouseholds`
- Real estate purpose radio buttons use dynamic UUIDs: `#[UUID]_realEstatePurpose_[value]`
- "Add Income" button uses data-testid: `btnAddIncome_[UUID]`
- "Add Expense" button uses data-testid: `btnAddExpense`
- Wait times are critical between sections to allow forms to load

**Steps**:

**Phase 1: Navigate to Calculations**

1. **Navigate to Calculations Tab**
   - Selector: `#calculations`
   - Action: Click
   - Full text: "Calculations(1)"
   - Classes: `TabButton-module_tab-button__LmGvF crmDetailsPageMenu`
   - Wait: ~6 seconds for tab to load

**Phase 2: Start New Borrowing Capacity Calculation**

2. **Click Add Dropdown**
   - Selector: `button.dropdown-toggle.btn.btn-light.btn-sm` (within MAFToolbar)
   - Action: Click to open dropdown menu
   - Text: "Add"
   - Wait: ~6 seconds

3. **Select "Borrowing Capacity" from Dropdown**
   - Selector: `button.dropdown-item:nth-of-type(2)` (within `.dropdown-menu.show`)
   - Action: Click
   - Text: "Borrowing Capacity"
   - Icon: piggy-bank icon
   - Wait: ~8 seconds for modal to appear

4. **Click "Proceed" in Modal**
   - Selector: `.btn.btn-outline-primary`
   - Action: Click
   - Text: "Proceed"
   - Context: Modal confirmation to start new calculation
   - Wait: ~8 seconds for main form to load

**Phase 3: Configure Basic Calculation Settings**

5. **Enter Loan Term**
   - Selector: `#loanTerm`
   - Action: Click (3x) to select all, then input
   - Value: `20` (years)
   - Type: number input
   - Wait: ~1 second between clicks

6. **Select Real Estate Purpose**
   - Selector: `#realEstatePurpose`
   - Action: Click dropdown, select option
   - Options: "Owner Occupied" | "Investment"
   - Selected: "Investment" (user clicked twice - selected "Investment")
   - Type: select dropdown
   - Wait: ~1 second

7. **Enter LVR (Loan-to-Value Ratio)**
   - Selector: `#lvrText`
   - Action: Click (4x) to select, then input
   - Value: `80` (percent)
   - Type: number input
   - Data attribute: May have data-field-type
   - Wait: ~1 second

8. **Check "Has Professional Pack" Checkbox**
   - Selector: `input[name="hasProfessionalPack"]` (ID is dynamic UUID)
   - Full ID example: `#36c350e2-9c61-4511-af6d-a8663c6474bb_hasProfessionalPack_hasProfessionalPack`
   - Action: Click checkbox (2 clicks to toggle on)
   - Type: checkbox
   - Value: "on"
   - Classes: `custom-control-input`
   - **Note**: UUID changes between sessions - use name attribute instead

9. **Enter Loan Amount Requested**
   - Selector: `#loanRequested`
   - Action: Click, then input
   - Value: `1000000` (entered as "1" then "1000000")
   - Type: text input (currency)
   - Data attribute: `data-field-type="currency"`
   - Label: "Loan Requested"
   - Placeholder: "0.00"
   - Wait: ~1 second

10. **Enter Number of Dependants**
    - Selector: `#dependants`
    - Action: Click (3x) to select, then input
    - Value: `01` (entered as "0" then "01")
    - Type: number input
    - Wait: ~1 second

11. **Check "Multiple Households" Checkbox**
    - Selector: `input[name="multipleHouseholds"]` (ID is dynamic UUID)
    - Full ID example: `#36c350e2-9c61-4511-af6d-a8663c6474bb_multipleHouseholds_multipleHouseholds`
    - Action: Click checkbox (2 clicks to toggle on)
    - Type: checkbox
    - Value: "on"
    - Classes: `custom-control-input`
    - **Note**: UUID changes between sessions - use name attribute

**Phase 4: Enter Applicant 1 Details**

12. **Expand Borrower 1 Section**
    - Text: "Borrowers Borrower"
    - Action: Click to expand collapsible card
    - Section header with CardList module
    - Wait: ~1 second for section to expand

13. **Expand "Incomes" Section**
    - Action: Click on "Incomes" section header
    - Context: Within Borrower 1 card
    - Wait: ~1 second for section to expand

**Add Income #1: Salary**

14. **Click "Add Income" Button**
    - Data-testid: `btnAddIncome_[UUID]` (UUID varies)
    - Example ID: `#btn_ccb2401f-3ad4-443a-bc05-55eaec0521db`
    - Action: Click
    - Wait: ~1 second for confirmation modal to appear

14a. **Click "Okay" in Confirmation Modal**
    - Selector: `button:contains("Okay")` or `button:contains("OK")`
    - Action: Click to proceed
    - Context: Confirmation modal appears after clicking Add Income
    - Wait: ~1 second for income form modal to appear
    - **Note**: This modal may not always appear - use try/except in automation

15. **Select Income Type: "Salary"**
    - Selector: `#type`
    - Action: Click dropdown (2x), then select
    - Options: Bonus, Commissions, Dividends, Family Allowance, Maintenance, Overtime, Government Pension, Superannuation Funds, Salary, etc.
    - Selected: "Salary"
    - Type: select dropdown

16. **Select Frequency: "Annual"**
    - Selector: `#frequency`
    - Action: Click dropdown (2x), then select
    - Options: Annual, Monthly, Fortnightly, Weekly
    - Selected: "Annual"
    - Type: select dropdown

17. **Enter Amount: $120,000**
    - Selector: `#amountText`
    - Action: Click, then input
    - Value: `120000` (entered as "12" then "120000")
    - Type: text input (currency)
    - Wait: ~1 second

**Add Income #2: Dividends**

18. **Click "Add Income" Button Again**
    - Same selector as step 14
    - Wait: ~1 second

19. **Select Income Type: "Dividends"**
    - Selector: `#type`
    - Selected: "Dividends"
    - Wait: ~1 second

20. **Select Frequency: "Annual"**
    - Selector: `#frequency`
    - Selected: "Annual"

21. **Enter Amount: $10,000**
    - Selector: `#amountText`
    - Value: `10000` (entered incrementally: "1", "10", "10000")
    - Wait: ~1 second

**Add Income #3: Family Allowance**

22. **Click "Add Income" Button**
    - Same selector
    - Wait: ~1 second

23. **Select Income Type: "Family Allowance"**
    - Selector: `#type`
    - Selected: "Family Allowance"

24. **Select Frequency: "Monthly"**
    - Selector: `#frequency`
    - Selected: "Monthly"

25. **Enter Amount: $200**
    - Selector: `#amountText`
    - Value: `200` (entered as "2" then "200")

**Add Income #4: Commissions**

26. **Click "Add Income" Button**
    - Same selector
    - Wait: ~1 second

27. **Select Income Type: "Commissions"**
    - Selector: `#type`
    - Selected: "Commissions"

28. **Select Frequency: "Fortnightly"**
    - Selector: `#frequency`
    - Selected: "Fortnightly"

29. **Enter Amount: $300**
    - Selector: `#amountText`
    - Value: `300` (entered as "3" then "300")

**Phase 5: Enter Applicant 1 Expenses**

30. **Expand "Expenses" Section**
    - Action: Click on "Expenses" section header
    - Context: Within Borrower 1 card
    - Wait: ~1 second for section to expand

**Add Expense #1: Living Expenses (auto-created)**

31. **Enter Living Expenses Amount**
    - Selector: `#amountText`
    - Value: `1000`
    - Context: Living Expenses row may auto-populate
    - Type: text input (currency)

**Add Expense #2: HECS**

32. **Select Expense Type: "HECS"**
    - Selector: `#type`
    - Action: Click dropdown (2x), then input
    - Options: Credit Card, Car Loan, Rent Paid, Personal Loan, Basic/Standard Living Expenses, Additional Living Expenses, Committed Savings, HECS, etc.
    - Selected: "HECS"
    - Type: select dropdown

33. **Select Frequency: "Annual"**
    - Selector: `#frequency`
    - Options: Annual, Monthly, Fortnightly, Weekly
    - Selected: "Annual" (user toggled through Weekly first)

34. **Enter Amount: $3,000**
    - Selector: `#amountText`
    - Value: `3000` (entered as "3" then "3000")

35. **Enter Balance: $10,000**
    - Selector: `#balance`
    - Value: `10000` (entered incrementally: "1", "10", "10000")
    - Context: HECS expenses require both amount AND balance
    - Wait: ~1 second

**Add Expense #3: Credit Card**

36. **Click "Add Expense" Button**
    - Data-testid: `btnAddExpense`
    - Example ID: `#btn_df105dec-b111-4844-883c-559e14776e15`
    - Action: Click
    - Wait: ~1 second for confirmation modal

36a. **Click "Okay" in Confirmation Modal** (if appears)
    - Selector: `button:contains("Okay")` or `button:contains("OK")`
    - Action: Click to proceed
    - Context: Confirmation modal may appear after clicking Add Expense
    - Wait: ~1 second for expense form modal to appear
    - **Note**: This modal may not always appear - use try/except in automation

37. **Select Expense Type: "Credit Card"**
    - Selector: `#type`
    - Selected: "Credit Card"

38. **Enter Credit Limit: $10,000**
    - Selector: `#creditLimitText`
    - Value: `10000` (entered incrementally: "1", "10", "10000")
    - Context: Credit Card expenses use "Credit Limit" instead of "Amount"

**Add Expense #4: Rent Paid**

39. **Click "Add Expense" Button**
    - Same selector as step 36
    - Wait: ~1 second

40. **Select Expense Type: "Rent Paid"**
    - Selector: `#type`
    - Selected: "Rent Paid"

41. **Select Frequency: "Monthly"**
    - Selector: `#frequency`
    - Selected: "Monthly"

42. **Enter Amount: $1,000**
    - Selector: `#amountText`
    - Value: `1000` (entered as "1" then "1000")

43. **Cancel Extra Expense Entry**
    - Selector: `button.btn.btn-primary:nth-of-type(2)` (within `.modal-footer`)
    - Text: "Cancel"
    - Action: Click to close modal
    - Context: User accidentally opened expense modal again
    - Wait: ~1 second

**Phase 6: Enter Applicant 2 Details**

44. **Click "Add Income" for Applicant 2**
    - Data-testid: `btnAddIncome_[different UUID]`
    - Example ID: `#btn_18552e2d-48ff-42eb-b46a-7a8b7319e600`
    - Context: Different button ID for second applicant
    - Wait: ~1 second

**Add Income #1: Salary**

45. **Select Income Type: "Salary"**
    - Selector: `#type`
    - Selected: "Salary"

46. **Select Frequency: "Annual"**
    - Selector: `#frequency`
    - Selected: "Annual"

47. **Enter Amount: $100,000**
    - Selector: `#amountText`
    - Value: `100000` (entered as "1" then "100000")
    - Wait: ~1 second

48. **Navigate to Expenses Section for Applicant 2**
    - Action: Click "Expenses" section header
    - Wait: ~1 second

**Phase 7: Enter Assets - Real Estate**

49. **Expand "Asset 1" Section**
    - Action: Click on "Asset 1" card header
    - Context: Assets section is shared across applicants
    - Wait: ~1 second for asset details to expand

50. **Select Real Estate Purpose: "Investment"**
    - Selector: `input[name="realEstatePurpose"][value="Investment"]` (ID is dynamic UUID)
    - Full ID example: `#8d5c0954-28ed-43cd-9d15-ef5a8dbd6eef_realEstatePurpose_Investment`
    - Action: Click radio button (2x to toggle)
    - Value: "Investment"
    - Type: radio button
    - **Note**: UUID changes between sessions - use name + value attributes

51. **Enter Property Value: $800,000**
    - Selector: `#value`
    - Value: `800000` (entered incrementally)
    - Type: text input (currency)
    - Wait: ~1 second

52. **Check "Real Estate To Be Purchased" Checkbox**
    - Selector: `input[name="realEstateToBePurchased"]` (ID is dynamic UUID)
    - Full ID example: `#8d5c0954-28ed-43cd-9d15-ef5a8dbd6eef_purchasing_realEstateToBePurchased`
    - Action: Click checkbox (3x to toggle on)
    - Value: "on"
    - Type: checkbox

53. **Check "Use As Security" Checkbox**
    - Selector: `input[name="realEstateUseAsSecurity"]` (ID is dynamic UUID)
    - Full ID example: `#8d5c0954-28ed-43cd-9d15-ef5a8dbd6eef_security_realEstateUseAsSecurity`
    - Action: Click checkbox (2x to toggle on)
    - Value: "on"
    - Type: checkbox

54. **Click on Proposed Loan Amount Field**
    - Selector: `#proposedLoanAmount`
    - Action: Click (2x)
    - Context: Field may auto-calculate or require manual entry
    - Wait: ~1 second

55. **Click on Proposed LVR Field**
    - Selector: `#proposedLvrText`
    - Action: Click
    - Context: Field may auto-calculate based on value and loan amount

**Rental Income Details**

56. **Select Rental Income Frequency: "Monthly"**
    - Selector: `#realEstateRentalIncomeFrequency`
    - Action: Click dropdown (2x), then select
    - Options: Annual, Monthly, Fortnightly, Weekly
    - Selected: "Monthly"

57. **Enter Rental Income: $600**
    - Selector: `#realEstateRentalIncome`
    - Value: `600`
    - Type: text input (currency)
    - Wait: ~1 second

**Investment Costs**

58. **Select Investment Cost Frequency: "Monthly"**
    - Selector: `#investmentCostFrequency`
    - Action: Click dropdown (2x), then select
    - Selected: "Monthly"

59. **Enter Investment Costs: $300**
    - Selector: `#investmentCost`
    - Value: `300` (entered as "3" then "300")
    - Type: text input (currency)

**Ownership Details**

60. **Expand "Ownership" Section**
    - Action: Click on "Ownership" section header
    - Wait: ~1 second for section to expand

61. **Enter Ownership Percentage**
    - Selector: `#ownership`
    - Action: Click (3x), then input
    - Value: `20` (entered as "80" first, then cleared to "2" then "20")
    - Type: number input
    - Context: Ownership split between applicants
    - Wait: ~1 second

**Automation Recommendations**:
- Use explicit waits (WebDriverWait) for modal appearances after clicking "Add Income" / "Add Expense"
- Implement dynamic UUID handling:
  - For checkboxes: Use `input[name="hasProfessionalPack"]` instead of ID
  - For radio buttons: Use `input[name="realEstatePurpose"][value="Investment"]`
- Verify each collapsible section has expanded before interacting with child elements
- Consider breaking into sub-workflows:
  1. Setup (Steps 1-11): Navigation + Basic Settings
  2. Applicant 1 (Steps 12-29): Income entries
  3. Applicant 1 Expenses (Steps 30-43)
  4. Applicant 2 (Steps 44-48)
  5. Assets (Steps 49-61)
  6. Calculate/Save
- Add checkpoint/resume capability due to workflow length (6+ minutes)
- Implement retry logic for dynamic content loading (wait for aria-expanded="true" on collapsible sections)
- Use data-testid attributes where available (`btnAddIncome_*`, `btnAddExpense`)

**Selenium Code Examples**:

```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Navigate to Calculations
driver.find_element(By.ID, "calculations").click()
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.dropdown-toggle.btn.btn-light.btn-sm")))

# Start Borrowing Capacity
driver.find_element(By.CSS_SELECTOR, "button.dropdown-toggle.btn.btn-light.btn-sm").click()
driver.find_element(By.CSS_SELECTOR, "button.dropdown-item:nth-of-type(2)").click()
driver.find_element(By.CSS_SELECTOR, ".btn.btn-outline-primary").click()

# Enter basic settings
driver.find_element(By.ID, "loanTerm").clear()
driver.find_element(By.ID, "loanTerm").send_keys("20")

driver.find_element(By.ID, "realEstatePurpose").click()
driver.find_element(By.XPATH, "//option[@value='Investment']").click()

driver.find_element(By.ID, "lvrText").clear()
driver.find_element(By.ID, "lvrText").send_keys("80")

# Handle dynamic UUID checkbox using name attribute
driver.find_element(By.CSS_SELECTOR, "input[name='hasProfessionalPack']").click()

driver.find_element(By.ID, "loanRequested").send_keys("1000000")
driver.find_element(By.ID, "dependants").send_keys("01")

# Add Income for Applicant 1
add_income_btn = driver.find_element(By.CSS_SELECTOR, "[data-testid^='btnAddIncome_']")
add_income_btn.click()

# Handle "Okay" confirmation modal (may not always appear)
try:
    ok_button = WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Okay') or contains(text(), 'OK')]"))
    )
    ok_button.click()
except:
    pass  # Modal didn't appear

# Wait for income form modal
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "type")))

# Select income type
income_type = driver.find_element(By.ID, "type")
income_type.click()
driver.find_element(By.XPATH, "//option[text()='Salary']").click()

# Select frequency
frequency = driver.find_element(By.ID, "frequency")
frequency.click()
driver.find_element(By.XPATH, "//option[text()='Annual']").click()

# Enter amount
driver.find_element(By.ID, "amountText").send_keys("120000")

# Submit (find save/submit button in modal)
driver.find_element(By.CSS_SELECTOR, ".modal-footer .btn.btn-primary").click()
```

**Field Reference Summary**:

**Basic Settings:**
- `#loanTerm` - Loan term in years
- `#realEstatePurpose` - Select: "Owner Occupied" or "Investment"
- `#lvrText` - LVR percentage (number input)
- `input[name="hasProfessionalPack"]` - Professional pack checkbox (dynamic ID)
- `#loanRequested` - Loan amount (currency input)
- `#dependants` - Number of dependants (number input)
- `input[name="multipleHouseholds"]` - Multiple households checkbox (dynamic ID)

**Income Modal Fields:**
- `#type` - Income type dropdown (Salary, Dividends, etc.)
- `#frequency` - Frequency dropdown (Annual, Monthly, Fortnightly, Weekly)
- `#amountText` - Income amount (currency input)

**Expense Modal Fields:**
- `#type` - Expense type dropdown (HECS, Credit Card, Rent Paid, etc.)
- `#frequency` - Frequency dropdown
- `#amountText` - Expense amount (currency input)
- `#balance` - Balance field (for HECS and similar)
- `#creditLimitText` - Credit limit (for Credit Card expenses)

**Asset Fields:**
- `input[name="realEstatePurpose"]` - Radio button (Owner Occupied/Investment, dynamic ID)
- `#value` - Property value (currency input)
- `input[name="realEstateToBePurchased"]` - Checkbox (dynamic ID)
- `input[name="realEstateUseAsSecurity"]` - Checkbox (dynamic ID)
- `#proposedLoanAmount` - Proposed loan amount
- `#proposedLvrText` - Proposed LVR
- `#realEstateRentalIncomeFrequency` - Rental frequency dropdown
- `#realEstateRentalIncome` - Rental income amount
- `#investmentCostFrequency` - Investment cost frequency dropdown
- `#investmentCost` - Investment cost amount
- `#ownership` - Ownership percentage (number input)

**Dropdown Options Discovered**:

**Income Types:**
- Bonus
- Commissions
- Dividends
- Family Allowance
- Maintenance
- Overtime
- Government Pension
- Superannuation Funds
- Salary

**Expense Types:**
- Credit Card
- Car Loan
- Rent Paid
- Personal Loan
- Basic/Standard Living Expenses
- Additional Living Expenses
- Committed Savings
- HECS

**Frequency Options:**
- Annual
- Monthly
- Fortnightly
- Weekly

**Real Estate Purpose:**
- Owner Occupied
- Investment

---

### Workflow 10: Login and Dashboard Navigation (Unified)

**Status**: Validated ✅
**Version**: 2.0.0
**Triggers Modal**: No
**Auto-Save**: N/A
**Complexity**: Medium (Score: 45.5)
**Total Modes**: 4 (existing_client, dashboard_action, opportunity, dashboard_only)
**Documentation**: [Complete Guide](./LOGIN_AND_DASHBOARD_WORKFLOW.md)

**Description**: Unified login and navigation workflow supporting 4 different modes for accessing Connective CRM. Handles authentication, email verification, CRM navigation, client search, dashboard actions, and opportunity creation.

**Critical Features**:
- **Cookie-Based Session**: Saves cookies to skip email verification on subsequent runs (saves ~60 seconds)
- **Multi-Tab Handling**: Automatically handles CRM opening in new tab
- **Keyboard Typing for Autocomplete**: Uses character-by-character typing to trigger search dropdowns
- **4 Operational Modes**: Flexible entry points for different workflows
- **Fuzzy Matching**: Smart value matching for opportunity types with 80% similarity threshold

**Timing**:
- First run (with email verification): ~49 seconds
- Cached runs (with cookies): ~9 seconds (81% faster)

**Steps**:

**Phase 1: Authentication**

1. **Navigate to Login URL**
   - URL: `https://login.connective.com.au/`
   - Wait: 2 seconds for page load

2. **Enter Username**
   - Selector: `#logname`
   - Action: Click → Fill
   - Pattern: Excel to Paste

3. **Enter Password**
   - Selector: `#password`
   - Action: Click → Fill
   - Pattern: Excel to Paste

4. **Submit Login**
   - Selector: `button[type="submit"]`
   - Action: Click

5. **Email Verification Wait** (First Run Only)
   - Wait: 30 seconds (configurable up to 60s)
   - Manual email approval required
   - Cookies saved for future runs

6. **Post-Login Redirect**
   - Expected URL: `https://apps.connective.com.au/`
   - Wait: 8 seconds for dashboard tiles

**Phase 2: CRM Navigation**

7. **Click CRM Tile**
   - Selector: `#appTile_CRM`
   - Action: Click
   - Behavior: Opens new browser tab
   - Wait: 3 seconds

8. **Switch to CRM Tab**
   - Action: Get all pages → Switch to page containing "crm.connective.com.au"
   - Verification: URL contains `crm.connective.com.au/#/`
   - Wait: 2 seconds

**Phase 3A: Client Search (Mode 1: existing_client)**

9. **Focus Universal Search Bar**
   - Selector: `input.form-control[placeholder="Search"]`
   - Action: Click
   - Wait: 500ms

10. **Type Client Name** (Character-by-Character)
    - Selector: `input.form-control[placeholder="Search"]`
    - Action: Type with 100ms delay between characters
    - **Critical**: DO NOT use paste/fill - autocomplete won't trigger
    - Example: "Andrew Effi" → 'A' → 'n' → 'd' → ...

11. **Wait for Autocomplete Dropdown**
    - Selector: `.dropdown-menu.show`
    - Timeout: 5 seconds

12. **Click Client Result**
    - Selector: `a.list-group-item:has-text("{client_name}")` AND `:has-text("(Lead)")`
    - Filter: Must contain both client name AND "(Lead)"
    - Action: Click

**Phase 3B: Dashboard Action (Mode 2: dashboard_action)**

9. **Click Dashboard Action Button**
   - Selector: `button:has-text('{dashboard_action}')`
   - Valid Actions: Person, Task, Doc Request, Funding Position, Borrowing Capacity, Product Comparison
   - Action: Click
   - Wait: 2 seconds

**Phase 3C: Opportunity Creation (Mode 3: opportunity)**

9. **Click Opportunity Dropdown**
   - Selector: `button.dropdown-toggle:has-text('Opportunity')`
   - Action: Click
   - Wait: 1.5 seconds

10. **Wait for Dropdown Menu**
    - Selector: `.dropdown-menu.show`
    - Timeout: 3 seconds

11. **Select Opportunity Type**
    - Primary Selector: `button[name='{opportunity_type}']`
    - Fallback: `button.dropdown-item:has-text('{opportunity_type}')`
    - Options: Home Loans, Commercial Loans, Asset Finance, Business Loans
    - Fuzzy Match: 80% threshold (e.g., "Home Loan" → "Home Loans")
    - Action: Click
    - Wait: 2 seconds

**Phase 3D: Dashboard Only (Mode 4: dashboard_only)**

9. **No Additional Navigation**
   - Stay on CRM dashboard
   - Ready for manual navigation

**Critical Selectors**:

| Element | Selector | Notes |
|---------|----------|-------|
| Login Username | `#logname` | Text input |
| Login Password | `#password` | Password input |
| Login Submit | `button[type="submit"]` | Form submit |
| CRM Tile | `#appTile_CRM` | Opens new tab |
| Universal Search | `input[placeholder="Search"]` | Keyboard typing required |
| Search Result | `a.list-group-item:has-text("{name}")` | Click to open |
| Dashboard Button | `button:has-text('{action}')` | Consistent pattern |
| Opportunity Dropdown | `button.dropdown-toggle:has-text('Opportunity')` | Bootstrap dropdown |
| Opportunity Option | `button.dropdown-item:has-text('{type}')` | In dropdown menu |

**Automation Recommendations**:
- **Cookie Persistence**: Save `.browser_cookies.json` and `.browser_storage.json` after first successful login
- **Keyboard Typing**: Always use `.type()` with 100ms delay for search bars, NEVER `.fill()`
- **Tab Handling**: Explicitly switch to new tab using page context, don't rely on auto-focus
- **Fuzzy Matching**: Implement 80% similarity threshold for opportunity types to handle typos
- **Skip Logic**: Check if client_name/dashboard_action/opportunity_type is blank before executing phase 3
- **Error Recovery**: If dropdown doesn't appear within 5s, retry keyboard typing

**Integration Pattern**:
```python
# This workflow is the foundation for ALL other workflows
# Use as first step, then continue with workflow-specific actions

# Example: Login → Borrowing Capacity
await login_executor.execute()  # Workflow 10
await borrowing_capacity_executor.execute()  # Workflow 9

# Browser stays open, session persists
```

**Related Workflows**: This login workflow is required for Workflows 1-9

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
