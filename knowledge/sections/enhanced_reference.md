# Connective CRM - Enhanced Knowledge Reference
# Integrated with Universal Browser Agent

**Last Updated**: 2025-10-06
**Total Elements**: 74+
**Sections Covered**: 8 CRM Tabs
**Dropdown Fields**: 19+
**Integration Status**: ✅ Validated with Universal Browser Agent patterns
**Architecture**: Modular (Master → Tab Deep Dives → Quick Reference)

---

## 🗺️ CRM Tab Navigation Map

**How to Use This Guide**:
- 📘 **Master File** (this file): Strategic overview, quick selectors, integration status
- 📗 **Tab Detail Files**: Deep tactical documentation for each CRM tab
- 📙 **Quick Reference**: Automation cheat sheet for coders

---

### 🎯 CRM Tab Structure

```
Connective CRM
├── Dashboard
│   └── [Coverage: Basic, see Master]
│
├── 📋 Details Tab → [DETAILS_TAB.md] (future)
│   ├── Opportunity Info
│   ├── Agent/Lender Selection
│   └── Transaction Details
│
├── 💰 Financials Tab → [FINANCIALS_OVERVIEW.md] (future)
│   ├── 💸 Living Expenses → [LIVING_EXPENSES_DETAILED.md] ✅ NEW
│   ├── 💳 Liabilities → [LIABILITIES_DETAILED.md] ✅ NEW
│   ├── 🏠 Real Estate Assets → [REAL_ESTATE_DETAILED.md] (future)
│   ├── 💼 Other Assets → [OTHER_ASSETS_DETAILED.md] (future)
│   └── 📊 Income/Employment → [INCOME_EMPLOYMENT_DETAILED.md] (future)
│
├── 👔 Employment Tab → [EMPLOYMENT_DETAILED.md] (future)
│   └── Employment history, current job details
│
├── 💵 Incomes Tab → [INCOMES_DETAILED.md] (future)
│   └── Income sources, frequency, amounts
│
├── 📎 Attachments Tab → [ATTACHMENTS_DETAILED.md] (future)
│   └── File uploads, document management
│
├── 📝 Questionnaires Tab → [QUESTIONNAIRES_DETAILED.md] (future)
│   └── Needs analysis, compliance forms (AG-Grid)
│
├── 🗒️ Notes Tab → [NOTES_DETAILED.md] (future)
│   └── Rich text notes, communication log (Froala)
│
└── ✅ BID & NCCP Tab → [BID_NCCP_DETAILED.md] (future)
    └── Compliance stages, credit guide
```

---

## 📚 File Guide

| File | Purpose | When to Use |
|------|---------|------------|
| **📘 CONNECTIVE_CRM_KNOWLEDGE_ENHANCED.md** (this file) | Strategic overview, pattern status, quick selectors | First stop for any CRM question |
| **📗 {TAB}_DETAILED.md** | Deep dive: selectors, workflows, recordings, timing | Implementing/debugging specific tab |
| **📙 AUTOMATION_QUICK_REFERENCE.md** | Condensed cheat sheet for coding | During active automation coding |
| **📓 CLAUDE.md** | Workflow-specific guidance | Understanding this specific workflow |

---

## 🔍 Quick Navigation

