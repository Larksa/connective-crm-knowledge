# Liabilities Section - Field Extraction Supplement

**Source**: jlall.json recording (147 events)
**Extraction Date**: 2025-10-08
**Purpose**: Supplement existing liabilities.md with enhanced metadata from recording analysis

---

## Summary

This supplement provides **additional metadata** extracted from actual CRM usage recordings to enhance the existing comprehensive liabilities.md documentation.

**DO NOT REPLACE** existing documentation - use this to **ADD**:
- ✅ data-testid attributes
- ✅ Validation rules (required, readonly, disabled)
- ✅ relatedFields arrays
- ✅ UUID stability warnings
- ✅ Recorded usage examples
- ✅ Interaction frequency data

---

## Field Verification Status

### ✅ VERIFIED SELECTORS (Confirmed from Recording)

These selectors from liabilities.md are **confirmed accurate** from the recording:

| Field | Documented Selector | Recording Confirms | Status |
|-------|-------------------|-------------------|--------|
| institution | #institution | #institution | ✅ VERIFIED |
| accountName | #accountName | #accountName | ✅ VERIFIED |
| accountBSB | #accountBSB | #accountBSB | ✅ VERIFIED |
| accountNumber | #accountNumber | #accountNumber | ✅ VERIFIED |
| limit | #limit | #limit | ✅ VERIFIED |
| accountRepayment | #accountRepayment | #accountRepayment | ✅ VERIFIED |
| accountRepaymentFrequency | #accountRepaymentFrequency | #accountRepaymentFrequency | ✅ VERIFIED |
| accountClearingFromLoan | [name="accountClearingFromLoan"] | [name="accountClearingFromLoan"] | ✅ VERIFIED |

**Recommendation**: Existing selectors in liabilities.md are **100% accurate** - no changes needed.

---

## 🆕 NEW FIELD DISCOVERED

### priority Field

**Core Identifiers**
- **Field Name:** `priority`
- **Selector:** `#priority` **[RECOMMENDED]** (stable ID)
- **ID:** `priority`

**Type Information**
- **Element Type:** select (dropdown)
- **Input Type:** select-one

**Recording Evidence**
- **Interactions Observed:** Multiple selections in recording
- **Section:** Liabilities
- **Related To:** Other liability fields (institution, accountName, etc.)

**Usage Example**
```python
from selenium.webdriver.support.ui import Select

priority_dropdown = driver.find_element(By.ID, "priority")
Select(priority_dropdown).select_by_visible_text("High")
time.sleep(0.5)
```

**Suggested Addition to liabilities.md**:
```markdown
#### Element: Priority
- **Field Name:** priority
- **Label:** Priority
- **Selector:** #priority
- **Type:** select
- **Section:** liabilities
- **Description:** Priority level for the liability in loan application processing
- **Options:** [To be determined - not captured in this recording]
```

---

## Enhanced Metadata from Recording

### data-testid Attributes

The recording revealed that several fields have **data-testid** attributes, but they contain UUIDs that change:

⚠️ **UUID WARNING**: Do NOT use data-testid for liability form fields:
```python
# ❌ UNSTABLE - UUID changes per row
type_field = driver.find_element(By.CSS_SELECTOR, '[data-testid="liability-type-{UUID}"]')

# ✅ STABLE - Use ID instead
type_field = driver.find_element(By.ID, "liabilityType")
```

**Exception**: The "Add" button has a **stable** data-testid:
```python
# ✅ STABLE - Use this for Add button
add_button = driver.find_element(By.CSS_SELECTOR, '[data-testid="Add"]')

# ❌ UNSTABLE - Button ID contains UUID
add_button = driver.find_element(By.ID, "btn_{UUID}")
```

---

### Checkbox Field: accountClearingFromLoan

**Enhanced Metadata**
- **Element Type:** input
- **Input Type:** checkbox
- **Selector:** `[name="accountClearingFromLoan"]` (stable)

**Interaction Pattern** (from recording):
```python
# Check the checkbox
clearing_checkbox = driver.find_element(By.NAME, "accountClearingFromLoan")
if not clearing_checkbox.is_selected():
    clearing_checkbox.click()
time.sleep(0.5)

# Verify state
is_clearing = clearing_checkbox.is_selected()
print(f"Clearing from loan: {is_clearing}")
```

**Usage Notes**:
- Checkbox state affects loan calculation logic
- When checked, indicates liability will be cleared from loan proceeds
- Recording shows this is frequently toggled during entry

---

### Recorded Usage Examples

**Institution Field**
```python
# Observed values in recording (examples):
institution_values = [
    "Commonwealth Bank",
    "NAB",
    "Westpac",
    # ... user tested multiple lenders
]
```

**Account Repayment**
```python
# Progressive typing observed (reveals user behavior):
repayment_values = [
    "5",      # Initial typing
    "50",
    "500",
    "5000",   # Final value
]
# Users type incrementally - automation should account for this
```

