# Connective CRM - jlall Complete Recording - Complete Field Reference

**Source**: jlall.json
**Generated**: 2025-10-04
**Recording Duration**: 6m 20s
**Total Events**: 147

---

## Summary

**Total Fields Discovered**: 60

**Field Types**:
- button: 16
- div: 3
- input: 21
- select: 18
- textarea: 2

---

## Field Definitions

### accountRepaymentFrequency

**Core Identifiers**
- **Field Name:** `accountRepaymentFrequency`
- **Selector:** `#accountRepaymentFrequency` [RECOMMENDED] (stable ID)
- **ID:** `accountRepaymentFrequency`

**Type Information**
- **Element Type:** select
- **Input Type:** select-one

**Context**
- **In Form:** Yes
- **Form Action:** https://crm.connective.com.au/#/
- **Form Method:** get
- **Related Fields:** `interestOnlyExpiry`, `fixedRateExpiry`, `loanTermExpiry`, `interestRate`, `accountRepayment`

**Dropdown Options**
- **Total Options:** 4
- **Options:**
  - Annual
  - Fortnightly
  - Monthly
  - Weekly

**Usage Example**
```python
# Select dropdown
from selenium.webdriver.support.ui import Select
accountRepaymentFrequency_dropdown = driver.find_element(By.CSS_SELECTOR, '#accountRepaymentFrequency')
Select(accountRepaymentFrequency_dropdown).select_by_visible_text('Annual')
time.sleep(0.5)
```

**Recorded Values** (from actual usage)
- `monthly`

**Metadata**
- **Interactions Observed:** 2
- **XPath:** `//*[@id="accountRepaymentFrequency"]`

---

### Broker

**Core Identifiers**
- **Field Name:** `agent`
- **Label:** Broker
- **Selector:** `#agent` [RECOMMENDED] (stable ID)
- **ID:** `agent`

**Type Information**
- **Element Type:** select
- **Input Type:** select-one

**Context**
- **In Form:** Yes
- **Form Action:** https://crm.connective.com.au/#/
- **Form Method:** get
- **Related Fields:** `btn_6f1b8cf7-01c7-414c-9739-3076bd539346`, `personActing`, `personResponsible`, `settlementOfficer`, `partnerName`
  - *(6 more...)*

**Dropdown Options**
- **Total Options:** 19
- **Options:**
  - Avril Clutterbuck
  - Benjamin Hawley
  - Benjamin Ringer
  - Corey Wild
  - Dean Joffe
  - Dom Dzakula
  - Elia Theodore
  - Harrison Favetti
  - James Curtis
  - James Ryan
  - Max Connley
  - Maximilian Harris
  - Nicholas OSullivan
  - Oliver Studdy
  - Reuben Way
  - Thomas Dunkley
  - Thomas Hawley
  - Timothy Perry
  - Tristan Cleggett

**Usage Example**
```python
# Select dropdown
from selenium.webdriver.support.ui import Select
agent_dropdown = driver.find_element(By.CSS_SELECTOR, '#agent')
Select(agent_dropdown).select_by_visible_text('Benjamin Hawley')
time.sleep(0.5)
```

**Metadata**
- **Interactions Observed:** 1
- **XPath:** `//*[@id="agent"]`

---

### Campaign

**Core Identifiers**
- **Field Name:** `campaignId`
- **Label:** Campaign
- **Selector:** `#campaignId` [RECOMMENDED] (stable ID)
- **ID:** `campaignId`

**Type Information**
- **Element Type:** select
- **Input Type:** select-one

**Context**
- **In Form:** Yes
- **Form Action:** https://crm.connective.com.au/#/
- **Form Method:** get
- **Related Fields:** `agent`, `btn_6f1b8cf7-01c7-414c-9739-3076bd539346`, `personActing`, `personResponsible`, `settlementOfficer`
  - *(6 more...)*

**Usage Example**
```python
# Select dropdown
from selenium.webdriver.support.ui import Select
campaignId_dropdown = driver.find_element(By.CSS_SELECTOR, '#campaignId')
time.sleep(0.5)
```

**Metadata**
- **Interactions Observed:** 1
- **XPath:** `//*[@id="campaignId"]`

---

### Shared Equally

**Core Identifiers**
- **Field Name:** `frequency`
- **Label:** Shared Equally
- **Selector:** `#frequency` [RECOMMENDED] (stable ID)
- **ID:** `frequency`

**Type Information**
- **Element Type:** select
- **Input Type:** select-one

**Context**
- **In Form:** Yes
- **Form Action:** https://crm.connective.com.au/#/
- **Form Method:** get
- **Related Fields:** `type`, `amount`

**Dropdown Options**
- **Total Options:** 4
- **Options:**
  - Annual
  - Fortnightly
  - Monthly
  - Weekly

**Usage Example**
```python
# Select dropdown
from selenium.webdriver.support.ui import Select
frequency_dropdown = driver.find_element(By.CSS_SELECTOR, '#frequency')
Select(frequency_dropdown).select_by_visible_text('Annual')
time.sleep(0.5)
```

**Recorded Values** (from actual usage)
- `Monthly`

**Metadata**
- **Interactions Observed:** 3
- **XPath:** `//*[@id="frequency"]`

---

### Lender

**Core Identifiers**
- **Field Name:** `lender`
- **Label:** Lender
- **Selector:** `#lender` [RECOMMENDED] (stable ID)
- **ID:** `lender`

**Type Information**
- **Element Type:** select
- **Input Type:** select-one

**Context**
- **In Form:** Yes
- **Form Action:** https://crm.connective.com.au/#/
- **Form Method:** get
- **Related Fields:** `tranxType`, `amountText`, `existingAmountText`, `securityValueText`, `loanValueRatio`
  - *(1 more...)*

**Dropdown Options**
- **Total Options:** 54
- **Options:**
  - AMP
  - ANZ
  - Aussie Bonds
  - Australian Military Bank
  - Auswide Bank
  - Bank SA
  - Bank of China
  - Bank of Melbourne
  - Bank of Queensland
  - Bankwest
  - Better Choice Home Loans
  - Better Mortgage Management
  - Bluebay Home Loans
  - Commonwealth Bank
  - Connective Advance (Thinktank)
  - Connective Bridge (Bridgit)
  - Connective Complete (Connective)
  - Connective Elevate (Bluestone)
  - Connective Essentials (Advantedge)
  - Connective Home Loan Essentials
  - Connective Horizon (Brighten)
  - Connective Reverse (Household Capital)
  - Connective Select (Bendigo Bank)
  - Connective Solutions (Pepper Money)
  - Deposit Assure
  - Deposit Power (Deposit Bonds)
  - Firefighters Mutual Bank
  - Firstmac
  - Gateway Bank
  - Granite Home Loans
  - Health Professionals Bank
  - Heritage Bank
  - HomeStart Finance
  - ING
  - Keystart Home Loans
  - La Trobe Financial
  - ME Bank
  - Macquarie Bank
  - MyState
  - NAB
  - Newcastle Permanent
  - OwnHome
  - P & N Bank
  - Paramount Mortgage Services
  - People's Choice Credit Union
  - Pepper Money
  - RedZed
  - Resimac
  - St George Bank
  - Suncorp Bank
  - Teachers Mutual Bank
  - Ubank
  - UniBank
  - Westpac

**Usage Example**
```python
# Select dropdown
from selenium.webdriver.support.ui import Select
lender_dropdown = driver.find_element(By.CSS_SELECTOR, '#lender')
Select(lender_dropdown).select_by_visible_text('AMP')
time.sleep(0.5)
```

**Metadata**
- **Interactions Observed:** 1
- **XPath:** `//*[@id="lender"]`

---

### Liability Type

**Core Identifiers**
- **Field Name:** `name`
- **Label:** Liability Type
- **Selector:** `[data-testid="asset-type-0"]` [RECOMMENDED] (stable data-testid)
- **ID:** `name`
- **data-testid:** `asset-type-0`

**Type Information**
- **Element Type:** select
- **Input Type:** select-one

**Context**
- **In Form:** Yes
- **Form Action:** https://crm.connective.com.au/#/
- **Form Method:** get
- **Related Fields:** `value`, `valueBasis`, `details`

**Dropdown Options**
- **Total Options:** 35
- **Options:**
  - Boat
  - Business Equity
  - Business Loan
  - Buy Now Pay Later
  - Car Loan
  - Cash Management
  - Charge Over Cash
  - Cheque Account
  - Commercial Bill
  - Credit Card
  - Debenture Charge
  - Gifts
  - Guarantee
  - HECS
  - Hire Purchase
  - Home Contents
  - Investment Savings
  - Lease
  - Life Insurance
  - Line Of Credit
  - Loan As Guarantor
  - Managed Funds
  - Mortgage Loan
  - Motor Vehicle
  - Other
  - Other Loan
  - Outstanding Taxation
  - Overdraft
  - Personal Loan
  - Savings Account
  - Shares
  - Store Card
  - Superannuation
  - Term Deposit
  - Term Loan

**Usage Example**
```python
# Select dropdown
from selenium.webdriver.support.ui import Select
name_dropdown = driver.find_element(By.CSS_SELECTOR, '[data-testid="asset-type-0"]')
Select(name_dropdown).select_by_visible_text('Boat')
time.sleep(0.5)
```

**Metadata**
- **Interactions Observed:** 2
- **XPath:** `//*[@id="name"]`

---

### Supervisor

**Core Identifiers**
- **Field Name:** `personResponsible`
- **Label:** Supervisor
- **Selector:** `#personResponsible` [RECOMMENDED] (stable ID)
- **ID:** `personResponsible`

**Type Information**
- **Element Type:** select
- **Input Type:** select-one

**Context**
- **In Form:** Yes
- **Form Action:** https://crm.connective.com.au/#/
- **Form Method:** get
- **Related Fields:** `agent`, `btn_6f1b8cf7-01c7-414c-9739-3076bd539346`, `personActing`, `settlementOfficer`, `partnerName`
  - *(6 more...)*

**Dropdown Options**
- **Total Options:** 15
- **Options:**
  - Benjamin Hawley
  - Cat Manipol
  - Christina Phan
  - Genie Nguyen
  - Isabelle Dib
  - James Larkey
  - Jay Huang
  - Lyka Garcia
  - Madeleine Konstan
  - Madeline Owees
  - Meg Robinson
  - Pra Mansour
  - Romer Andrews
  - Select Other...
  - Thomas Hawley