**By CRM Tab**:
- [Dashboard](#dashboard-section)
- [Details Tab](#details-section)
- [Financials Tab](#financials-section) → [Living Expenses](#living-expenses), [Liabilities](#liabilities)
- [Employment Tab](#employment-section)
- [Incomes Tab](#incomes-section)
- [Attachments Tab](#attachments-section)
- [Questionnaires Tab](#questionnaires-section)
- [Notes Tab](#notes-section)
- [BID & NCCP Tab](#bid-nccp-section)

**By Task**:
- [Adding Living Expenses](#living-expenses) → [LIVING_EXPENSES_DETAILED.md](./LIVING_EXPENSES_DETAILED.md)
- [Adding Liabilities](#liabilities) → [LIABILITIES_DETAILED.md](./LIABILITIES_DETAILED.md)
- [Creating Notes](#notes-section) → Planned: NOTES_DETAILED.md
- [Uploading Files](#attachments-section) → Planned: ATTACHMENTS_DETAILED.md

**By Automation Need**:
- [All Selectors Quick Reference](#quick-selector-reference)
- [Timing Requirements](#timing-requirements)
- [Dropdown Options](#all-dropdown-fields-with-options)
- [Pattern Implementation Status](#pattern-validation)

---

## 📋 Table of Contents

1. [Universal Browser Agent Integration](#universal-browser-agent-integration)
2. [All Dropdown Fields with Options](#all-dropdown-fields-with-options)
3. [Section Breakdowns](#section-breakdowns)
4. [Excel Column Mapping](#excel-column-mapping)
5. [Pattern Validation](#pattern-validation)
6. [Quick Selector Reference](#quick-selector-reference)
7. [Validated Workflows](#validated-workflows)
8. [Implementation Roadmap](#implementation-roadmap)
9. [Critical Timing Requirements](#timing-requirements)

---

## 🔗 Universal Browser Agent Integration

### Current Coverage (73 patterns across 13 sequences)

| Sequence | Patterns | Status | Knowledge Base Match |
|----------|----------|--------|---------------------|
| **authentication** | 1 | ✅ Active | Validated |
| **navigate_to_crm** | 1 | ✅ Active | Validated |
| **create_opportunity** | 1 | ✅ Active | Validated (#transactionType) |
| **fill_opportunity_form** | 25 | ✅ Active | Validated (agent, lender, tranxType) |
| **financials_navigation** | 1 | ✅ Active | Tab validated (#financials) |
| **living_expenses** | 2 | ✅ Active | Validated (#frequency dropdown) |
| **other_assets** | 3 | ✅ Active | Validated (asset buttons) |
| **liabilities** | 8 | ✅ Active | Validated (#name liability type) |
| **employment** | 2 | ✅ Active | Validated (#employment tab) |
| **incomes** | 4 | ✅ Active | Validated (#type dropdown) |
| **real_estate_assets** | 23 | ✅ Active | Validated (propertyType, propertyStatus, etc.) |
| **workflow_completion** | 1 | ✅ Active | N/A (wait pattern) |

### Not Yet Implemented (From Knowledge Base)

| Section | Elements | Priority | Complexity |
|---------|----------|----------|------------|
| **Notes** | 5 | HIGH | Medium (modal + rich text) |
| **Attachments** | 1 | MEDIUM | Low (file upload) |
| **Questionnaires** | 1 | MEDIUM | High (AG-Grid) |
| **BID & NCCP** | 3 | LOW | Low (3 buttons) |

---

## 🎯 All Dropdown Fields with Options

### ✅ VALIDATED - Currently Used in Patterns

#### **1. Lender** (54 options) ✅
**Selector**: `#lender`
**Section**: Details (Opportunity Form)
**Excel Column**: C23 (broker-info_vertical_standardized.xlsx)
**Pattern Type**: excel_dropdown
**Current Implementation**: Step 23 in fill_opportunity_form sequence

```
Options (54 total):
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

**Validation**: Create `lender_mappings.json` like expense_mappings.json

---

#### **2. Agent** (19 options) ✅
**Selector**: `#agent`
**Section**: Details (Opportunity Form)
**Excel Column**: C18 (broker-info_vertical_standardized.xlsx)
**Pattern Type**: excel_dropdown
**Current Implementation**: Step 18 in fill_opportunity_form sequence

```
Options:
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
14. Nicholas OSullivan
15. Oliver Studdy
16. Reuben Way
17. Thomas Dunkley
18. Timothy Perry
19. Tristan Cleggett
```

**Status**: ✅ Currently working in patterns

---

#### **3. Transaction Type (tranxType)** (6 options) ✅
**Selector**: `#tranxType`
**Section**: Details (Opportunity Form)
**Excel Column**: C24 (broker-info_vertical_standardized.xlsx)
**Pattern Type**: excel_dropdown
**Current Implementation**: Step 24 in fill_opportunity_form sequence

```
Options:
1. FHO
2. Pre-Approval
3. Purchase
4. Refinance
5. Top up
6. Variation
```

**Status**: ✅ Currently working in patterns

---

#### **4. Property Type** (63 options) ✅
**Selector**: `#propertyType`
**Section**: Financials → Real Estate Assets
**Excel Column**: Real estate section (rows 195+)
**Pattern Type**: excel_dropdown
**Current Implementation**: real_estate_assets sequence

```
Options (63 total):
1.  Apartment/Unit/Flat
2.  Bedsitter Bachelor
3.  Boarding House
4.  Combi Shop Residence
5.  Commercial
6.  Company Title Unit
7.  Converted Commercial Property
8.  Converted Industrial Property
9.  Converted Motel Units
10. Converted Property
11. Display Home
12. Duplex
13. Fully Detached House
14. Govt Rental Guarantee
15. Hobby Farm
16. Holiday Home
17. Holiday Rental
18. Industrial
19. Inner City Apartment
20. Kit Home
21. Licenced Builder House Construction
22. Luxury House
23. Luxury Other
24. Multiple On Title
25. New Strata Title Unit
26. Nursing Home
27. Owner Builder House Construction
28. Property Development
29. Relocatable Home
30. Rental Guarantee
31. Resort Unit
32. Retirement Unit
33. Semi Detached House
34. Serviced Apt
35. Single Bedroom Less 50m2
36. Snowlease
37. Strata Title Unit
38. Student Accommodation
39. Studio Warehouse Apt
40. Terrace
41. Timeshare
42. Townhouse
43. Transportable Home
44. Unit Student Accom
45. Vacant Land
46. Villa
47. Warehouse Conversion
48. Prof Chambers
49. Offices
50. Factory
51. Warehouse
52. Retirement Village
53. Non Specialised Commercial
54. Residential Commercial
55. Non Specialised Industrial
56. Light Industrial
57. 8 Hectares Or Less
58. Over 8 Less Than 40 Hectares
59. Over 40 Hectares
60. Other (multiple categories)
```

**Status**: ✅ Currently working in real_estate_assets sequence

---

#### **5. Payment Frequency** (4 options) ✅
**Selector**: `#frequency`
**Section**: Financials → Living Expenses
**Excel Column**: Expense frequency rows (60, 63, 66, etc.)
**Pattern Type**: excel_dropdown
**Current Implementation**: living_expenses sequence

```
Options:
1. Annual
2. Monthly
3. Fortnightly
4. Weekly
```

**⚠️ Critical**: 40+ second timeout required for page load (from recording analysis)
**Categories**: 22 expense types available (Childcare, Transport, Groceries, etc.)
**Pattern**: Multi-select filter → form auto-population
**Status**: ✅ Currently working in living_expenses sequence

**📚 Deep Dive**: [LIVING_EXPENSES_DETAILED.md](./LIVING_EXPENSES_DETAILED.md)

---

#### **6. Liability Type** (19 options) ✅
**Selector**: `#name`
**Section**: Financials → Liabilities
**Excel Column**: Liability section (rows 100+)
**Pattern Type**: excel_dropdown
**Current Implementation**: liabilities sequence (8 patterns)

```
Options:
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

**Additional Fields**: Ownership, Repayment Frequency, Limit/Amount, Repayment
**Pattern**: Similar to Living Expenses but with ownership logic
**Status**: ✅ Currently working in liabilities sequence

**📚 Deep Dive**: [LIABILITIES_DETAILED.md](./LIABILITIES_DETAILED.md)

---

#### **7. Income/Other Type** (5 options) ✅
**Selector**: `#type`
**Section**: Financials → Incomes
**Excel Column**: Income section (rows 155+)
**Pattern Type**: excel_dropdown
**Current Implementation**: incomes sequence (4 patterns)

```
Options:
1. Dividends
2. Family Allowance
3. Maintenance
4. Other
```

**Status**: ✅ Currently working in incomes sequence

---

#### **8. Property Status** (5 options) ✅
**Selector**: `#propertyStatus`
**Section**: Financials → Real Estate Assets
**Excel Column**: Real estate section
**Pattern Type**: excel_dropdown
**Current Implementation**: real_estate_assets sequence

```
Options:
1. New Building
2. To Be Built
3. Established
4. Vacant Land
```

**Status**: ✅ Currently working in real_estate_assets sequence

---

#### **9. Real Estate Zoning** (5 options) ✅
**Selector**: `#realEstateZoning`
**Section**: Financials → Real Estate Assets
**Excel Column**: Real estate section
**Pattern Type**: excel_dropdown
**Current Implementation**: real_estate_assets sequence

```
Options:
1. Residential
2. Commercial
3. Industrial
4. Rural
```

**Status**: ✅ Currently working in real_estate_assets sequence

---

#### **10. Real Estate Purpose** (3 options) ✅
**Selector**: `#realEstatePurpose`
**Section**: Financials → Real Estate Assets
**Excel Column**: Real estate section
**Pattern Type**: excel_dropdown
**Current Implementation**: real_estate_assets sequence

```
Options:
1. Owner Occupied
2. Investment
```

**Status**: ✅ Currently working in real_estate_assets sequence

---

### ⚠️ DOCUMENTED - Not Yet Implemented

#### **11. Transaction Type (Loan Type)** (4 options)
**Selector**: `#transactionType`
**Section**: Dashboard/Initial Selection
**Usage**: Opportunity type selection (Home Loans, Commercial, etc.)
**Priority**: Already handled in create_opportunity sequence

```
Options:
1. Home Loans
2. Commercial Loans
3. Asset Finance
4. Business Loans
```

**Note**: We currently select "Home Loans" in create_opportunity sequence. This dropdown is the initial opportunity type selector.

---

#### **12. Person Responsible** (15 options)
**Selector**: `#personResponsible`
**Section**: Details (Opportunity Form)
**Priority**: MEDIUM - Often auto-filled or optional

```
Options:
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

---

#### **13. Settlement Officer** (15 options)
**Selector**: `#settlementOfficer`
**Section**: Details (Opportunity Form)
**Priority**: MEDIUM - Often same as Person Responsible

```
Options:
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

**Note**: Currently in patterns as broker/admin/supervisor/settlement officer dropdowns

---

#### **14. Property Title Type** (15 options)
**Selector**: `#propertyTitleType`
**Section**: Financials → Real Estate Assets
**Priority**: HIGH - Important for property details

```
Options:
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

**Action**: Add to real_estate_assets sequence

---

#### **15. Loan Priority** (5 options)
**Selector**: `#priority`
**Section**: Financials → Real Estate/Liabilities
**Priority**: MEDIUM

```
Options:
1. First
2. Second
3. Third
4. Fourth
```

---

#### **16. Account Repayment Frequency** (5 options)
**Selector**: `#accountRepaymentFrequency`
**Section**: Financials → Liabilities
**Priority**: MEDIUM

```
Options:
1. Annual
2. Monthly
3. Fortnightly
4. Weekly
```

**Note**: Similar to Payment Frequency (#frequency) but for liabilities

---

#### **17. Valuation Basis** (4 options)
**Selector**: `#valueBasis`
**Section**: Financials → Assets
**Priority**: MEDIUM

```
Options:
1. Applicant Estimate
2. Certified Valuation
3. Actual Value
```

---

#### **18. Note Type** (13 options) ⭐ NEW SECTION
**Selector**: `#noteType`
**Section**: Notes (Not yet implemented)
**Priority**: HIGH - Complete workflow documented

```
Options:
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

**Implementation Needed**: Add Notes sequence with rich text editor

---

#### **19. User ID** (Dynamic) ⭐ NEW SECTION
**Selector**: `#userID`
**Section**: Notes
**Priority**: LOW - Auto-detects logged-in user

```
Format: CA109034:James Larkey (CA number followed by name)
```

---

## 📂 Section Breakdowns

### ✅ **Details Section** (Currently Implemented)

| Element | Type | Selector | Excel Column | Pattern Sequence | Status |
|---------|------|----------|--------------|------------------|--------|
| Agent | select | `#agent` | C18 | fill_opportunity_form | ✅ Active |
| Lender | select | `#lender` | C23 | fill_opportunity_form | ✅ Active |
| Transaction Type | select | `#tranxType` | C24 | fill_opportunity_form | ✅ Active |
| Loan Amount | input | `#loanAmount` | C25 | fill_opportunity_form | ✅ Active |
| Existing Amount | input | `#existingAmountText` | C26 | fill_opportunity_form | ✅ Active |
| Security Value | input | `#securityValueText` | C27 | fill_opportunity_form | ✅ Active |
| Person Responsible | select | `#personResponsible` | - | - | ⚠️ Optional |
| Settlement Officer | select | `#settlementOfficer` | - | - | ⚠️ In patterns |

---

### ✅ **Financials Section** (Partially Implemented)

**Sub-sections:**
- ✅ Living Expenses (2 patterns) → [LIVING_EXPENSES_DETAILED.md](./LIVING_EXPENSES_DETAILED.md)
- ✅ Liabilities (8 patterns) → [LIABILITIES_DETAILED.md](./LIABILITIES_DETAILED.md)
- ✅ Other Assets (3 patterns)
- ✅ Employment (2 patterns)
- ✅ Incomes (4 patterns)
- ✅ Real Estate Assets (23 patterns)

**Dropdowns Currently Used:**
- #frequency (Payment Frequency) - Living Expenses
- #type (Income Type)
- #name (Liability Type)
- #propertyType (63 options)
- #propertyStatus
- #realEstateZoning
- #realEstatePurpose
- #accountRepaymentFrequency - Liabilities

**Missing from Implementation:**
- #propertyTitleType (15 options) - Should add
- #priority (Loan Priority)
- #valueBasis (Asset valuation)

**⚠️ Critical**: Living Expenses requires 40+ second page load timeout

---

### ⭐ **Notes Section** (NOT YET IMPLEMENTED - HIGH PRIORITY)

**Elements (5 total):**

| Element | Type | Selector | Notes | Implementation |
|---------|------|----------|-------|----------------|
| Add Note Button | button | `[data-testid="addNoteToOpportunity"]` | Triggers modal | ❌ Add pattern |
| Note Type | select | `#noteType` | 13 options | ❌ Add dropdown pattern |
| User ID | select | `#userID` | Auto-detects | ⚠️ Optional |
| Rich Text Editor | rich_text | `.fr-element.fr-view` | Froala editor | ❌ Special handler |
| Create Button | button | `[data-testid="createNote"]` | Submit modal | ❌ Add pattern |

**Validated Workflow:**
```
1. Click [data-testid="addNoteToOpportunity"]
2. Wait for modal
3. Select #noteType (optional)
4. Fill .fr-element.fr-view using JavaScript:
   document.querySelector('.fr-element.fr-view').innerHTML = 'Note content'
5. Click [data-testid="createNote"]
6. Wait for modal close
```

**Priority**: HIGH - Common workflow, well-documented

---

### ⭐ **Attachments Section** (NOT YET IMPLEMENTED - MEDIUM PRIORITY)

**Elements (1 total):**

| Element | Type | Selector | Notes | Implementation |
|---------|------|----------|-------|----------------|
| File Upload | input | `#file` | Hidden (display:none) | ❌ Add pattern |

**Validated Workflow:**
```
1. Click #attachments (tab)
2. Wait 2 seconds
3. Click [data-testid="Add"]
4. Send keys to #file (hidden input):
   file_input.send_keys(absolute_path)
```

**Priority**: MEDIUM - Common need, simple implementation

---

### ⭐ **Questionnaires Section** (NOT YET IMPLEMENTED - MEDIUM PRIORITY)

**Elements (1 total):**

| Element | Type | Selector | Notes | Implementation |
|---------|------|----------|-------|----------------|
| Questionnaire Grid | ag_grid | `.ag-cell` | AG-Grid component | ❌ Complex pattern |

**Available Questionnaires:**
- Home Loan - Needs Analysis
- Asset Finance - Needs Analysis
- Personal Loan - Needs Analysis
- Consent to perform a Credit Check

**Validated Workflow:**
```
1. Click #questionnaires (tab)
2. Wait 2 seconds
3. Click [data-testid="Add"]
4. Wait for modal with AG-Grid
5. Click .ag-cell containing questionnaire name
6. Click [data-testid="Choose"]
7. Wait 3 seconds for form
8. Expand sections and fill
```

**Priority**: MEDIUM - Complex but documented

---

### ⭐ **BID & NCCP Section** (NOT YET IMPLEMENTED - LOW PRIORITY)

**Elements (3 total):**

| Element | Type | Selector | Notes | Implementation |
|---------|------|----------|-------|----------------|
| Stage 1 | button | `[data-testid="CREDIT_GUIDE"]` | Credit Guide | ❌ Simple click |
| Stage 2 | button | `[data-testid="PRELIM_ASSESSMENT"]` | Preliminary Assessment | ❌ Simple click |
| Stage 3 | button | `[data-testid="CPD_AND_SUBMISSION"]` | SoRCP and Submission | ❌ Simple click |

**Priority**: LOW - Compliance stages, less common

---

### ✅ **Navigation** (Currently Implemented)

| Tab | Selector | Pattern Sequence | Status |
|-----|----------|------------------|--------|
| Details | `#details` | employment | ✅ Active |
| Financials | `#financials` | financials_navigation | ✅ Active |
| Employment | `#employment` | employment | ✅ Active |
| Incomes | `#incomes` | incomes | ✅ Active |
| Attachments | `#attachments` | - | ❌ Not implemented |
| Questionnaires | `#questionnaires` | - | ❌ Not implemented |
| Notes | `#notes` | - | ❌ Not implemented |
| BID & NCCP | `#newCompliance` | - | ❌ Not implemented |

---

## 📊 Excel Column Mapping

**Excel File**: `broker-info_vertical_standardized.xlsx`

| Excel Row(s) | Field_Name | Selector | Dropdown Options | Pattern Sequence |
|-------------|------------|----------|------------------|------------------|
| C1 | URL | - | - | authentication |
| C2 | logname | #logname | - | authentication |
| C3 | password | #logpw | - | authentication |
| C18 | Agent | #agent | 19 agents | fill_opportunity_form |
| C23 | Lender | #lender | 54 lenders | fill_opportunity_form |
| C24 | Transaction Type | #tranxType | 6 types | fill_opportunity_form |
| C25 | Loan Amount | #loanAmount | - | fill_opportunity_form |
| C26 | Existing Amount | #existingAmountText | - | fill_opportunity_form |
| C27 | Security Value | #securityValueText | - | fill_opportunity_form |
| 60, 63, 66... | Expense Frequency | #frequency | 4 options | living_expenses |
| 100+ | Liability Type | #name | 19 types | liabilities |
| 155+ | Income Type | #type | 5 types | incomes |
| 195+ | Property Type | #propertyType | 63 types | real_estate_assets |
| 195+ | Property Status | #propertyStatus | 5 options | real_estate_assets |
| 195+ | Real Estate Zoning | #realEstateZoning | 5 options | real_estate_assets |
| 195+ | Real Estate Purpose | #realEstatePurpose | 3 options | real_estate_assets |

**Missing from Excel** (Should Add):
- Property Title Type (#propertyTitleType) - 15 options
- Note Type (#noteType) - 13 options
- Valuation Basis (#valueBasis) - 4 options

---

## ✅ Pattern Validation

### Selector Priority (Knowledge Base Recommendation)
1. ✅ **data-testid** (most reliable - never changes)
2. ✅ **ID** (reliable if not UUID)
3. ✅ **Text content** (for buttons)
4. ⚠️ **Class** (less reliable)
5. ⚠️ **XPath** (fallback only)

### Current Pattern Implementation Review

**Using data-testid (BEST)** ✅
- `[data-testid="addNoteToOpportunity"]` (Notes - not yet implemented)
- `[data-testid="createNote"]` (Notes - not yet implemented)
- `[data-testid="Add"]` (Multiple sections)
- `[data-testid="CREDIT_GUIDE"]` (BID & NCCP - not yet implemented)

**Using ID selectors** ✅
- `#logname`, `#logpw` (Authentication)
- `#agent`, `#lender`, `#tranxType` (Dropdowns)
- `#frequency`, `#type`, `#name` (Financials)
- `#propertyType`, `#propertyStatus` (Real Estate)

**Recommendation**: Continue using ID selectors where available. Add data-testid for new sections (Notes, Attachments, Questionnaires).

---

## ⏱️ Critical Timing Requirements {#timing-requirements}

**From Recording Analysis & Automation Testing**

| Section | Timeout Needed | Notes | Source |
|---------|----------------|-------|--------|
| **Living Expenses** | **40+ seconds** | Page load wait - CRITICAL for initial dropdown | Recording analysis (39623ms) |
| **Financials Tab** | 10+ seconds | General financials section load | Pattern testing |
| **Liabilities** | 5-10 seconds | Standard section load | Recording (1m 49s for 3 entries) |
| **Dropdowns** | 2-5 seconds | After clicking dropdown button | User observation |
| **Form Fields** | 1-2 seconds | Individual field interactions | Pattern execution |
| **Multi-entry Workflow** | ~30 sec/category | Living Expenses: 9 categories in 4m 34s | Recording analysis |

### User Workflow Patterns (From Voice Annotations)

**Living Expenses Insights**:
- Users add 9+ expense categories in ~4 minutes
- Incremental amount entry: "3" → "30" → "300" (typing pattern)
- Monthly frequency is default/most common
- Multi-select dropdowns are primary interaction model

**Liabilities Insights**:
- Average ~36 seconds per liability entry
- Ownership field requires explicit selection
- Faster than Living Expenses (no 40s page load)

### Automation Recommendations

```python
# Living Expenses - CRITICAL
WebDriverWait(driver, 40).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '.dropdown-toggle.btn.btn-light.btn-sm'))
)

# Most other sections
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'selector'))
)

# Individual fields
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, 'field'))
)
```

**See also**: [AUTOMATION_QUICK_REFERENCE.md](./AUTOMATION_QUICK_REFERENCE.md) for complete timing guide

---

## 💡 Implementation Roadmap

### Phase 1: Validation & Enhancement (Immediate)

**Tasks:**
1. ✅ Create enhanced knowledge reference (this file)
2. 🔲 Create dropdown mapping files:
   - `lender_mappings.json` (54 lenders)
   - `property_type_mappings.json` (63 types)
   - `liability_type_mappings.json` (19 types)
3. 🔲 Validate all current dropdown patterns against knowledge base
4. 🔲 Add missing dropdowns to real_estate_assets:
   - #propertyTitleType (15 options)
   - #valueBasis (4 options)
5. 🔲 Update Excel with new rows for missing fields

**Time Estimate**: 2-3 hours

---

### Phase 2: Notes Section (High Priority)

**Tasks:**
1. 🔲 Create `notes` pattern sequence
2. 🔲 Add rich text editor handler for Froala
3. 🔲 Implement modal-based workflow:
   - Click `[data-testid="addNoteToOpportunity"]`
   - Wait for modal
   - Fill #noteType dropdown
   - Fill `.fr-element.fr-view` rich text
   - Click `[data-testid="createNote"]`
4. 🔲 Add Excel rows for note data
5. 🔲 Test complete notes workflow

**Time Estimate**: 3-4 hours

---

### Phase 3: Attachments Section (Medium Priority)

**Tasks:**
1. 🔲 Create `attachments` pattern sequence
2. 🔲 Implement file upload handler for hidden input
3. 🔲 Add file path column to Excel
4. 🔲 Test upload workflow

**Time Estimate**: 1-2 hours

---

### Phase 4: Questionnaires (Medium-High Complexity)

**Tasks:**
1. 🔲 Create `questionnaires` pattern sequence
2. 🔲 Implement AG-Grid interaction handler
3. 🔲 Add questionnaire selection logic
4. 🔲 Handle dynamic form filling after questionnaire selection
5. 🔲 Test with "Home Loan - Needs Analysis"

**Time Estimate**: 4-6 hours

---

### Phase 5: BID & NCCP (Low Priority)

**Tasks:**
1. 🔲 Create `compliance` pattern sequence
2. 🔲 Add 3 stage button patterns
3. 🔲 Handle stage progression logic

**Time Estimate**: 1 hour

---

## 🔍 Quick Selector Reference

### High-Priority Selectors (Most Common)

| Field | Selector | Type | Options | Status |
|-------|----------|------|---------|--------|
| **Lender** | `#lender` | select | 54 | ✅ Implemented |
| **Agent** | `#agent` | select | 19 | ✅ Implemented |
| **Property Type** | `#propertyType` | select | 63 | ✅ Implemented |
| **Transaction Type** | `#tranxType` | select | 6 | ✅ Implemented |
| **Liability Type** | `#name` | select | 19 | ✅ Implemented |
| **Payment Frequency** | `#frequency` | select | 4 | ✅ Implemented |
| **Note Type** | `#noteType` | select | 13 | ❌ Not implemented |
| **Add Note** | `[data-testid="addNoteToOpportunity"]` | button | - | ❌ Not implemented |
| **Create Note** | `[data-testid="createNote"]` | button | - | ❌ Not implemented |
| **Rich Text Editor** | `.fr-element.fr-view` | rich_text | - | ❌ Not implemented |

### Tab Navigation

| Tab | Selector | Status |
|-----|----------|--------|
| Details | `#details` | ✅ Implemented |
| Financials | `#financials` | ✅ Implemented |
| Employment | `#employment` | ✅ Implemented |
| Incomes | `#incomes` | ✅ Implemented |
| Attachments | `#attachments` | ❌ Not implemented |
| Questionnaires | `#questionnaires` | ❌ Not implemented |
| Notes | `#notes` | ❌ Not implemented |
| BID & NCCP | `#newCompliance` | ❌ Not implemented |

---

## ✅ Validated Workflows

### **Workflow 1: Add Note** ⭐ NEW

**Status**: ✅ Validated from real workflow (Knowledge Base)
**Priority**: HIGH - Common operation
**Implementation Status**: ❌ Not yet implemented

**Steps**:
1. Click `[data-testid="addNoteToOpportunity"]`
2. Wait for modal to appear
3. Select from `#noteType` (13 options, optional)
4. Select from `#userID` (auto-detects, optional)
5. Fill `.fr-element.fr-view` rich text editor using JavaScript:
   ```javascript
   document.querySelector('.fr-element.fr-view').innerHTML = 'Your note content';
   ```
6. Click `[data-testid="createNote"]`
7. Wait for modal to close

**Pattern Type**: Modal-based with rich text
**Framework**: Froala Editor

---

### **Workflow 2: Upload Files** ⭐ NEW

**Status**: ✅ Validated from real workflow (Knowledge Base)
**Priority**: MEDIUM - Common need
**Implementation Status**: ❌ Not yet implemented

**Steps**:
1. Click `#attachments` tab
2. Wait 2 seconds for tab to load
3. Click `[data-testid="Add"]` button
4. Send file path to hidden input `#file`:
   ```python
   file_input = page.locator("#file")
   file_input.set_input_files(absolute_file_path)
   ```

**Note**: File input has `display:none` but is accessible via Playwright
**Pattern Type**: Hidden file input

---

### **Workflow 3: Complete Questionnaire** ⭐ NEW

**Status**: ✅ Validated from real workflow (Knowledge Base)
**Priority**: MEDIUM - Complex but documented
**Implementation Status**: ❌ Not yet implemented

**Steps**:
1. Click `#questionnaires` tab
2. Wait 2 seconds for tab to load
3. Click `[data-testid="Add"]` button
4. Wait for modal with AG-Grid to appear
5. Click `.ag-cell` containing desired questionnaire name
6. Click `[data-testid="Choose"]` button
7. Wait 3 seconds for questionnaire form to load
8. Expand sections and fill fields

**Available Questionnaires**:
- Home Loan - Needs Analysis
- Asset Finance - Needs Analysis
- Personal Loan - Needs Analysis
- Consent to perform a Credit Check

**Pattern Type**: AG-Grid interaction with dynamic form
**Framework**: AG-Grid

---

### **Workflow 4: Create Opportunity** ✅ CURRENT

**Status**: ✅ Currently implemented and working
**Patterns**: 13 sequences, 73 patterns total

**High-Level Flow**:
1. ✅ Authentication (email verification)
2. ✅ Navigate to CRM
3. ✅ Create opportunity (select "Home Loans")
4. ✅ Fill opportunity form (25 patterns)
5. ✅ Navigate to Financials
6. ✅ Fill living expenses (2 patterns)
7. ✅ Fill other assets (3 patterns)
8. ✅ Fill liabilities (8 patterns)
9. ✅ Fill employment (2 patterns)
10. ✅ Fill incomes (4 patterns)
11. ✅ Fill real estate assets (23 patterns)
12. ✅ Workflow completion wait

**Total Coverage**: 73 patterns across 13 sequences

---

## 💡 Usage Tips

### Selector Priority (From Knowledge Base)
1. **data-testid** (most reliable - never changes)
2. **ID** (reliable if not UUID)
3. **Text content** (for buttons)
4. **Class** (less reliable)
5. **XPath** (fallback only)

### Common Patterns

**Modal-Based Architecture** ⭐
- Elements don't exist until triggered
- Always wait for modal after clicking "Add" buttons
- Elements disappear when modal closes
- Use explicit waits for modal appearance/disappearance

**Dynamic UUIDs** ⚠️
- Avoid selectors with patterns like `btn_xxxxx-xxxx-xxxx`
- These change on every page load
- Prefer data-testid or stable IDs

**Hidden Elements** ℹ️
- File input `#file` has `display:none`
- Still accessible via Playwright `set_input_files()`
- Don't try to click - directly set file path

**Rich Text Editors** ℹ️
- Froala editor uses `.fr-element.fr-view` selector
- Fill using JavaScript: `element.innerHTML = 'content'`
- Alternative: Use editor's API if available

**AG-Grid Components** ℹ️
- Grid cells use `.ag-cell` selector
- Wait for grid to load before interaction
- Use text matching to find specific cells

---

## 📊 Statistics

**Coverage:**
- ✅ **Implemented**: 73 patterns across 13 sequences
- ❌ **Not Implemented**: 4 sections (Notes, Attachments, Questionnaires, BID & NCCP)
- ⚠️ **Partial**: 2 dropdowns missing from Financials (propertyTitleType, valueBasis)

**Dropdowns:**
- ✅ **Validated**: 10 dropdowns (agent, lender, tranxType, propertyType, frequency, type, name, propertyStatus, realEstateZoning, realEstatePurpose)
- ❌ **Missing**: 9 dropdowns (noteType, propertyTitleType, priority, accountRepaymentFrequency, valueBasis, personResponsible, settlementOfficer, transactionType partially, userID)

**Workflows:**
- ✅ **Current**: 1 complete workflow (Create Opportunity with Financials)
- ⭐ **New**: 3 validated workflows (Add Note, Upload Files, Questionnaires)

**Frameworks Detected:**
- Froala Editor (rich text)
- AG-Grid (data grids)
- React-Select (some dropdowns)
- Bootstrap Dropdowns (standard dropdowns)

---

## 🔄 Integration Checklist

### Immediate Actions

- [ ] Copy this file to workflows/connective1/
- [ ] Create lender_mappings.json
- [ ] Create property_type_mappings.json
- [ ] Create liability_type_mappings.json
- [ ] Validate all current dropdown options against knowledge base
- [ ] Add #propertyTitleType to real_estate_assets sequence
- [ ] Add #valueBasis to assets patterns

### Short-Term (Next Sprint)

- [ ] Implement Notes section (5 patterns)
- [ ] Implement Attachments section (1 pattern)
- [ ] Add rich text editor handler
- [ ] Add file upload handler
- [ ] Update Excel with notes/attachments rows
- [ ] Test complete workflows

### Medium-Term

- [ ] Implement Questionnaires section (AG-Grid)
- [ ] Implement BID & NCCP section (3 buttons)
- [ ] Add questionnaire selection logic
- [ ] Test all new sections end-to-end

### Long-Term

- [ ] Full workflow optimization
- [ ] Reduce manual waits
- [ ] Implement smart element detection
- [ ] Add comprehensive error recovery
- [ ] Create workflow variants (different loan types)

---

**This enhanced reference integrates Universal Browser Agent patterns with Connective CRM knowledge for maximum automation effectiveness!**
