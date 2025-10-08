# Other Income - COMPLETE Field Reference

**Source**: connective-other-income-mcp.json recording
**Extraction Date**: 2025-10-08
**Recording Duration**: 1m 58s
**Total Events**: 51
**Extraction Method**: Automated field extractor + manual context analysis

---

## Summary

**Total Fields**: 9 (7 extracted from interactions + 2 from context)

**Field Breakdown**:
- Navigation buttons: 2 (#financials, #incomes)
- Action button: 1 ([data-testid="Add"])
- Form inputs: 3 (#type, #frequency, #amount)
- Context buttons: 2 (anonymous - ownership, evidence)
- Container element: 1 (div - context only)

---

## Primary Form Fields

### 1. Income Type (Dropdown)

**Core Identifiers**
- **Field Name:** `type`
- **Label:** "Shared Equally" (from form context)
- **Selector:** `#type` **[RECOMMENDED]** (stable ID)
- **ID:** `type`
- **data-testid:** `income-type-{UUID}` **[WARNING]** (UUID changes per row - DO NOT USE)

**Type Information**
- **Element Type:** select
- **Input Type:** select-one

**Context**
- **In Form:** Yes
- **Form Action:** https://crm.connective.com.au/#/
- **Form Method:** get
- **Related Fields:** `frequency`, `amount`, (2 anonymous buttons)

**Dropdown Options** (4)
1. Dividends
2. Family Allowance
3. Maintenance
4. Other

**Validation**
- **Required:** No (from recording validation data)

**Usage Example**
```python
from selenium.webdriver.support.ui import Select

# RECOMMENDED: Use stable ID selector
type_dropdown = driver.find_element(By.ID, "type")
Select(type_dropdown).select_by_visible_text("Dividends")
time.sleep(0.5)

# ❌ AVOID: data-testid contains changing UUID
# type_dropdown = driver.find_element(By.CSS_SELECTOR, '[data-testid="income-type-84a841a0..."]')
```

**Recorded Values** (all 4 types tested in recording)
- Dividends
- Family Allowance
- Maintenance
- Other

**Metadata**
- **Interactions Observed:** 12
- **XPath:** `//*[@id="type"]`

---

### 2. Frequency (Dropdown)

**Core Identifiers**
- **Field Name:** `frequency`
- **Label:** "Shared Equally" (from form context)
- **Selector:** `#frequency` **[RECOMMENDED]** (stable ID)
- **ID:** `frequency`

**Type Information**
- **Element Type:** select
- **Input Type:** select-one

**Context**
- **In Form:** Yes
- **Form Action:** https://crm.connective.com.au/#/
- **Form Method:** get
- **Related Fields:** `type`, `amount`

**Dropdown Options** (4)
1. Annual
2. Monthly
3. Fortnightly
4. Weekly

**Usage Example**
```python
from selenium.webdriver.support.ui import Select

frequency_dropdown = driver.find_element(By.ID, "frequency")
Select(frequency_dropdown).select_by_visible_text("Annual")
time.sleep(0.5)
```

**Recorded Values** (all 4 frequencies tested)
- Annual
- Monthly
- Fortnightly
- Weekly

**Metadata**
- **Interactions Observed:** 12
- **XPath:** `//*[@id="frequency"]`

---

### 3. Amount (Text Input)

**Core Identifiers**
- **Field Name:** `amount`
- **Label:** "0.00" (placeholder/initial value)
- **Selector:** `#amount` **[RECOMMENDED]** (stable ID)
- **ID:** `amount`

**Type Information**
- **Element Type:** input
- **Input Type:** text
- **Format:** Currency (right-aligned, numeric)

**Context**
- **In Form:** Yes
- **Form Action:** https://crm.connective.com.au/#/
- **Form Method:** get
- **Related Fields:** `type`, `frequency`

**Validation**
- **Required:** No (from recording data)
- **Pattern:** Numeric values (currency)

**Usage Example**
```python
amount_field = driver.find_element(By.ID, "amount")
amount_field.clear()
amount_field.send_keys("5000")
time.sleep(0.5)
```

**Recorded Values** (progressive typing observed)
- 5
- 50
- 100
- 500
- 1000
- 5000

**Metadata**
- **Interactions Observed:** 12
- **XPath:** `//*[@id="amount"]`

---

## Navigation Buttons

### 4. Financials Tab

**Core Identifiers**
- **Field Name:** `financials`
- **Selector:** `#financials` **[RECOMMENDED]** (stable ID)
- **ID:** `financials`

**Type Information**
- **Element Type:** button
- **Input Type:** submit
- **Button Text:** "Financials"

**Usage Example**
```python
financials_tab = driver.find_element(By.ID, "financials")
financials_tab.click()
time.sleep(1)  # Wait for tab to load
```

**Metadata**
- **Interactions Observed:** 1
- **XPath:** `//*[@id="financials"]`

---

### 5. Other Income Sub-Tab

**Core Identifiers**
- **Field Name:** `incomes`
- **Selector:** `#incomes` **[RECOMMENDED]** (stable ID)
- **ID:** `incomes`

**Type Information**
- **Element Type:** button
- **Input Type:** button
- **Button Text:** "Other Income"

**Usage Example**
```python
incomes_tab = driver.find_element(By.ID, "incomes")
incomes_tab.click()
time.sleep(2)  # Wait for section to load
```

**Metadata**
- **Interactions Observed:** 1
- **XPath:** `//*[@id="incomes"]`

---

## Action Buttons

### 6. Add Income Button **[CRITICAL SELECTOR]**

**Core Identifiers**
- **Field Name:** `Add`
- **Selector:** `[data-testid="Add"]` **[RECOMMENDED]** (stable data-testid)
- **ID:** `btn_{UUID}` **[WARNING]** (UUID changes per session - DO NOT USE)
- **data-testid:** `Add` (stable!)

**Type Information**
- **Element Type:** button
- **Input Type:** button
- **Button Text:** "Income"

**Critical Selector Notes**
⚠️ **This is the KEY finding from this recording!**

**✅ STABLE - Use this:**
```python
add_button = driver.find_element(By.CSS_SELECTOR, '[data-testid="Add"]')
```

**❌ UNSTABLE - Do NOT use:**
```python
# This ID contains UUID and changes:
# btn_e6e4f13c-445e-4754-8efa-455f5f0444bb
add_button = driver.find_element(By.ID, "btn_e6e4f13c-445e-4754-8efa-455f5f0444bb")
```

**Usage Example**
```python
# Add new income entry
add_button = driver.find_element(By.CSS_SELECTOR, '[data-testid="Add"]')
add_button.click()
time.sleep(1)  # Wait for form to appear
```

**Metadata**
- **Interactions Observed:** 4 (once per income entry in recording)
- **XPath:** `//*[@id="btn_e6e4f13c-445e-4754-8efa-455f5f0444bb"]` (unstable)

---

## Context Buttons (Not Interacted With)

These buttons exist in the form but weren't clicked in the recording. They appear in the `relatedFields` array:

### 7. Anonymous Button #1 (Likely Ownership Allocation)

**Core Identifiers**
- **Field Name:** *(none)*
- **ID:** *(none)*
- **Selector:** Unknown (not clicked in recording)

**Type Information**
- **Element Type:** button
- **Input Type:** button
- **Purpose:** Likely "Ownership Allocation" button (for dual applications)

**Context**
- **In Form:** Yes (appears in relatedFields)
- **Related To:** `type`, `frequency`, `amount`

**Note**: This button appears in other sections (Assets, Liabilities) for allocating ownership between applicants. Not used for single applicant cases.

---

### 8. Anonymous Button #2 (Likely Evidence/Assign)

**Core Identifiers**
- **Field Name:** *(none)*
- **ID:** *(none)*
- **Selector:** Unknown (not clicked in recording)

**Type Information**
- **Element Type:** button
- **Input Type:** button
- **Purpose:** Likely "Assign Evidence" or "Evidence" button

**Context**
- **In Form:** Yes (appears in relatedFields)
- **Related To:** `type`, `frequency`, `amount`

**Note**: This button likely allows linking evidence documents to income entries. Not required for basic entry.

---

## Container Element (Context Only)

### 9. Form Container Div

**Core Identifiers**
- **Selector:** Long nth-of-type selector (complex, not recommended)
- **Element Type:** div

**Purpose**: Context element only - not for direct interaction. This is the container div that holds the income form.

---

## Complete Workflow

### Adding Other Income Entry

**Prerequisites**:
- Already on CRM dashboard
- Logged in

**Steps**:

1. **Navigate to Financials Tab**
   ```python
   driver.find_element(By.ID, "financials").click()
   time.sleep(1)
   ```

2. **Navigate to Other Income Sub-Tab**
   ```python
   driver.find_element(By.ID, "incomes").click()
   time.sleep(2)
   ```

3. **Click Add Income**
   ```python
   driver.find_element(By.CSS_SELECTOR, '[data-testid="Add"]').click()
   time.sleep(1)
   ```

4. **Select Income Type**
   ```python
   from selenium.webdriver.support.ui import Select
   type_dd = driver.find_element(By.ID, "type")
   Select(type_dd).select_by_visible_text("Dividends")
   time.sleep(0.5)
   ```

5. **Select Frequency**
   ```python
   freq_dd = driver.find_element(By.ID, "frequency")
   Select(freq_dd).select_by_visible_text("Annual")
   time.sleep(0.5)
   ```

6. **Enter Amount**
   ```python
   amount = driver.find_element(By.ID, "amount")
   amount.clear()
   amount.send_keys("5000")
   time.sleep(2)  # Auto-save wait
   ```

7. **Repeat steps 3-6 for additional income entries**

---

## Field Relationships

**Form Structure**:
```
┌─────────────────────────────────────────────────────┐
│ [Add Button] ← [data-testid="Add"]                 │
├─────────────────────────────────────────────────────┤
│ Type:      [Dividends ▼]          (#type)          │
│ Frequency: [Annual ▼]              (#frequency)     │
│ Amount:    [5000        ]          (#amount)        │
│                                                      │
│ [Anonymous Button 1] [Anonymous Button 2]           │
│ (Ownership?)         (Evidence?)                    │
└─────────────────────────────────────────────────────┘
```

**Related Fields** (from `elementContext.relatedFields`):
1. `type` (select-one)
2. *(anonymous button)* - position 2
3. *(anonymous button)* - position 3
4. `frequency` (select-one)
5. `amount` (text)

---

## MCP Query Compatibility

**After SDK Enhancement**, these queries should work:

```python
from sdk import CRMReference

crm = CRMReference()

# Get field selectors
crm.get_selector("type", section="other_income")      # → "#type"
crm.get_selector("frequency", section="other_income")  # → "#frequency"
crm.get_selector("amount", section="other_income")     # → "#amount"
crm.get_selector("Add", section="other_income")        # → '[data-testid="Add"]'

# Get field metadata
field_info = crm.get_field_metadata("amount", section="other_income")
# → InputField(name="amount", selector="#amount", type="text",
#              format="currency", required=False, ...)

# List all fields in section
fields = crm.list_section_fields("other_income")
# → [type, frequency, amount, Add, financials, incomes]

# Get related fields
related = crm.get_related_fields("amount", section="other_income")
# → [type, frequency]
```

---

## Key Insights from Recording

1. **Selector Stability**: `[data-testid="Add"]` is stable, but button IDs with UUIDs are not
2. **data-testid on dropdowns**: Contains UUIDs that change per row - use `#id` instead
3. **Related Fields**: 2 anonymous buttons exist but weren't used
4. **All Options Tested**: Recording tested all 4 income types and all 4 frequencies
5. **Progressive Typing**: Users type amounts incrementally (5→50→500→5000)
6. **Auto-Save**: Form auto-saves after field completion (no submit button)

---

## Comparison to Other Sections

| Aspect | Living Expenses | Assets | Liabilities | Other Income |
|--------|----------------|---------|-------------|--------------|
| **Form Fields** | 3 per entry | 4-5 per entry | 9-12 per entry | **3 per entry** (simplest!) |
| **Dropdown Options** | 21 categories | 18 types | 18 types | **4 types** |
| **Anonymous Buttons** | No | Yes (ownership) | Yes (ownership, security) | **Yes (2 buttons)** |
| **Conditional Fields** | No | Yes (vehicle type) | No | **No** |
| **Selector Stability** | Mixed | Good | Good | **Excellent** |

---

**Document Status**: ✅ Complete field extraction from recording + context analysis
**Extraction Method**: Automated + manual verification
**Ready For**: SDK parsing, MCP integration, automation