**Usage Example**
```python
# Select dropdown
from selenium.webdriver.support.ui import Select
personResponsible_dropdown = driver.find_element(By.CSS_SELECTOR, '#personResponsible')
Select(personResponsible_dropdown).select_by_visible_text('Benjamin Hawley')
time.sleep(0.5)
```

**Metadata**
- **Interactions Observed:** 1
- **XPath:** `//*[@id="personResponsible"]`

---

### Priority

**Core Identifiers**
- **Field Name:** `priority`
- **Label:** Priority
- **Selector:** `#priority` [RECOMMENDED] (stable ID)
- **ID:** `priority`

**Type Information**
- **Element Type:** select
- **Input Type:** select-one

**Context**
- **In Form:** Yes
- **Form Action:** https://crm.connective.com.au/#/
- **Form Method:** get
- **Related Fields:** `institution`, `accountName`, `accountBSB`, `accountNumber`

**Dropdown Options**
- **Total Options:** 5
- **Options:**
  - <Clear Priority>
  - First
  - Fourth
  - Second
  - Third

**Usage Example**
```python
# Select dropdown
from selenium.webdriver.support.ui import Select
priority_dropdown = driver.find_element(By.CSS_SELECTOR, '#priority')
Select(priority_dropdown).select_by_visible_text('<Clear Priority>')
time.sleep(0.5)
```

**Recorded Values** (from actual usage)
- `1`

**Metadata**
- **Interactions Observed:** 1
- **XPath:** `//*[@id="priority"]`

---

### Status

**Core Identifiers**
- **Field Name:** `propertyStatus`
- **Label:** Status
- **Selector:** `#propertyStatus` [RECOMMENDED] (stable ID)
- **ID:** `propertyStatus`

**Type Information**
- **Element Type:** select
- **Input Type:** select-one

**Context**
- **In Form:** Yes
- **Form Action:** https://crm.connective.com.au/#/
- **Form Method:** get
- **Related Fields:** `propertyType`, `propertyTitleType`, `realEstateZoning`, `dateOfPurchase`

**Dropdown Options**
- **Total Options:** 4
- **Options:**
  - Established
  - New Building
  - To Be Built
  - Vacant Land

**Usage Example**
```python
# Select dropdown
from selenium.webdriver.support.ui import Select
propertyStatus_dropdown = driver.find_element(By.CSS_SELECTOR, '#propertyStatus')
Select(propertyStatus_dropdown).select_by_visible_text('New Building')
time.sleep(0.5)
```

**Metadata**
- **Interactions Observed:** 1
- **XPath:** `//*[@id="propertyStatus"]`

---

### Title Type

**Core Identifiers**
- **Field Name:** `propertyTitleType`
- **Label:** Title Type
- **Selector:** `#propertyTitleType` [RECOMMENDED] (stable ID)
- **ID:** `propertyTitleType`

**Type Information**
- **Element Type:** select
- **Input Type:** select-one

**Context**
- **In Form:** Yes
- **Form Action:** https://crm.connective.com.au/#/
- **Form Method:** get
- **Related Fields:** `propertyType`, `propertyStatus`, `realEstateZoning`, `dateOfPurchase`

**Dropdown Options**
- **Total Options:** 14
- **Options:**
  - Community Title
  - Company Title
  - Crown Land
  - Crown Lease
  - Freehold
  - Group Titles Plan
  - Leasehold
  - Moiety Title
  - None
  - Other Title
  - Purple Title
  - Strata Title
  - Stratum Title
  - Unit Title

**Usage Example**
```python
# Select dropdown
from selenium.webdriver.support.ui import Select
propertyTitleType_dropdown = driver.find_element(By.CSS_SELECTOR, '#propertyTitleType')
Select(propertyTitleType_dropdown).select_by_visible_text('Community Title')
time.sleep(0.5)
```

**Metadata**
- **Interactions Observed:** 1
- **XPath:** `//*[@id="propertyTitleType"]`

---

### Property Type

**Core Identifiers**
- **Field Name:** `propertyType`
- **Label:** Property Type
- **Selector:** `#propertyType` [RECOMMENDED] (stable ID)
- **ID:** `propertyType`

**Type Information**
- **Element Type:** select
- **Input Type:** select-one

**Context**
- **In Form:** Yes
- **Form Action:** https://crm.connective.com.au/#/
- **Form Method:** get
- **Related Fields:** `propertyTitleType`, `propertyStatus`, `realEstateZoning`, `dateOfPurchase`

**Dropdown Options**
- **Total Options:** 60
- **Options:**
  - 8 Hectares Or Less
  - Apartment/Unit/Flat
  - Bedsitter Bachelor
  - Boarding House
  - Combi Shop Residence
  - Commercial
  - Company Title Unit
  - Converted Commercial Property
  - Converted Industrial Property
  - Converted Motel Units
  - Converted Property
  - Display Home
  - Duplex
  - Factory
  - Fully Detached House
  - Govt Rental Guarantee
  - Hobby Farm
  - Holiday Home
  - Holiday Rental
  - Industrial
  - Inner City Apartment
  - Kit Home
  - Licenced Builder House Construction
  - Light Industrial
  - Luxury House
  - Luxury Other
  - Multiple On Title
  - New Strata Title Unit
  - Non Specialised Commercial
  - Non Specialised Industrial
  - Nursing Home
  - Offices
  - Other
  - Over 40 Hectares
  - Over 8 Less Than 40 Hectares
  - Owner Builder House Construction
  - Prof Chambers
  - Property Development
  - Relocatable Home
  - Rental Guarantee
  - Residential Commercial
  - Resort Unit
  - Retirement Unit
  - Retirement Village
  - Semi Detached House
  - Serviced Apt
  - Single Bedroom Less 50m2
  - Snowlease
  - Strata Title Unit
  - Student Accommodation
  - Studio Warehouse Apt
  - Terrace
  - Timeshare
  - Townhouse
  - TransportableHome
  - Unit Student Accom
  - Vacant Land
  - Villa
  - Warehouse
  - Warehouse Conversion

**Usage Example**
```python
# Select dropdown
from selenium.webdriver.support.ui import Select
propertyType_dropdown = driver.find_element(By.CSS_SELECTOR, '#propertyType')
Select(propertyType_dropdown).select_by_visible_text('Apartment/Unit/Flat')
time.sleep(0.5)
```

**Metadata**
- **Interactions Observed:** 1
- **XPath:** `//*[@id="propertyType"]`

---

### Primary Purpose

**Core Identifiers**
- **Field Name:** `realEstatePurpose`
- **Label:** Primary Purpose
- **Selector:** `#realEstatePurpose` [RECOMMENDED] (stable ID)
- **ID:** `realEstatePurpose`

**Type Information**
- **Element Type:** select
- **Input Type:** select-one

**Context**
- **In Form:** Yes
- **Form Action:** https://crm.connective.com.au/#/
- **Form Method:** get
- **Related Fields:** `value`, `valueBasis`, `realEstateUseAsSecurity`, `realEstateToBePurchased`

**Dropdown Options**
- **Total Options:** 2
- **Options:**
  - Investment
  - Owner Occupied

**Usage Example**
```python
# Select dropdown
from selenium.webdriver.support.ui import Select
realEstatePurpose_dropdown = driver.find_element(By.CSS_SELECTOR, '#realEstatePurpose')
Select(realEstatePurpose_dropdown).select_by_visible_text('Owner Occupied')
time.sleep(0.5)
```

**Recorded Values** (from actual usage)
- `Owner Occupied`

**Metadata**
- **Interactions Observed:** 1
- **XPath:** `//*[@id="realEstatePurpose"]`

---

### Zoning

**Core Identifiers**
- **Field Name:** `realEstateZoning`
- **Label:** Zoning
- **Selector:** `#realEstateZoning` [RECOMMENDED] (stable ID)
- **ID:** `realEstateZoning`

**Type Information**
- **Element Type:** select
- **Input Type:** select-one

**Context**
- **In Form:** Yes
- **Form Action:** https://crm.connective.com.au/#/
- **Form Method:** get
- **Related Fields:** `propertyType`, `propertyTitleType`, `propertyStatus`, `dateOfPurchase`

**Dropdown Options**
- **Total Options:** 4
- **Options:**
  - Commercial
  - Industrial
  - Residential
  - Rural

**Usage Example**
```python
# Select dropdown
from selenium.webdriver.support.ui import Select
realEstateZoning_dropdown = driver.find_element(By.CSS_SELECTOR, '#realEstateZoning')
Select(realEstateZoning_dropdown).select_by_visible_text('Residential')
time.sleep(0.5)
```

**Metadata**
- **Interactions Observed:** 1
- **XPath:** `//*[@id="realEstateZoning"]`

---

### Settlement Officer

**Core Identifiers**
- **Field Name:** `settlementOfficer`
- **Label:** Settlement Officer
- **Selector:** `#settlementOfficer` [RECOMMENDED] (stable ID)
- **ID:** `settlementOfficer`

**Type Information**
- **Element Type:** select
- **Input Type:** select-one

**Context**
- **In Form:** Yes
- **Form Action:** https://crm.connective.com.au/#/
- **Form Method:** get
- **Related Fields:** `agent`, `btn_6f1b8cf7-01c7-414c-9739-3076bd539346`, `personActing`, `personResponsible`, `partnerName`
  - *(6 more...)*

**Dropdown Options**
- **Total Options:** 15
- **Options:**
  - Benjamin Hawley
  - Cat Manipol
  - Christina Phan
  - Genie Nguyen
  - Isabelle Dib
  - James Larkey
  - Jay Huang
  - Lyka Garcia
  - Madeleine Konstan
  - Madeline Owees
  - Meg Robinson
  - Pra Mansour
  - Romer Andrews
  - Select Other...
  - Thomas Hawley

**Usage Example**
```python
# Select dropdown
from selenium.webdriver.support.ui import Select
settlementOfficer_dropdown = driver.find_element(By.CSS_SELECTOR, '#settlementOfficer')
Select(settlementOfficer_dropdown).select_by_visible_text('Benjamin Hawley')
time.sleep(0.5)
```

**Metadata**
- **Interactions Observed:** 1
- **XPath:** `//*[@id="settlementOfficer"]`

---

### Opportunity Type

**Core Identifiers**
- **Field Name:** `transactionType`
- **Label:** Opportunity Type
- **Selector:** `#transactionType` [RECOMMENDED] (stable ID)
- **ID:** `transactionType`

**Type Information**
- **Element Type:** select
- **Input Type:** select-one

**Context**
- **In Form:** Yes
- **Form Action:** https://crm.connective.com.au/#/
- **Form Method:** get
- **Related Fields:** `agent`, `btn_6f1b8cf7-01c7-414c-9739-3076bd539346`, `personActing`, `personResponsible`, `settlementOfficer`
  - *(6 more...)*

