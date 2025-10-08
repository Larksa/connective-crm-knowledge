# Other Income - Complete Field Reference

**Source**: connective-other-income-mcp.json
**Generated**: 2025-10-08
**Recording Duration**: 1m 58s
**Total Events**: 51

---

## Summary

**Total Fields Discovered**: 7

**Field Types**:
- button: 3
- div: 1
- input: 1
- select: 2

---

## Field Definitions

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
- `Annual`
- `Monthly`
- `Fortnightly`
- `Weekly`

**Metadata**
- **Interactions Observed:** 12
- **XPath:** `//*[@id="frequency"]`

---

### Shared Equally

**Core Identifiers**
- **Field Name:** `type`
- **Label:** Shared Equally
- **Selector:** `#type` [RECOMMENDED] (stable ID)
- **ID:** `type`
- **data-testid:** `income-type-ae771380-a400-11f0-9560-75d5d04fee53` [WARNING] (contains UUID - unstable)

**Type Information**
- **Element Type:** select
- **Input Type:** select-one

**Context**
- **In Form:** Yes
- **Form Action:** https://crm.connective.com.au/#/
- **Form Method:** get
- **Related Fields:** `frequency`, `amount`

**Dropdown Options**
- **Total Options:** 4
- **Options:**
  - Dividends
  - Family Allowance
  - Maintenance
  - Other

**Usage Example**
```python
# Select dropdown
from selenium.webdriver.support.ui import Select
type_dropdown = driver.find_element(By.CSS_SELECTOR, '#type')
Select(type_dropdown).select_by_visible_text('Dividends')
time.sleep(0.5)
```

**Recorded Values** (from actual usage)
- `Dividends`
- `Family Allowance`
- `Maintenance`
- `Other`

**Metadata**
- **Interactions Observed:** 12
- **XPath:** `//*[@id="type"]`

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
amount_field.send_keys('5')
time.sleep(0.5)
```

**Recorded Values** (from actual usage)
- `5`
- `5000`
- `500`
- `1`
- `100`
- *(1 more values recorded)*

**Metadata**
- **Interactions Observed:** 12
- **XPath:** `//*[@id="amount"]`

---

### Add

**Core Identifiers**
- **Field Name:** `Add`
- **Selector:** `[data-testid="Add"]` [RECOMMENDED] (stable data-testid)
- **ID:** `btn_e6e4f13c-445e-4754-8efa-455f5f0444bb` [WARNING] (contains UUID - unstable)
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
- **Interactions Observed:** 4
- **XPath:** `//*[@id="btn_e6e4f13c-445e-4754-8efa-455f5f0444bb"]`

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
- **Interactions Observed:** 3
- **XPath:** `/html[1]/body[1]/div[1]/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]`

---