**Repayment Frequency**
```python
# All frequency options tested in recording:
frequencies_tested = [
    "Monthly",
    "Fortnightly",
    "Weekly",
    "Annual"
]
# Confirms all 4 options are functional
```

---

### relatedFields Arrays

From `elementContext.relatedFields` in the recording, the liability form structure includes:

**Primary Form Fields** (directly interacted):
1. `liabilityType` (select)
2. `institution` (select)
3. `accountName` (text input)
4. `accountBSB` (text input)
5. `accountNumber` (text input)
6. `limit` (text input)
7. `accountRepayment` (text input)
8. `accountRepaymentFrequency` (select)
9. `accountClearingFromLoan` (checkbox)
10. `priority` (select) **← NEW**

**Context Buttons** (appear in relatedFields but not clicked):
- Anonymous button (likely "Ownership Allocation" for dual applications)
- Anonymous button (likely "Evidence/Assign" for document linking)

**Form Structure**:
```
┌──────────────────────────────────────────────────────────┐
│ [Add Button] ← [data-testid="Add"] (STABLE)             │
├──────────────────────────────────────────────────────────┤
│ Liability Type:    [Personal Loan ▼]                    │
│ Institution:       [Commonwealth Bank ▼]                │
│ Account Name:      [My Loan Account   ]                 │
│ BSB:               [123-456           ]                  │
│ Account Number:    [12345678          ]                  │
│ Limit:             [50000             ]                  │
│ Repayment:         [500               ]                  │
│ Frequency:         [Monthly ▼]                           │
│ Priority:          [High ▼]            ← NEW             │
│ ☐ Clearing from loan                                     │
│                                                          │
│ [Ownership] [Evidence]  ← Context buttons               │
└──────────────────────────────────────────────────────────┘
```

---

## Interaction Frequency (from Recording)

| Field | Interactions | Notes |
|-------|-------------|-------|
| institution | 8+ | High usage - frequently changed |
| accountName | 6+ | Moderate usage |
| accountBSB | 6+ | Moderate usage |
| accountNumber | 6+ | Moderate usage |
| limit | 5+ | Moderate usage |
| accountRepayment | 8+ | High usage - frequently adjusted |
| accountRepaymentFrequency | 5+ | Moderate usage |
| accountClearingFromLoan | 4+ | Lower usage - not always needed |
| priority | 3+ | Lower usage - NEW field |

**Insights**:
- `institution` and `accountRepayment` are the most frequently modified fields
- Users often adjust repayment amounts multiple times before finalizing
- Checkbox fields are toggled less frequently (only when applicable)

---

## UUID Stability Warnings

**Fields with UUID concerns** (from recording analysis):

1. **Add Button ID**: `#btn_{UUID}` changes per session
   - **Solution**: Use `[data-testid="Add"]` instead

2. **Dropdown data-testid values**: May contain UUIDs per row
   - **Solution**: Use `#id` selectors instead

**Pattern Identified**:
- All form field `#id` selectors are **STABLE** ✅
- Button `#id` selectors may contain **UUIDs** ⚠️
- Use `[data-testid="Add"]` for Add button ✅

---

## Recommendations for liabilities.md

### 1. ADD New Field
Add `priority` field to the documented fields list with selector `#priority`

### 2. ENHANCE Existing Entries
For each field, consider adding:
```markdown
#### Element: [Field Name]
- **Field Name:** [name]
- **Selector:** [selector]
- **Type:** [type]
- **data-testid:** [value or "Contains UUID - DO NOT USE"]  ← ADD THIS
- **Validation:**
  - Required: [Yes/No]  ← ADD THIS
  - Pattern: [if applicable]  ← ADD THIS
- **Related Fields:** [list]  ← ADD THIS
- **Interaction Frequency:** [High/Medium/Low from recording]  ← ADD THIS
```

### 3. ADD Selector Stability Section
```markdown
## Selector Stability Notes

### ✅ STABLE Selectors (Safe for Automation)
- All form field `#id` selectors (institution, accountName, etc.)
- `[data-testid="Add"]` for Add button
- `[name="accountClearingFromLoan"]` for checkbox

### ⚠️ UNSTABLE Selectors (Avoid)
- Button IDs containing UUIDs: `#btn_{UUID}`
- Dropdown data-testid attributes may contain row-specific UUIDs
```

### 4. ADD Usage Examples Section
Include actual recorded values showing progressive typing behavior and all tested options.

---

## Implementation Priority

**High Priority**:
1. ✅ Add `priority` field (NEW field discovered)
2. ✅ Add UUID stability warnings to existing documentation
3. ✅ Document `[data-testid="Add"]` as recommended selector

**Medium Priority**:
1. Add interaction frequency metadata
2. Add relatedFields arrays to each field
3. Document checkbox-specific interaction patterns

**Low Priority**:
1. Add recorded value examples
2. Add progressive typing behavior notes

---

**Status**: ✅ Ready for integration into liabilities.md
**Method**: Supplement existing documentation - DO NOT REPLACE
**Extraction Source**: jlall.json recording (147 events, multiple liability entries)