**Dropdown Options**
- **Total Options:** 4
- **Options:**
  - Asset Finance
  - Business Loans
  - Commercial Loans
  - Home Loans

**Usage Example**
```python
# Select dropdown
from selenium.webdriver.support.ui import Select
transactionType_dropdown = driver.find_element(By.CSS_SELECTOR, '#transactionType')
Select(transactionType_dropdown).select_by_visible_text('Home Loans')
time.sleep(0.5)
```

**Recorded Values** (from actual usage)
- `Loan`

**Metadata**
- **Interactions Observed:** 1
- **XPath:** `//*[@id="transactionType"]`

---

### Transaction Type

**Core Identifiers**
- **Field Name:** `tranxType`
- **Label:** Transaction Type
- **Selector:** `#tranxType` [RECOMMENDED] (stable ID)
- **ID:** `tranxType`

**Type Information**
- **Element Type:** select
- **Input Type:** select-one

**Context**
- **In Form:** Yes
- **Form Action:** https://crm.connective.com.au/#/
- **Form Method:** get
- **Related Fields:** `lender`, `amountText`, `existingAmountText`, `securityValueText`, `loanValueRatio`
  - *(1 more...)*

**Dropdown Options**
- **Total Options:** 6
- **Options:**
  - FHO
  - Pre-Approval
  - Purchase
  - Refinance
  - Top up
  - Variation

**Usage Example**
```python
# Select dropdown
from selenium.webdriver.support.ui import Select
tranxType_dropdown = driver.find_element(By.CSS_SELECTOR, '#tranxType')
Select(tranxType_dropdown).select_by_visible_text('FHO')
time.sleep(0.5)
```

**Metadata**
- **Interactions Observed:** 1
- **XPath:** `//*[@id="tranxType"]`

---

### Shared Equally

**Core Identifiers**
- **Field Name:** `type`
- **Label:** Shared Equally
- **Selector:** `#type` [RECOMMENDED] (stable ID)
- **ID:** `type`
- **data-testid:** `income-type-a381afc0-a0dc-11f0-a005-331d76b402cb` [WARNING] (contains UUID - unstable)

**Type Information**
- **Element Type:** select
- **Input Type:** select-one

**Context**
- **In Form:** Yes
- **Form Action:** https://crm.connective.com.au/#/
- **Form Method:** get
- **Related Fields:** `frequency`, `amount`

**Dropdown Options**
- **Total Options:** 25
- **Options:**
  - Board
  - Child & Spouse Maintenance
  - Childcare
  - Clothing & Personal Care
  - Dividends
  - Family Allowance
  - General Insurance
  - Groceries
  - Higher Education & Vocational Training
  - Investment Property Costs
  - Maintenance
  - Medical & Health
  - O/Occ Strata, Body Corporate, Land Tax
  - Other
  - Other Insurances
  - Other Regular and Recurring Expenses
  - Personal Insurance
  - Primary Residence Costs
  - Private & Non-Government Education
  - Public or Government Primary & Secondary Education
  - Recreation & Entertainment
  - Rent
  - Secondary Residence & Holiday Home Costs
  - Telephone, Internet, Pay TV & Media Streaming Subscriptions
  - Transport

**Usage Example**
```python
# Select dropdown
from selenium.webdriver.support.ui import Select
type_dropdown = driver.find_element(By.CSS_SELECTOR, '#type')
Select(type_dropdown).select_by_visible_text('Childcare')
time.sleep(0.5)
```

**Recorded Values** (from actual usage)
- `Child & Spouse Maintenance`

**Metadata**
- **Interactions Observed:** 2
- **XPath:** `//*[@id="type"]`

---

### valueBasis

**Core Identifiers**
- **Field Name:** `valueBasis`
- **Selector:** `#valueBasis` [RECOMMENDED] (stable ID)
- **ID:** `valueBasis`

**Type Information**
- **Element Type:** select
- **Input Type:** select-one

**Context**
- **In Form:** Yes
- **Form Action:** https://crm.connective.com.au/#/
- **Form Method:** get
- **Related Fields:** `value`, `realEstatePurpose`, `realEstateUseAsSecurity`, `realEstateToBePurchased`, `security_1d822675-a0dc-11f0-9423-005056b5e136_realEstateUseAsSecurity`
  - *(2 more...)*

**Dropdown Options**
- **Total Options:** 3
- **Options:**
  - Actual Value
  - Applicant Estimate
  - Certified Valuation

**Usage Example**
```python
# Select dropdown
from selenium.webdriver.support.ui import Select
valueBasis_dropdown = driver.find_element(By.CSS_SELECTOR, '#valueBasis')
Select(valueBasis_dropdown).select_by_visible_text('Applicant Estimate')
time.sleep(0.5)
```

**Recorded Values** (from actual usage)
- `Applicant Estimate`

**Metadata**
- **Interactions Observed:** 3
- **XPath:** `//*[@id="valueBasis"]`

---

### #root > div > div.w-100.maf-app-container:nth-of-type(3) > div.maf-main-component.overflow-auto.p-0.container-fluid:nth-of-type(2) > div.h-100.d-flex.flex-column > div.wrapper-container:nth-of-type(3) > div.tab-content.h-100 > div.tab-pane.h-100.active > div.h-100.row > div.flex-grow-1.pl-0.w-50.ml-2.mr-1.h-100:nth-of-type(2) > div.h-100 > div.pt-3:nth-of-type(2) > div.col-12.col-wd-11.col-xwd-10 > div.row > div.pl-3.mb-1.col-lg-3 > div.multi-select-filter.ml-1.btn-group.btn-group-sm.show > div.dropdown-menu.show > button.dropdown-item > div.custom-checkbox.custom-control > input.custom-control-input

**Core Identifiers**
- **Field Name:** `#root > div > div.w-100.maf-app-container:nth-of-type(3) > div.maf-main-component.overflow-auto.p-0.container-fluid:nth-of-type(2) > div.h-100.d-flex.flex-column > div.wrapper-container:nth-of-type(3) > div.tab-content.h-100 > div.tab-pane.h-100.active > div.h-100.row > div.flex-grow-1.pl-0.w-50.ml-2.mr-1.h-100:nth-of-type(2) > div.h-100 > div.pt-3:nth-of-type(2) > div.col-12.col-wd-11.col-xwd-10 > div.row > div.pl-3.mb-1.col-lg-3 > div.multi-select-filter.ml-1.btn-group.btn-group-sm.show > div.dropdown-menu.show > button.dropdown-item > div.custom-checkbox.custom-control > input.custom-control-input`
- **Selector:** `#root > div > div.w-100.maf-app-container:nth-of-type(3) > div.maf-main-component.overflow-auto.p-0.container-fluid:nth-of-type(2) > div.h-100.d-flex.flex-column > div.wrapper-container:nth-of-type(3) > div.tab-content.h-100 > div.tab-pane.h-100.active > div.h-100.row > div.flex-grow-1.pl-0.w-50.ml-2.mr-1.h-100:nth-of-type(2) > div.h-100 > div.pt-3:nth-of-type(2) > div.col-12.col-wd-11.col-xwd-10 > div.row > div.pl-3.mb-1.col-lg-3 > div.multi-select-filter.ml-1.btn-group.btn-group-sm.show > div.dropdown-menu.show > button.dropdown-item > div.custom-checkbox.custom-control > input.custom-control-input` [RECOMMENDED] (stable ID)

**Type Information**
- **Element Type:** input
- **Input Type:** checkbox

**Usage Example**
```python
# Input field
#root > div > div.w-100.maf-app-container:nth-of-type(3) > div.maf-main-component.overflow-auto.p-0.container-fluid:nth-of-type(2) > div.h-100.d-flex.flex-column > div.wrapper-container:nth-of-type(3) > div.tab-content.h-100 > div.tab-pane.h-100.active > div.h-100.row > div.flex-grow-1.pl-0.w-50.ml-2.mr-1.h-100:nth-of-type(2) > div.h-100 > div.pt-3:nth-of-type(2) > div.col-12.col-wd-11.col-xwd-10 > div.row > div.pl-3.mb-1.col-lg-3 > div.multi-select-filter.ml-1.btn-group.btn-group-sm.show > div.dropdown-menu.show > button.dropdown-item > div.custom-checkbox.custom-control > input.custom-control-input_field = driver.find_element(By.CSS_SELECTOR, '#root > div > div.w-100.maf-app-container:nth-of-type(3) > div.maf-main-component.overflow-auto.p-0.container-fluid:nth-of-type(2) > div.h-100.d-flex.flex-column > div.wrapper-container:nth-of-type(3) > div.tab-content.h-100 > div.tab-pane.h-100.active > div.h-100.row > div.flex-grow-1.pl-0.w-50.ml-2.mr-1.h-100:nth-of-type(2) > div.h-100 > div.pt-3:nth-of-type(2) > div.col-12.col-wd-11.col-xwd-10 > div.row > div.pl-3.mb-1.col-lg-3 > div.multi-select-filter.ml-1.btn-group.btn-group-sm.show > div.dropdown-menu.show > button.dropdown-item > div.custom-checkbox.custom-control > input.custom-control-input')
#root > div > div.w-100.maf-app-container:nth-of-type(3) > div.maf-main-component.overflow-auto.p-0.container-fluid:nth-of-type(2) > div.h-100.d-flex.flex-column > div.wrapper-container:nth-of-type(3) > div.tab-content.h-100 > div.tab-pane.h-100.active > div.h-100.row > div.flex-grow-1.pl-0.w-50.ml-2.mr-1.h-100:nth-of-type(2) > div.h-100 > div.pt-3:nth-of-type(2) > div.col-12.col-wd-11.col-xwd-10 > div.row > div.pl-3.mb-1.col-lg-3 > div.multi-select-filter.ml-1.btn-group.btn-group-sm.show > div.dropdown-menu.show > button.dropdown-item > div.custom-checkbox.custom-control > input.custom-control-input_field.clear()
#root > div > div.w-100.maf-app-container:nth-of-type(3) > div.maf-main-component.overflow-auto.p-0.container-fluid:nth-of-type(2) > div.h-100.d-flex.flex-column > div.wrapper-container:nth-of-type(3) > div.tab-content.h-100 > div.tab-pane.h-100.active > div.h-100.row > div.flex-grow-1.pl-0.w-50.ml-2.mr-1.h-100:nth-of-type(2) > div.h-100 > div.pt-3:nth-of-type(2) > div.col-12.col-wd-11.col-xwd-10 > div.row > div.pl-3.mb-1.col-lg-3 > div.multi-select-filter.ml-1.btn-group.btn-group-sm.show > div.dropdown-menu.show > button.dropdown-item > div.custom-checkbox.custom-control > input.custom-control-input_field.send_keys('All')
time.sleep(0.5)
```

**Recorded Values** (from actual usage)
- `All`

**Metadata**
- **Interactions Observed:** 2
- **XPath:** `/html[1]/body[1]/div[1]/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]/div[1]/input[1]`

---

### Search for property address...

**Core Identifiers**
- **Field Name:** `.rbt-input-main.form-control.rbt-input.focus.input-sm.form-control-sm`
- **Label:** Search for property address...
- **Selector:** `.rbt-input-main.form-control.rbt-input.focus.input-sm.form-control-sm` [USE WITH CARE] (complex selector)

**Type Information**
- **Element Type:** input
- **Input Type:** text

**Context**
- **In Form:** Yes
- **Form Action:** https://crm.connective.com.au/#/
- **Form Method:** get

**Usage Example**
```python
# Input field
.rbt-input-main.form-control.rbt-input.focus.input-sm.form-control-sm_field = driver.find_element(By.CSS_SELECTOR, '.rbt-input-main.form-control.rbt-input.focus.input-sm.form-control-sm')
.rbt-input-main.form-control.rbt-input.focus.input-sm.form-control-sm_field.clear()
.rbt-input-main.form-control.rbt-input.focus.input-sm.form-control-sm_field.send_keys('value')
time.sleep(0.5)
```

**Metadata**
- **Interactions Observed:** 1
- **XPath:** `/html[1]/body[1]/div[1]/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/table[1]/tbody[1]/tr[2]/td[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/input[1]`

---

### BSB

**Core Identifiers**
- **Field Name:** `accountBSB`
- **Label:** BSB
- **Selector:** `#accountBSB` [RECOMMENDED] (stable ID)
- **ID:** `accountBSB`

**Type Information**
- **Element Type:** input
- **Input Type:** text

**Context**
- **In Form:** Yes
- **Form Action:** https://crm.connective.com.au/#/
- **Form Method:** get
- **Related Fields:** `priority`, `institution`, `accountName`, `accountNumber`

**Validation**
- **Length:** 0 - 15

**Usage Example**
```python
# Input field
accountBSB_field = driver.find_element(By.CSS_SELECTOR, '#accountBSB')
accountBSB_field.clear()
accountBSB_field.send_keys('value')
time.sleep(0.5)
```

**Metadata**
- **Interactions Observed:** 1
- **XPath:** `//*[@id="accountBSB"]`

---

### Clearing from this loan?

**Core Identifiers**
- **Field Name:** `accountClearingFromLoan`
- **Label:** Clearing from this loan?
- **Selector:** `[name="accountClearingFromLoan"]` [ALTERNATIVE] (name attribute)
- **ID:** `cb_clearing_356f9eeb-a0dc-11f0-9423-005056b5e136_accountClearingFromLoan` [WARNING] (contains UUID - unstable)

**Type Information**
- **Element Type:** input
- **Input Type:** checkbox

**Context**
- **In Form:** Yes
- **Form Action:** https://crm.connective.com.au/#/
- **Form Method:** get
- **Related Fields:** `value`, `limit`

**Usage Example**
```python
# Input field
accountClearingFromLoan_field = driver.find_element(By.CSS_SELECTOR, '[name="accountClearingFromLoan"]')
accountClearingFromLoan_field.clear()
accountClearingFromLoan_field.send_keys('on')
time.sleep(0.5)
```

**Recorded Values** (from actual usage)
- `on`

**Metadata**
- **Interactions Observed:** 6
- **XPath:** `//*[@id="cb_clearing_356f9eeb-a0dc-11f0-9423-005056b5e136_accountClearingFromLoan"]`

---

### Account Name

**Core Identifiers**
- **Field Name:** `accountName`
- **Label:** Account Name
- **Selector:** `#accountName` [RECOMMENDED] (stable ID)
- **ID:** `accountName`

**Type Information**
- **Element Type:** input
- **Input Type:** text

**Context**
- **In Form:** Yes
- **Form Action:** https://crm.connective.com.au/#/
- **Form Method:** get
- **Related Fields:** `priority`, `institution`, `accountBSB`, `accountNumber`

**Validation**
- **Length:** 0 - 80

**Usage Example**
```python
# Input field
accountName_field = driver.find_element(By.CSS_SELECTOR, '#accountName')
accountName_field.clear()
accountName_field.send_keys('value')
time.sleep(0.5)
```

**Metadata**
- **Interactions Observed:** 1
- **XPath:** `//*[@id="accountName"]`

---

### Account Number

**Core Identifiers**
- **Field Name:** `accountNumber`
- **Label:** Account Number
- **Selector:** `#accountNumber` [RECOMMENDED] (stable ID)
- **ID:** `accountNumber`

**Type Information**
- **Element Type:** input
- **Input Type:** text

**Context**
- **In Form:** Yes
- **Form Action:** https://crm.connective.com.au/#/
- **Form Method:** get
- **Related Fields:** `priority`, `institution`, `accountName`, `accountBSB`

**Validation**
- **Length:** 0 - 30

**Usage Example**
```python
# Input field
accountNumber_field = driver.find_element(By.CSS_SELECTOR, '#accountNumber')
accountNumber_field.clear()
accountNumber_field.send_keys('value')
time.sleep(0.5)
```

**Metadata**
- **Interactions Observed:** 1
- **XPath:** `//*[@id="accountNumber"]`

---

### Repayments

**Core Identifiers**
- **Field Name:** `accountRepayment`
- **Label:** Repayments
- **Selector:** `#accountRepayment` [RECOMMENDED] (stable ID)
- **ID:** `accountRepayment`

**Type Information**
- **Element Type:** input
- **Input Type:** text

**Context**
- **In Form:** Yes
- **Form Action:** https://crm.connective.com.au/#/
- **Form Method:** get
- **Related Fields:** `interestOnlyExpiry`, `fixedRateExpiry`, `loanTermExpiry`, `interestRate`, `accountRepaymentFrequency`

**Usage Example**
```python
# Input field
accountRepayment_field = driver.find_element(By.CSS_SELECTOR, '#accountRepayment')
accountRepayment_field.clear()
accountRepayment_field.send_keys('value')
time.sleep(0.5)
```

**Metadata**
- **Interactions Observed:** 2
- **XPath:** `//*[@id="accountRepayment"]`

---

### 0.00

**Core Identifiers**
- **Field Name:** `amount`
- **Label:** 0.00
- **Selector:** `#amount` [RECOMMENDED] (stable ID)
- **ID:** `amount`

**Type Information**
- **Element Type:** input
- **Input Type:** text

**Context**
- **In Form:** Yes
- **Form Action:** https://crm.connective.com.au/#/
- **Form Method:** get
- **Related Fields:** `type`, `frequency`

**Usage Example**
```python
# Input field
amount_field = driver.find_element(By.CSS_SELECTOR, '#amount')
amount_field.clear()
amount_field.send_keys('value')
time.sleep(0.5)
```

**Metadata**
- **Interactions Observed:** 4
- **XPath:** `//*[@id="amount"]`

---

### Loan Amount

**Core Identifiers**
- **Field Name:** `amountText`
- **Label:** Loan Amount
- **Selector:** `#loanAmount` [RECOMMENDED] (stable ID)
- **ID:** `loanAmount`

**Type Information**
- **Element Type:** input
- **Input Type:** text

**Context**
- **In Form:** Yes
- **Form Action:** https://crm.connective.com.au/#/
- **Form Method:** get
- **Related Fields:** `lender`, `tranxType`, `existingAmountText`, `securityValueText`, `loanValueRatio`
  - *(1 more...)*

**Usage Example**
```python
# Input field
amountText_field = driver.find_element(By.CSS_SELECTOR, '#loanAmount')
amountText_field.clear()
amountText_field.send_keys('value')
time.sleep(0.5)
```

**Metadata**
- **Interactions Observed:** 1
- **XPath:** `//*[@id="loanAmount"]`

---

### Loan Term Expiry

**Core Identifiers**
- **Field Name:** `dateOfPurchase`
- **Label:** Loan Term Expiry
- **Selector:** `.form-control.form-control-sm.react-datepicker-ignore-onclickoutside` [USE WITH CARE] (complex selector)

**Type Information**
- **Element Type:** input
- **Input Type:** text

**Context**
- **In Form:** Yes
- **Form Action:** https://crm.connective.com.au/#/
- **Form Method:** get
- **Related Fields:** `propertyType`, `propertyTitleType`, `propertyStatus`, `realEstateZoning`, `interestOnlyExpiry`
  - *(5 more...)*

**Usage Example**
```python
# Input field
dateOfPurchase_field = driver.find_element(By.CSS_SELECTOR, '.form-control.form-control-sm.react-datepicker-ignore-onclickoutside')
dateOfPurchase_field.clear()
dateOfPurchase_field.send_keys('value')
time.sleep(0.5)
```

**Metadata**
- **Interactions Observed:** 4
- **XPath:** `/html[1]/body[1]/div[1]/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/table[1]/tbody[1]/tr[2]/td[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/div[1]/div[5]/div[1]/div[1]/div[1]/input[1]`

---

### Details

**Core Identifiers**
- **Field Name:** `details`
- **Label:** Details
- **Selector:** `#details` [RECOMMENDED] (stable ID)
- **ID:** `details`

**Type Information**
- **Element Type:** textarea
- **Input Type:** textarea

**Context**
- **In Form:** Yes
- **Form Action:** https://crm.connective.com.au/#/
- **Form Method:** get
- **Related Fields:** `name`

**Validation**
- **Length:** 0 - 164

**Usage Example**
```python
```

**Metadata**
- **Interactions Observed:** 1
- **XPath:** `//*[@id="details"]`

---

### Existing Amount

**Core Identifiers**
- **Field Name:** `existingAmountText`
- **Label:** Existing Amount
- **Selector:** `#existingAmountText` [RECOMMENDED] (stable ID)
- **ID:** `existingAmountText`

**Type Information**
- **Element Type:** input
- **Input Type:** text

**Context**
- **In Form:** Yes
- **Form Action:** https://crm.connective.com.au/#/
- **Form Method:** get
- **Related Fields:** `lender`, `tranxType`, `amountText`, `securityValueText`, `loanValueRatio`
  - *(1 more...)*

**Usage Example**
```python
# Input field
existingAmountText_field = driver.find_element(By.CSS_SELECTOR, '#existingAmountText')
existingAmountText_field.clear()
existingAmountText_field.send_keys('value')
time.sleep(0.5)
```

**Metadata**
- **Interactions Observed:** 1
- **XPath:** `//*[@id="existingAmountText"]`

---

### Creditor

**Core Identifiers**
- **Field Name:** `institution`
- **Label:** Creditor
- **Selector:** `#institution` [RECOMMENDED] (stable ID)
- **ID:** `institution`

**Type Information**
- **Element Type:** input
- **Input Type:** text

**Context**
- **In Form:** Yes
- **Form Action:** https://crm.connective.com.au/#/
- **Form Method:** get
- **Related Fields:** `priority`, `accountName`, `accountBSB`, `accountNumber`

**Validation**
- **Length:** 0 - 44

**Usage Example**
```python
# Input field
institution_field = driver.find_element(By.CSS_SELECTOR, '#institution')
institution_field.clear()
institution_field.send_keys('value')
time.sleep(0.5)
```

**Metadata**
- **Interactions Observed:** 1
- **XPath:** `//*[@id="institution"]`

---

### IO Expiry

**Core Identifiers**
- **Field Name:** `interestOnlyExpiry`
- **Label:** IO Expiry
- **Selector:** `#root > div > div.w-100.maf-app-container:nth-of-type(3) > div.maf-main-component.overflow-auto.p-0.container-fluid:nth-of-type(2) > div.h-100.d-flex.flex-column > div.wrapper-container:nth-of-type(3) > div.tab-content.h-100 > div.tab-pane.h-100.active > div.h-100.row > div.flex-grow-1.pl-0.w-50.ml-2.mr-1.h-100:nth-of-type(2) > div.h-100 > div.pt-3:nth-of-type(2) > div.col-lg-11.col-xwd-9 > div:nth-of-type(2) > table.mt-3.col-12 > tbody > tr:nth-of-type(2) > td.RealEstateComponentV2_bordered__2pwX2 > div.RealEstateComponentV2_detailsContainer__2fAhh.col > div.row > div.pt-1.col-lg-12:nth-of-type(2) > div.h-100.mb-4 > div.ml-2.MortgageDetails_relative__1pEAp:nth-of-type(2) > div.mt-3.row:nth-of-type(2) > div.col-md-4:nth-of-type(2) > form > div.row.form-group > div.col-lg-7 > div.row > div.col-sm-12 > div.react-datepicker-wrapper > div.react-datepicker__input-container > input.form-control.form-control-sm` [RECOMMENDED] (stable ID)

**Type Information**
- **Element Type:** input
- **Input Type:** text

**Context**
- **In Form:** Yes
- **Form Action:** https://crm.connective.com.au/#/
- **Form Method:** get
- **Related Fields:** `fixedRateExpiry`, `loanTermExpiry`, `interestRate`, `accountRepayment`, `accountRepaymentFrequency`

**Usage Example**
```python
# Input field
interestOnlyExpiry_field = driver.find_element(By.CSS_SELECTOR, '#root > div > div.w-100.maf-app-container:nth-of-type(3) > div.maf-main-component.overflow-auto.p-0.container-fluid:nth-of-type(2) > div.h-100.d-flex.flex-column > div.wrapper-container:nth-of-type(3) > div.tab-content.h-100 > div.tab-pane.h-100.active > div.h-100.row > div.flex-grow-1.pl-0.w-50.ml-2.mr-1.h-100:nth-of-type(2) > div.h-100 > div.pt-3:nth-of-type(2) > div.col-lg-11.col-xwd-9 > div:nth-of-type(2) > table.mt-3.col-12 > tbody > tr:nth-of-type(2) > td.RealEstateComponentV2_bordered__2pwX2 > div.RealEstateComponentV2_detailsContainer__2fAhh.col > div.row > div.pt-1.col-lg-12:nth-of-type(2) > div.h-100.mb-4 > div.ml-2.MortgageDetails_relative__1pEAp:nth-of-type(2) > div.mt-3.row:nth-of-type(2) > div.col-md-4:nth-of-type(2) > form > div.row.form-group > div.col-lg-7 > div.row > div.col-sm-12 > div.react-datepicker-wrapper > div.react-datepicker__input-container > input.form-control.form-control-sm')
interestOnlyExpiry_field.clear()
interestOnlyExpiry_field.send_keys('value')
time.sleep(0.5)
```

**Metadata**
- **Interactions Observed:** 1
- **XPath:** `/html[1]/body[1]/div[1]/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/table[1]/tbody[1]/tr[2]/td[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]`

---

### Interest Rate

**Core Identifiers**
- **Field Name:** `interestRate`
- **Label:** Interest Rate
- **Selector:** `#interestRate` [RECOMMENDED] (stable ID)
- **ID:** `interestRate`

**Type Information**
- **Element Type:** input
- **Input Type:** text

**Context**
- **In Form:** Yes
- **Form Action:** https://crm.connective.com.au/#/
- **Form Method:** get
- **Related Fields:** `interestOnlyExpiry`, `fixedRateExpiry`, `loanTermExpiry`, `accountRepayment`, `accountRepaymentFrequency`

**Usage Example**
```python
# Input field
interestRate_field = driver.find_element(By.CSS_SELECTOR, '#interestRate')
interestRate_field.clear()
interestRate_field.send_keys('0')
time.sleep(0.5)
```

**Recorded Values** (from actual usage)
- `0`

**Metadata**
- **Interactions Observed:** 1
- **XPath:** `//*[@id="interestRate"]`

---

### Limit

**Core Identifiers**
- **Field Name:** `limit`
- **Label:** Limit
- **Selector:** `#limit` [RECOMMENDED] (stable ID)
- **ID:** `limit`

**Type Information**
- **Element Type:** input
- **Input Type:** text

**Context**
- **In Form:** Yes
- **Form Action:** https://crm.connective.com.au/#/
- **Form Method:** get
- **Related Fields:** `value`, `accountClearingFromLoan`, `cb_clearing_5ed0827d-a0dc-11f0-9423-005056b5e136_accountClearingFromLoan`

**Usage Example**
```python
# Input field
limit_field = driver.find_element(By.CSS_SELECTOR, '#limit')
limit_field.clear()
limit_field.send_keys('value')
time.sleep(0.5)
```

**Metadata**
- **Interactions Observed:** 2
- **XPath:** `//*[@id="limit"]`

---

### LMI

**Core Identifiers**
- **Field Name:** `lmiText`
- **Label:** LMI
- **Selector:** `#lmiText` [RECOMMENDED] (stable ID)
- **ID:** `lmiText`

**Type Information**
- **Element Type:** input
- **Input Type:** text

**Context**
- **In Form:** Yes
- **Form Action:** https://crm.connective.com.au/#/
- **Form Method:** get
- **Related Fields:** `lender`, `tranxType`, `amountText`, `existingAmountText`, `securityValueText`
  - *(1 more...)*

**Usage Example**
```python
# Input field
lmiText_field = driver.find_element(By.CSS_SELECTOR, '#lmiText')
lmiText_field.clear()
lmiText_field.send_keys('value')
time.sleep(0.5)
```

**Metadata**
- **Interactions Observed:** 1
- **XPath:** `//*[@id="lmiText"]`

---

### Categories

**Core Identifiers**
- **Field Name:** `react-select-2-input`
- **Label:** Categories
- **Selector:** `#react-select-2-input` [RECOMMENDED] (stable ID)
- **ID:** `react-select-2-input`

**Type Information**
- **Element Type:** input
- **Input Type:** text

**Context**
- **In Form:** Yes
- **Form Action:** https://crm.connective.com.au/#/
- **Form Method:** get
- **Related Fields:** `agent`, `btn_6f1b8cf7-01c7-414c-9739-3076bd539346`, `personActing`, `personResponsible`, `settlementOfficer`
  - *(6 more...)*

**Usage Example**
```python
# Input field
react-select-2-input_field = driver.find_element(By.CSS_SELECTOR, '#react-select-2-input')
react-select-2-input_field.clear()
react-select-2-input_field.send_keys('value')
time.sleep(0.5)
```

**Metadata**
- **Interactions Observed:** 1
- **XPath:** `//*[@id="react-select-2-input"]`

---

### To be purchased

**Core Identifiers**
- **Field Name:** `realEstateToBePurchased`
- **Label:** To be purchased
- **Selector:** `[name="realEstateToBePurchased"]` [ALTERNATIVE] (name attribute)
- **ID:** `purchased_1d822675-a0dc-11f0-9423-005056b5e136_realEstateToBePurchased` [WARNING] (contains UUID - unstable)

**Type Information**
- **Element Type:** input
- **Input Type:** checkbox

**Context**
- **In Form:** Yes
- **Form Action:** https://crm.connective.com.au/#/
- **Form Method:** get
- **Related Fields:** `value`, `valueBasis`, `realEstatePurpose`, `realEstateUseAsSecurity`, `security_1d822675-a0dc-11f0-9423-005056b5e136_realEstateUseAsSecurity`

**Usage Example**
```python
# Input field
realEstateToBePurchased_field = driver.find_element(By.CSS_SELECTOR, '[name="realEstateToBePurchased"]')
realEstateToBePurchased_field.clear()
realEstateToBePurchased_field.send_keys('on')
time.sleep(0.5)
```

**Recorded Values** (from actual usage)
- `on`

**Metadata**
- **Interactions Observed:** 6
- **XPath:** `//*[@id="purchased_1d822675-a0dc-11f0-9423-005056b5e136_realEstateToBePurchased"]`

---

### Used as security

**Core Identifiers**
- **Field Name:** `realEstateUseAsSecurity`
- **Label:** Used as security
- **Selector:** `[name="realEstateUseAsSecurity"]` [ALTERNATIVE] (name attribute)
- **ID:** `security_1d822675-a0dc-11f0-9423-005056b5e136_realEstateUseAsSecurity` [WARNING] (contains UUID - unstable)

**Type Information**
- **Element Type:** input
- **Input Type:** checkbox

**Context**
- **In Form:** Yes
- **Form Action:** https://crm.connective.com.au/#/
- **Form Method:** get
- **Related Fields:** `value`, `valueBasis`, `realEstatePurpose`, `realEstateToBePurchased`, `purchased_1d822675-a0dc-11f0-9423-005056b5e136_realEstateToBePurchased`

**Usage Example**
```python
# Input field
realEstateUseAsSecurity_field = driver.find_element(By.CSS_SELECTOR, '[name="realEstateUseAsSecurity"]')
realEstateUseAsSecurity_field.clear()
realEstateUseAsSecurity_field.send_keys('on')
time.sleep(0.5)
```

**Recorded Values** (from actual usage)
- `on`

**Metadata**
- **Interactions Observed:** 6
- **XPath:** `//*[@id="security_1d822675-a0dc-11f0-9423-005056b5e136_realEstateUseAsSecurity"]`

---

### Security Value

**Core Identifiers**
- **Field Name:** `securityValueText`
- **Label:** Security Value
- **Selector:** `#securityValueText` [RECOMMENDED] (stable ID)
- **ID:** `securityValueText`

**Type Information**
- **Element Type:** input
- **Input Type:** text

**Context**
- **In Form:** Yes
- **Form Action:** https://crm.connective.com.au/#/
- **Form Method:** get
- **Related Fields:** `lender`, `tranxType`, `amountText`, `existingAmountText`, `loanValueRatio`
  - *(1 more...)*

**Usage Example**
```python
# Input field
securityValueText_field = driver.find_element(By.CSS_SELECTOR, '#securityValueText')
securityValueText_field.clear()
securityValueText_field.send_keys('value')
time.sleep(0.5)
```

**Metadata**
- **Interactions Observed:** 1
- **XPath:** `//*[@id="securityValueText"]`

---

### Status Notes

**Core Identifiers**
- **Field Name:** `sitRep`
- **Label:** Status Notes
- **Selector:** `#sitRep` [RECOMMENDED] (stable ID)
- **ID:** `sitRep`

**Type Information**
- **Element Type:** textarea
- **Input Type:** textarea

**Context**
- **In Form:** Yes
- **Form Action:** https://crm.connective.com.au/#/
- **Form Method:** get

**Usage Example**
```python
```

**Recorded Values** (from actual usage)
- `S`

**Metadata**
- **Interactions Observed:** 2
- **XPath:** `//*[@id="sitRep"]`

---

### Balance

**Core Identifiers**
- **Field Name:** `value`
- **Label:** Balance
- **Selector:** `[data-testid="mortgageBalance"]` [RECOMMENDED] (stable data-testid)
- **ID:** `value`
- **data-testid:** `mortgageBalance`

**Type Information**
- **Element Type:** input
- **Input Type:** text

**Context**
- **In Form:** Yes
- **Form Action:** https://crm.connective.com.au/#/
- **Form Method:** get
- **Related Fields:** `valueBasis`, `realEstatePurpose`, `realEstateUseAsSecurity`, `realEstateToBePurchased`, `limit`
  - *(3 more...)*

**Usage Example**
```python
# Input field
value_field = driver.find_element(By.CSS_SELECTOR, '[data-testid="mortgageBalance"]')
value_field.clear()
value_field.send_keys('value')
time.sleep(0.5)
```

**Metadata**
- **Interactions Observed:** 4
- **XPath:** `//*[@id="value"]`

---

### #root > div > div.w-100.maf-app-container:nth-of-type(3) > div.maf-main-component.overflow-auto.p-0.container-fluid:nth-of-type(2) > div.h-100.d-flex.flex-column > div.wrapper-container:nth-of-type(3) > div.tab-content.h-100 > div.tab-pane.h-100.active > div.h-100.row > div.flex-grow-1.pl-0.w-50.ml-2.mr-1.h-100:nth-of-type(2) > div.h-100 > div.pt-3:nth-of-type(2) > div.col-12.col-wd-11.col-xwd-10 > div.row > div.pl-3.mb-1.col-lg-3 > div.multi-select-filter.ml-1.btn-group.btn-group-sm.show > div.dropdown-menu.show > button.dropdown-item:nth-of-type(2)

**Core Identifiers**
- **Field Name:** `#root > div > div.w-100.maf-app-container:nth-of-type(3) > div.maf-main-component.overflow-auto.p-0.container-fluid:nth-of-type(2) > div.h-100.d-flex.flex-column > div.wrapper-container:nth-of-type(3) > div.tab-content.h-100 > div.tab-pane.h-100.active > div.h-100.row > div.flex-grow-1.pl-0.w-50.ml-2.mr-1.h-100:nth-of-type(2) > div.h-100 > div.pt-3:nth-of-type(2) > div.col-12.col-wd-11.col-xwd-10 > div.row > div.pl-3.mb-1.col-lg-3 > div.multi-select-filter.ml-1.btn-group.btn-group-sm.show > div.dropdown-menu.show > button.dropdown-item:nth-of-type(2)`
- **Selector:** `#root > div > div.w-100.maf-app-container:nth-of-type(3) > div.maf-main-component.overflow-auto.p-0.container-fluid:nth-of-type(2) > div.h-100.d-flex.flex-column > div.wrapper-container:nth-of-type(3) > div.tab-content.h-100 > div.tab-pane.h-100.active > div.h-100.row > div.flex-grow-1.pl-0.w-50.ml-2.mr-1.h-100:nth-of-type(2) > div.h-100 > div.pt-3:nth-of-type(2) > div.col-12.col-wd-11.col-xwd-10 > div.row > div.pl-3.mb-1.col-lg-3 > div.multi-select-filter.ml-1.btn-group.btn-group-sm.show > div.dropdown-menu.show > button.dropdown-item:nth-of-type(2)` [RECOMMENDED] (stable ID)

**Type Information**
- **Element Type:** button
- **Input Type:** button
- **Button Text:** "Childcare"

**Usage Example**
```python
# Click button
#root > div > div.w-100.maf-app-container:nth-of-type(3) > div.maf-main-component.overflow-auto.p-0.container-fluid:nth-of-type(2) > div.h-100.d-flex.flex-column > div.wrapper-container:nth-of-type(3) > div.tab-content.h-100 > div.tab-pane.h-100.active > div.h-100.row > div.flex-grow-1.pl-0.w-50.ml-2.mr-1.h-100:nth-of-type(2) > div.h-100 > div.pt-3:nth-of-type(2) > div.col-12.col-wd-11.col-xwd-10 > div.row > div.pl-3.mb-1.col-lg-3 > div.multi-select-filter.ml-1.btn-group.btn-group-sm.show > div.dropdown-menu.show > button.dropdown-item:nth-of-type(2)_button = driver.find_element(By.CSS_SELECTOR, '#root > div > div.w-100.maf-app-container:nth-of-type(3) > div.maf-main-component.overflow-auto.p-0.container-fluid:nth-of-type(2) > div.h-100.d-flex.flex-column > div.wrapper-container:nth-of-type(3) > div.tab-content.h-100 > div.tab-pane.h-100.active > div.h-100.row > div.flex-grow-1.pl-0.w-50.ml-2.mr-1.h-100:nth-of-type(2) > div.h-100 > div.pt-3:nth-of-type(2) > div.col-12.col-wd-11.col-xwd-10 > div.row > div.pl-3.mb-1.col-lg-3 > div.multi-select-filter.ml-1.btn-group.btn-group-sm.show > div.dropdown-menu.show > button.dropdown-item:nth-of-type(2)')
#root > div > div.w-100.maf-app-container:nth-of-type(3) > div.maf-main-component.overflow-auto.p-0.container-fluid:nth-of-type(2) > div.h-100.d-flex.flex-column > div.wrapper-container:nth-of-type(3) > div.tab-content.h-100 > div.tab-pane.h-100.active > div.h-100.row > div.flex-grow-1.pl-0.w-50.ml-2.mr-1.h-100:nth-of-type(2) > div.h-100 > div.pt-3:nth-of-type(2) > div.col-12.col-wd-11.col-xwd-10 > div.row > div.pl-3.mb-1.col-lg-3 > div.multi-select-filter.ml-1.btn-group.btn-group-sm.show > div.dropdown-menu.show > button.dropdown-item:nth-of-type(2)_button.click()
time.sleep(0.5)
```

**Metadata**
- **Interactions Observed:** 1
- **XPath:** `/html[1]/body[1]/div[1]/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/button[2]`

---

### #root > div > div.w-100.maf-app-container:nth-of-type(3) > div.maf-main-component.overflow-auto.p-0.container-fluid:nth-of-type(2) > div.h-100.d-flex.flex-column > div.wrapper-container:nth-of-type(3) > div.tab-content.h-100 > div.tab-pane.h-100.active > div.h-100.row > div.flex-grow-1.pl-0.w-50.ml-2.mr-1.h-100:nth-of-type(2) > div.h-100 > div.pt-3:nth-of-type(2) > div.col-12.col-wd-11.col-xwd-10 > div.row > div.pl-3.mb-1.col-lg-3 > div.multi-select-filter.ml-1.btn-group.btn-group-sm.show > div.dropdown-menu.show > button.dropdown-item:nth-of-type(3)

**Core Identifiers**
- **Field Name:** `#root > div > div.w-100.maf-app-container:nth-of-type(3) > div.maf-main-component.overflow-auto.p-0.container-fluid:nth-of-type(2) > div.h-100.d-flex.flex-column > div.wrapper-container:nth-of-type(3) > div.tab-content.h-100 > div.tab-pane.h-100.active > div.h-100.row > div.flex-grow-1.pl-0.w-50.ml-2.mr-1.h-100:nth-of-type(2) > div.h-100 > div.pt-3:nth-of-type(2) > div.col-12.col-wd-11.col-xwd-10 > div.row > div.pl-3.mb-1.col-lg-3 > div.multi-select-filter.ml-1.btn-group.btn-group-sm.show > div.dropdown-menu.show > button.dropdown-item:nth-of-type(3)`
- **Selector:** `#root > div > div.w-100.maf-app-container:nth-of-type(3) > div.maf-main-component.overflow-auto.p-0.container-fluid:nth-of-type(2) > div.h-100.d-flex.flex-column > div.wrapper-container:nth-of-type(3) > div.tab-content.h-100 > div.tab-pane.h-100.active > div.h-100.row > div.flex-grow-1.pl-0.w-50.ml-2.mr-1.h-100:nth-of-type(2) > div.h-100 > div.pt-3:nth-of-type(2) > div.col-12.col-wd-11.col-xwd-10 > div.row > div.pl-3.mb-1.col-lg-3 > div.multi-select-filter.ml-1.btn-group.btn-group-sm.show > div.dropdown-menu.show > button.dropdown-item:nth-of-type(3)` [RECOMMENDED] (stable ID)

**Type Information**
- **Element Type:** button
- **Input Type:** button
- **Button Text:** "Child & Spouse Maintenance"

**Usage Example**
```python
# Click button
#root > div > div.w-100.maf-app-container:nth-of-type(3) > div.maf-main-component.overflow-auto.p-0.container-fluid:nth-of-type(2) > div.h-100.d-flex.flex-column > div.wrapper-container:nth-of-type(3) > div.tab-content.h-100 > div.tab-pane.h-100.active > div.h-100.row > div.flex-grow-1.pl-0.w-50.ml-2.mr-1.h-100:nth-of-type(2) > div.h-100 > div.pt-3:nth-of-type(2) > div.col-12.col-wd-11.col-xwd-10 > div.row > div.pl-3.mb-1.col-lg-3 > div.multi-select-filter.ml-1.btn-group.btn-group-sm.show > div.dropdown-menu.show > button.dropdown-item:nth-of-type(3)_button = driver.find_element(By.CSS_SELECTOR, '#root > div > div.w-100.maf-app-container:nth-of-type(3) > div.maf-main-component.overflow-auto.p-0.container-fluid:nth-of-type(2) > div.h-100.d-flex.flex-column > div.wrapper-container:nth-of-type(3) > div.tab-content.h-100 > div.tab-pane.h-100.active > div.h-100.row > div.flex-grow-1.pl-0.w-50.ml-2.mr-1.h-100:nth-of-type(2) > div.h-100 > div.pt-3:nth-of-type(2) > div.col-12.col-wd-11.col-xwd-10 > div.row > div.pl-3.mb-1.col-lg-3 > div.multi-select-filter.ml-1.btn-group.btn-group-sm.show > div.dropdown-menu.show > button.dropdown-item:nth-of-type(3)')
#root > div > div.w-100.maf-app-container:nth-of-type(3) > div.maf-main-component.overflow-auto.p-0.container-fluid:nth-of-type(2) > div.h-100.d-flex.flex-column > div.wrapper-container:nth-of-type(3) > div.tab-content.h-100 > div.tab-pane.h-100.active > div.h-100.row > div.flex-grow-1.pl-0.w-50.ml-2.mr-1.h-100:nth-of-type(2) > div.h-100 > div.pt-3:nth-of-type(2) > div.col-12.col-wd-11.col-xwd-10 > div.row > div.pl-3.mb-1.col-lg-3 > div.multi-select-filter.ml-1.btn-group.btn-group-sm.show > div.dropdown-menu.show > button.dropdown-item:nth-of-type(3)_button.click()
time.sleep(0.5)
```

**Metadata**
- **Interactions Observed:** 1
- **XPath:** `/html[1]/body[1]/div[1]/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/button[3]`

---

### .dropdown-toggle.btn.btn-light.btn-sm

**Core Identifiers**
- **Field Name:** `.dropdown-toggle.btn.btn-light.btn-sm`
- **Selector:** `.dropdown-toggle.btn.btn-light.btn-sm` [USE WITH CARE] (complex selector)

**Type Information**
- **Element Type:** button
- **Input Type:** button
- **Button Text:** "Living Expense"

**Usage Example**
```python
# Click button
.dropdown-toggle.btn.btn-light.btn-sm_button = driver.find_element(By.CSS_SELECTOR, '.dropdown-toggle.btn.btn-light.btn-sm')
.dropdown-toggle.btn.btn-light.btn-sm_button.click()
time.sleep(0.5)
```

**Metadata**
- **Interactions Observed:** 2
- **XPath:** `/html[1]/body[1]/div[1]/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/button[1]`

---

### .dropdown-toggle.btn.btn-primary.btn-sm

**Core Identifiers**
- **Field Name:** `.dropdown-toggle.btn.btn-primary.btn-sm`
- **Selector:** `.dropdown-toggle.btn.btn-primary.btn-sm` [USE WITH CARE] (complex selector)

**Type Information**
- **Element Type:** button
- **Input Type:** button
- **Button Text:** "Opportunity"

**Usage Example**
```python
# Click button
.dropdown-toggle.btn.btn-primary.btn-sm_button = driver.find_element(By.CSS_SELECTOR, '.dropdown-toggle.btn.btn-primary.btn-sm')
.dropdown-toggle.btn.btn-primary.btn-sm_button.click()
time.sleep(0.5)
```

**Metadata**
- **Interactions Observed:** 1
- **XPath:** `/html[1]/body[1]/div[1]/div[1]/div[3]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/button[1]`

---

### Add

**Core Identifiers**
- **Field Name:** `Add`
- **Selector:** `[data-testid="Add"]` [RECOMMENDED] (stable data-testid)
- **ID:** `btn_083ea9e3-8fb7-4462-a6b1-116567202320` [WARNING] (contains UUID - unstable)
- **data-testid:** `Add`

**Type Information**
- **Element Type:** button
- **Input Type:** button
- **Button Text:** "Real Estate Asset"

**Usage Example**
```python
# Click button
Add_button = driver.find_element(By.CSS_SELECTOR, '[data-testid="Add"]')
Add_button.click()
time.sleep(0.5)
```

**Metadata**
- **Interactions Observed:** 1
- **XPath:** `//*[@id="btn_083ea9e3-8fb7-4462-a6b1-116567202320"]`

---

### Add

**Core Identifiers**
- **Field Name:** `Add`
- **Selector:** `[data-testid="Add"]` [RECOMMENDED] (stable data-testid)
- **ID:** `btn_6e535688-0766-47a6-a358-e0d25eed59c9` [WARNING] (contains UUID - unstable)
- **data-testid:** `Add`

**Type Information**
- **Element Type:** button
- **Input Type:** button
- **Button Text:** "Other Asset"

**Usage Example**
```python
# Click button
Add_button = driver.find_element(By.CSS_SELECTOR, '[data-testid="Add"]')
Add_button.click()
time.sleep(0.5)
```

**Metadata**
- **Interactions Observed:** 1
- **XPath:** `//*[@id="btn_6e535688-0766-47a6-a358-e0d25eed59c9"]`

---

### Add

**Core Identifiers**
- **Field Name:** `Add`
- **Selector:** `[data-testid="Add"]` [RECOMMENDED] (stable data-testid)
- **ID:** `btn_c3b681e8-2395-4210-8aa9-5637336f7f56` [WARNING] (contains UUID - unstable)
- **data-testid:** `Add`

**Type Information**
- **Element Type:** button
- **Input Type:** button
- **Button Text:** "Liability"

**Usage Example**
```python
# Click button
Add_button = driver.find_element(By.CSS_SELECTOR, '[data-testid="Add"]')
Add_button.click()
time.sleep(0.5)
```

**Metadata**
- **Interactions Observed:** 1
- **XPath:** `//*[@id="btn_c3b681e8-2395-4210-8aa9-5637336f7f56"]`

---

### Add

**Core Identifiers**
- **Field Name:** `Add`
- **Selector:** `[data-testid="Add"]` [RECOMMENDED] (stable data-testid)
- **ID:** `btn_2043785a-5663-42ad-bb8c-562a10959e1b` [WARNING] (contains UUID - unstable)
- **data-testid:** `Add`

**Type Information**
- **Element Type:** button
- **Input Type:** button
- **Button Text:** "Income"

**Usage Example**
```python
# Click button
Add_button = driver.find_element(By.CSS_SELECTOR, '[data-testid="Add"]')
Add_button.click()
time.sleep(0.5)
```

**Metadata**
- **Interactions Observed:** 1
- **XPath:** `//*[@id="btn_2043785a-5663-42ad-bb8c-562a10959e1b"]`

---

### Add  Loan

**Core Identifiers**
- **Field Name:** `Add Loan`
- **Label:** Add  Loan
- **Selector:** `[data-testid="Add Loan"]` [RECOMMENDED] (stable data-testid)
- **ID:** `btn_7c86c163-cef1-4061-b70a-0c2f7c4beda3` [WARNING] (contains UUID - unstable)
- **data-testid:** `Add Loan`

**Type Information**
- **Element Type:** button
- **Input Type:** button
- **Button Text:** "Add Loan"

**Usage Example**
```python
# Click button
Add Loan_button = driver.find_element(By.CSS_SELECTOR, '[data-testid="Add Loan"]')
Add Loan_button.click()
time.sleep(0.5)
```

**Metadata**
- **Interactions Observed:** 1
- **XPath:** `//*[@id="btn_7c86c163-cef1-4061-b70a-0c2f7c4beda3"]`

---

### Home  Loans

**Core Identifiers**
- **Field Name:** `Home Loans`
- **Label:** Home  Loans
- **Selector:** `#root > div > div.w-100.maf-app-container:nth-of-type(3) > div.maf-main-component.overflow-auto.p-0.container-fluid:nth-of-type(2) > div.h-100.d-flex.flex-column > div.d-flex.flex-column.flex-grow-1.overflow-auto:nth-of-type(2) > div.tab-content.h-100 > div.tab-pane.h-100.active > div.pt-2.h-100.d-flex.flex-column.container-fluid > div.card.Dashboard_dashboardCard__3YDGy.css-fdpxu8 > div.card-body > div:nth-of-type(2) > div.MAFToolbar-module_toolbar-container__fYIIi > div.css-1vc1nn3 > div.btn-group.show > div.dropdown-menu.show > button.dropdown-item` [RECOMMENDED] (stable ID)

**Type Information**
- **Element Type:** button
- **Input Type:** button
- **Button Text:** "Home Loans"

**Usage Example**
```python
# Click button
Home Loans_button = driver.find_element(By.CSS_SELECTOR, '#root > div > div.w-100.maf-app-container:nth-of-type(3) > div.maf-main-component.overflow-auto.p-0.container-fluid:nth-of-type(2) > div.h-100.d-flex.flex-column > div.d-flex.flex-column.flex-grow-1.overflow-auto:nth-of-type(2) > div.tab-content.h-100 > div.tab-pane.h-100.active > div.pt-2.h-100.d-flex.flex-column.container-fluid > div.card.Dashboard_dashboardCard__3YDGy.css-fdpxu8 > div.card-body > div:nth-of-type(2) > div.MAFToolbar-module_toolbar-container__fYIIi > div.css-1vc1nn3 > div.btn-group.show > div.dropdown-menu.show > button.dropdown-item')
Home Loans_button.click()
time.sleep(0.5)
```

**Metadata**
- **Interactions Observed:** 1
- **XPath:** `/html[1]/body[1]/div[1]/div[1]/div[3]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/button[1]`

---

### employment

**Core Identifiers**
- **Field Name:** `employment`
- **Selector:** `#employment` [RECOMMENDED] (stable ID)
- **ID:** `employment`

**Type Information**
- **Element Type:** button
- **Input Type:** button
- **Button Text:** "Employment"

**Usage Example**
```python
# Click button
employment_button = driver.find_element(By.CSS_SELECTOR, '#employment')
employment_button.click()
time.sleep(0.5)
```

**Metadata**
- **Interactions Observed:** 1
- **XPath:** `//*[@id="employment"]`

---

### financials

**Core Identifiers**
- **Field Name:** `financials`
- **Selector:** `#financials` [RECOMMENDED] (stable ID)
- **ID:** `financials`

**Type Information**
- **Element Type:** button
- **Input Type:** submit
- **Button Text:** "Financials"

**Usage Example**
```python
# Click button
financials_button = driver.find_element(By.CSS_SELECTOR, '#financials')
financials_button.click()
time.sleep(0.5)
```

**Metadata**
- **Interactions Observed:** 1
- **XPath:** `//*[@id="financials"]`

---

### incomes

**Core Identifiers**
- **Field Name:** `incomes`
- **Selector:** `#incomes` [RECOMMENDED] (stable ID)
- **ID:** `incomes`

**Type Information**
- **Element Type:** button
- **Input Type:** button
- **Button Text:** "Other Income"

**Usage Example**
```python
# Click button
incomes_button = driver.find_element(By.CSS_SELECTOR, '#incomes')
incomes_button.click()
time.sleep(0.5)
```

**Metadata**
- **Interactions Observed:** 1
- **XPath:** `//*[@id="incomes"]`

---

### liabilities

**Core Identifiers**
- **Field Name:** `liabilities`
- **Selector:** `#liabilities` [RECOMMENDED] (stable ID)
- **ID:** `liabilities`

**Type Information**
- **Element Type:** button
- **Input Type:** button
- **Button Text:** "Liabilities(1)"

**Usage Example**
```python
# Click button
liabilities_button = driver.find_element(By.CSS_SELECTOR, '#liabilities')
liabilities_button.click()
time.sleep(0.5)
```

**Metadata**
- **Interactions Observed:** 1
- **XPath:** `//*[@id="liabilities"]`

---

### otherAssets

**Core Identifiers**
- **Field Name:** `otherAssets`
- **Selector:** `#otherAssets` [RECOMMENDED] (stable ID)
- **ID:** `otherAssets`

**Type Information**
- **Element Type:** button
- **Input Type:** button
- **Button Text:** "Assets - Other"

**Usage Example**
```python
# Click button
otherAssets_button = driver.find_element(By.CSS_SELECTOR, '#otherAssets')
otherAssets_button.click()
time.sleep(0.5)
```

**Metadata**
- **Interactions Observed:** 1
- **XPath:** `//*[@id="otherAssets"]`

---

### realEstateAssets

**Core Identifiers**
- **Field Name:** `realEstateAssets`
- **Selector:** `#realEstateAssets` [RECOMMENDED] (stable ID)
- **ID:** `realEstateAssets`

**Type Information**
- **Element Type:** button
- **Input Type:** button
- **Button Text:** "Assets - Real Estate"

**Usage Example**
```python
# Click button
realEstateAssets_button = driver.find_element(By.CSS_SELECTOR, '#realEstateAssets')
realEstateAssets_button.click()
time.sleep(0.5)
```

**Metadata**
- **Interactions Observed:** 1
- **XPath:** `//*[@id="realEstateAssets"]`

---

### #root > div > div.w-100.maf-app-container:nth-of-type(3) > div.maf-main-component.overflow-auto.p-0.container-fluid:nth-of-type(2) > div.h-100.d-flex.flex-column > div.wrapper-container:nth-of-type(3) > div.tab-content.h-100 > div.tab-pane.h-100.active > div.h-100.row > div.flex-grow-1.pl-0.w-50.ml-2.mr-1.h-100:nth-of-type(2) > div.h-100 > div.pt-3:nth-of-type(2)

**Core Identifiers**
- **Field Name:** `#root > div > div.w-100.maf-app-container:nth-of-type(3) > div.maf-main-component.overflow-auto.p-0.container-fluid:nth-of-type(2) > div.h-100.d-flex.flex-column > div.wrapper-container:nth-of-type(3) > div.tab-content.h-100 > div.tab-pane.h-100.active > div.h-100.row > div.flex-grow-1.pl-0.w-50.ml-2.mr-1.h-100:nth-of-type(2) > div.h-100 > div.pt-3:nth-of-type(2)`
- **Selector:** `#root > div > div.w-100.maf-app-container:nth-of-type(3) > div.maf-main-component.overflow-auto.p-0.container-fluid:nth-of-type(2) > div.h-100.d-flex.flex-column > div.wrapper-container:nth-of-type(3) > div.tab-content.h-100 > div.tab-pane.h-100.active > div.h-100.row > div.flex-grow-1.pl-0.w-50.ml-2.mr-1.h-100:nth-of-type(2) > div.h-100 > div.pt-3:nth-of-type(2)` [RECOMMENDED] (stable ID)

**Type Information**
- **Element Type:** div

**Usage Example**
```python
```

**Metadata**
- **Interactions Observed:** 1
- **XPath:** `/html[1]/body[1]/div[1]/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]`

---

### #root > div > div.w-100.maf-app-container:nth-of-type(3) > div.maf-main-component.overflow-auto.p-0.container-fluid:nth-of-type(2) > div.h-100.d-flex.flex-column > div.wrapper-container:nth-of-type(3) > div.tab-content.h-100 > div.tab-pane.h-100.active > div.h-100.row > div.flex-grow-1.pl-0.w-50.ml-2.mr-1.h-100:nth-of-type(2) > div.h-100 > div.pt-3:nth-of-type(2) > div.col-lg-11.col-xwd-9 > div:nth-of-type(2) > table.mt-3.col-12 > tbody > tr:nth-of-type(2) > td.RealEstateComponentV2_bordered__2pwX2 > div.RealEstateComponentV2_detailsContainer__2fAhh.col > div.row > div.pt-1.mt-1.col-lg-12 > div > div.h-100.row > div.col-lg-4:nth-of-type(2)

**Core Identifiers**
- **Field Name:** `#root > div > div.w-100.maf-app-container:nth-of-type(3) > div.maf-main-component.overflow-auto.p-0.container-fluid:nth-of-type(2) > div.h-100.d-flex.flex-column > div.wrapper-container:nth-of-type(3) > div.tab-content.h-100 > div.tab-pane.h-100.active > div.h-100.row > div.flex-grow-1.pl-0.w-50.ml-2.mr-1.h-100:nth-of-type(2) > div.h-100 > div.pt-3:nth-of-type(2) > div.col-lg-11.col-xwd-9 > div:nth-of-type(2) > table.mt-3.col-12 > tbody > tr:nth-of-type(2) > td.RealEstateComponentV2_bordered__2pwX2 > div.RealEstateComponentV2_detailsContainer__2fAhh.col > div.row > div.pt-1.mt-1.col-lg-12 > div > div.h-100.row > div.col-lg-4:nth-of-type(2)`
- **Selector:** `#root > div > div.w-100.maf-app-container:nth-of-type(3) > div.maf-main-component.overflow-auto.p-0.container-fluid:nth-of-type(2) > div.h-100.d-flex.flex-column > div.wrapper-container:nth-of-type(3) > div.tab-content.h-100 > div.tab-pane.h-100.active > div.h-100.row > div.flex-grow-1.pl-0.w-50.ml-2.mr-1.h-100:nth-of-type(2) > div.h-100 > div.pt-3:nth-of-type(2) > div.col-lg-11.col-xwd-9 > div:nth-of-type(2) > table.mt-3.col-12 > tbody > tr:nth-of-type(2) > td.RealEstateComponentV2_bordered__2pwX2 > div.RealEstateComponentV2_detailsContainer__2fAhh.col > div.row > div.pt-1.mt-1.col-lg-12 > div > div.h-100.row > div.col-lg-4:nth-of-type(2)` [RECOMMENDED] (stable ID)

**Type Information**
- **Element Type:** div

**Usage Example**
```python
```

**Metadata**
- **Interactions Observed:** 3
- **XPath:** `/html[1]/body[1]/div[1]/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/table[1]/tbody[1]/tr[2]/td[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]`

---

### #root > div > div.w-100.maf-app-container:nth-of-type(3) > div.maf-main-component.overflow-auto.p-0.container-fluid:nth-of-type(2) > div.h-100.d-flex.flex-column > div.wrapper-container:nth-of-type(3) > div.tab-content.h-100 > div.tab-pane.h-100.active > div.h-100.row > div.flex-grow-1.pl-0.w-50.ml-2.mr-1.h-100:nth-of-type(2) > div.h-100.opp-details-wrapper > div.row > div.col-xxl-11.col-wd-10.col-xwd-9 > div.pt-4.row:nth-of-type(3) > div.col-md-8:nth-of-type(2) > div.row > div.col-sm-12 > div.row > div.col-md-6

**Core Identifiers**
- **Field Name:** `#root > div > div.w-100.maf-app-container:nth-of-type(3) > div.maf-main-component.overflow-auto.p-0.container-fluid:nth-of-type(2) > div.h-100.d-flex.flex-column > div.wrapper-container:nth-of-type(3) > div.tab-content.h-100 > div.tab-pane.h-100.active > div.h-100.row > div.flex-grow-1.pl-0.w-50.ml-2.mr-1.h-100:nth-of-type(2) > div.h-100.opp-details-wrapper > div.row > div.col-xxl-11.col-wd-10.col-xwd-9 > div.pt-4.row:nth-of-type(3) > div.col-md-8:nth-of-type(2) > div.row > div.col-sm-12 > div.row > div.col-md-6`
- **Selector:** `#root > div > div.w-100.maf-app-container:nth-of-type(3) > div.maf-main-component.overflow-auto.p-0.container-fluid:nth-of-type(2) > div.h-100.d-flex.flex-column > div.wrapper-container:nth-of-type(3) > div.tab-content.h-100 > div.tab-pane.h-100.active > div.h-100.row > div.flex-grow-1.pl-0.w-50.ml-2.mr-1.h-100:nth-of-type(2) > div.h-100.opp-details-wrapper > div.row > div.col-xxl-11.col-wd-10.col-xwd-9 > div.pt-4.row:nth-of-type(3) > div.col-md-8:nth-of-type(2) > div.row > div.col-sm-12 > div.row > div.col-md-6` [RECOMMENDED] (stable ID)

**Type Information**
- **Element Type:** div

**Usage Example**
```python
```

**Metadata**
- **Interactions Observed:** 1
- **XPath:** `/html[1]/body[1]/div[1]/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]`

---
