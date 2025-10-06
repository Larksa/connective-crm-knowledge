# Living Expenses - Detailed Automation Guide

> **Parent Reference**: [CONNECTIVE_CRM_KNOWLEDGE_ENHANCED.md](./CONNECTIVE_CRM_KNOWLEDGE_ENHANCED.md)
> **CRM Tab**: Financials → Living Expenses
> **Integration Status**: ✅ Patterns implemented in `living_expenses` sequence
> **Last Updated**: 2025-10-06

---

**🔗 Navigation**
- ⬆️ [Master Reference](./CONNECTIVE_CRM_KNOWLEDGE_ENHANCED.md)
- 📙 [Quick Reference](./AUTOMATION_QUICK_REFERENCE.md)
- 📓 [Workflow Guide](./CLAUDE.md)

---

## 📋 Table of Contents

1. [Overview](#overview)
2. [Navigation Path](#navigation-path)
3. [Complete Category List](#complete-category-list-22-categories)
4. [Category Selection Pattern](#category-selection-pattern)
5. [Form Fields Reference](#form-fields-reference)
6. [Workflow Patterns](#workflow-patterns)
7. [Element Positioning](#element-positioning-reference)
8. [Voice Annotation Insights](#voice-annotation-insights)
9. [Category-to-Selector Mapping](#complete-category-to-selector-mapping)
10. [Testing Checklist](#testing-checklist)
11. [Quick Start Guide](#quick-start-guide-for-ai-agent)
12. [Summary Statistics](#summary-statistics)

---

## Overview

### Purpose
The Living Expenses section in Connective Financial CRM captures detailed financial information for loan applications and financial assessments.

### User Workflow (From Voice Annotations)
1. **Living Expenses**: _"we have begun the living expenses we've never got this page now we're going to go through and add all the expenses and click the relevant Fields"_
2. **Dropdowns**: _"I've selected childcare and added it and as you'll see there are all these drop down I'm gonna click each field and add them"_

### Form Structure
- **Multi-select filter** for expense categories
- **Dynamic form fields** that appear based on category selection
- **Repeatable entries** for multiple items in same category

### ⚠️ Critical Requirements
- **Page Load Timeout**: 40+ seconds required (estimated from 39623ms automation hint)
- **Dropdown Interactions**: 2-5 seconds
- **Form Field Population**: 1-2 seconds
- **Multi-entry Workflow**: ~30 seconds per category
- **Total for 9 categories**: ~4 minutes 34 seconds (from recording)

---

## Navigation Path

### To Access Financials Section
```
1. Click: #financials > span.TabButton-module_tab-button-elem__AV3Ub:nth-of-type(2)
   Text: "Financials"

2. Section appears with tabs:
   - Living Expenses
   - Liabilities (accessible via same tab structure)
```

### Living Expenses Tab
```css
Selector: button.dropdown-toggle.btn.btn-light.btn-sm
Text: "Living Expense"
XPath: /html[1]/body[1]/div[1]/div[1]/div[3]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/button[1]
```

---

## Complete Category List (22 Categories)

All categories available in the Living Expenses dropdown:

| # | Category | ID/Selector | Position Known | Notes |
|---|----------|-------------|----------------|-------|
| 1 | **All / Clear All** | Filter control | ✓ (position 1) | Multi-select control |
| 2 | **Childcare** | `#type` option | ✓ (position 2) | Confirmed from recording |
| 3 | **Child & Spouse Maintenance** | `#type` option | ✓ (position 3) | Confirmed from recording |
| 4 | **Clothing & Personal Care** | `#type` option | ✓ (position 5) | Confirmed from recording |
| 5 | **Entertainment & Recreation** | `#type` option | Unknown | |
| 6 | **Groceries** | `#type` option | Unknown | Seen in recording |
| 7 | **Health & Medical** | `#type` option | Unknown | |
| 8 | **Higher Education & Vocational Fees** | `#type` option | Unknown | Partial capture in recording |
| 9 | **Home & Contents Insurance** | `#type` option | Unknown | |
| 10 | **Investment Property Costs (including Insurance)** | `#type` option | Unknown | Seen in recording |
| 11 | **Motor Vehicle Insurance** | `#type` option | Unknown | |
| 12 | **Motor Vehicle Running Costs** | `#type` option | Unknown | |
| 13 | **Other Expenses** | `#type` option | Unknown | |
| 14 | **Other Insurance** | `#type` option | Unknown | |
| 15 | **Personal Insurance (Life, Health, Sickness and Personal Accident)** | `#type` option | Unknown | Seen in recording |
| 16 | **Private School Fees** | `#type` option | Unknown | |
| 17 | **Public or Government Primary/Secondary School Fees** | `#type` option | Unknown | Partial in recording |
| 18 | **Recreation & Entertainment** | `#type` option | Unknown | Possible duplicate? |
| 19 | **Rent** | `#type` option | Unknown | |
| 20 | **Superannuation & Investments** | `#type` option | Unknown | |
| 21 | **Telephone & Internet** | `#type` option | Unknown | |
| 22 | **Transport** | `#type` option | ✓ (position 22) | Confirmed from recording |

> **Note on Positions**: Only categories clicked during the recording have confirmed nth-of-type positions. To discover all positions, capture a full dropdown interaction recording or inspect the live dropdown HTML.

---

## Category Selection Pattern

### Step 1: Open Multi-Select Filter
```javascript
// Click to open dropdown
Selector: ".dropdown-toggle.btn.btn-light.btn-sm"
Text: "Living Expense"
Classes: "dropdown-toggle btn btn-light btn-sm"
```

### Step 2: Select Category Checkbox
```javascript
// Example: Selecting Childcare
Selector: "#root > div > div.w-100.maf-app-container:nth-of-type(3) > ... > button.dropdown-item:nth-of-type(2) > div.custom-checkbox.custom-control > label.custom-control-label"

// Pattern for each category:
button.dropdown-item:nth-of-type(N) > div.custom-checkbox.custom-control > label.custom-control-label

Where N = category position:
- 2 = Childcare
- 3 = Child & Spouse Maintenance
- 5 = Clothing & Personal Care
- 22 = Transport
```

### Step 3: Form Auto-Populates
When a category is selected, the form displays:
- Type selector (pre-filled with category)
- Frequency selector
- Amount input field

---

## Form Fields Reference

### 1. Type Selector (Category)

```yaml
Field ID: #type
Element Type: select
Tag Name: select
Classes: "undefined form-item__element--select form-control"
```

**Options Format**:
```html
<select id="type" class="undefined form-item__element--select form-control">
  <option><Clear undefined></option>
  <option>Childcare</option>
  <option>Child & Spouse Maintenance</option>
  <option>Clothing & Personal Care</option>
  <option>Public or Government Primary</option>
  <!-- ... more options -->
</select>
```

**XPath**: `//*[@id="type"]`

---

### 2. Frequency Selector

```yaml
Field ID: #frequency
Element Type: select
Tag Name: select
Input Type: select-one
Classes: "undefined form-item__element--select form-control-sm form-control"
```

**Options** (4 frequencies):
```html
<select id="frequency" class="undefined form-item__element--select form-control-sm form-control">
  <option><Clear ></option>
  <option value="Annual">Annual</option>
  <option value="Monthly">Monthly</option>
  <option value="Fortnightly">Fortnightly</option>
  <option value="Weekly">Weekly</option>
</select>
```

**Element Dimensions**:
- Width: 169.59375px
- Height: 28px
- Position varies: top: 274.8125px - 461.375px (depending on entry)

**XPath**: `//*[@id="frequency"]`

**Default**: Usually "Monthly" (most common in recording)

---

### 3. Amount Input Field

```yaml
Field ID: #amount
Element Type: input
Tag Name: input
Input Type: text
Classes: "align-right border-radius-right form-control-sm form-control"
```

**Characteristics**:
- Right-aligned text (for currency display)
- Rounded border on right side
- Small form control size

**Element Dimensions**:
- Width: 145.71875px
- Height: 28px
- Position: left: 983.46875px (consistent)

**XPath**: `//*[@id="amount"]`

**Input Pattern Observed**:
```javascript
// User types incrementally: "3" → "30" → "300"
// Or: "2" → "20" → "200"
// Suggests numeric-only validation
```

---

## Workflow Patterns

### Pattern 1: Add Single Living Expense

```javascript
// Step 1: Click Living Expense dropdown
click('.dropdown-toggle.btn.btn-light.btn-sm')

// Step 2: Select category (e.g., Childcare)
click('button.dropdown-item:nth-of-type(2) > div.custom-checkbox.custom-control > label')

// Step 3: Form auto-fills category
waitForElement('#type') // Should show selected category

// Step 4: Select frequency
click('#frequency')
selectOption('#frequency', 'Annual') // or Monthly, Fortnightly, Weekly

// Step 5: Enter amount
click('#amount')
type('#amount', '300')

// Step 6: Repeat for next category
click('.dropdown-toggle.btn.btn-light.btn-sm')
// ... continue pattern
```

### Pattern 2: Add Multiple Expenses Rapidly

```javascript
// Observed pattern from recording:
// User adds 9 different expense categories in ~4 minutes

expenses = [
  { category: 2, frequency: 'Annual', amount: '200' },      // Childcare
  { category: 3, frequency: 'Fortnightly', amount: '500' }, // Child & Spouse
  { category: 5, frequency: 'Weekly', amount: '50' },       // Clothing
  // ... etc
]

for (expense of expenses) {
  openLivingExpenseDropdown()
  selectCategory(expense.category)
  selectFrequency(expense.frequency)
  enterAmount(expense.amount)
  // Form auto-saves or moves to next entry
}
```

---

## Element Positioning Reference

### Frequency Dropdown Positions
Observed top positions (varies by entry number):
- Entry 1: `top: 274.8125px`
- Entry 2: `top: 337px`
- Entry 3: `top: 399.1875px`
- Entry 4: `top: 461.375px`

**Pattern**: ~62px spacing between entries (vertical stacking)

### Amount Field Positions
Consistent left position: `left: 983.46875px`
Same vertical pattern as frequency field

**Use Case**: For visual validation in testing, elements should appear at predictable positions

---

## Voice Annotation Insights

### User Thought Process (Captured)

1. **Initial Approach**:
   > "we have begun the living expenses we've never got this page now we're going to go through and add all the expenses and click the relevant Fields"

   - User navigates to new page
   - Plans to add multiple expenses
   - Will click through fields systematically

2. **Dropdown Discovery**:
   > "I've selected childcare and added it and as you'll see there are all these drop down I'm gonna click each field and add them"

   - User discovers dropdown controls
   - Recognizes pattern: select category → fill fields
   - Plans to repeat for each expense

### AI Agent Implications

**For Training**:
- Emphasize the **repetitive pattern** (category → frequency → amount)
- Teach **dropdown navigation** as core skill
- Highlight **multi-entry workflow** (9+ categories common)

**For Automation**:
- Build **loop-based entry** functions
- Implement **category mapping** (name → nth-of-type position)
- Handle **dynamic field appearance** gracefully

---

## Complete Category-to-Selector Mapping

### Living Expense Categories

```javascript
const LIVING_EXPENSE_CATEGORIES = {
  // Category Name: nth-of-type position in dropdown
  // ✓ = Confirmed from recording, ? = Position needs discovery

  'All / Clear All': 1,                                                           // ✓ Multi-select control
  'Childcare': 2,                                                                 // ✓ Confirmed
  'Child & Spouse Maintenance': 3,                                                // ✓ Confirmed
  'Clothing & Personal Care': 5,                                                  // ✓ Confirmed (not sequential!)
  'Entertainment & Recreation': null,                                             // ? Position unknown
  'Groceries': null,                                                              // ? Seen in recording
  'Health & Medical': null,                                                       // ? Position unknown
  'Higher Education & Vocational Fees': null,                                     // ? Partial in recording
  'Home & Contents Insurance': null,                                              // ? Position unknown
  'Investment Property Costs (including Insurance)': null,                        // ? Seen in recording
  'Motor Vehicle Insurance': null,                                                // ? Position unknown
  'Motor Vehicle Running Costs': null,                                            // ? Position unknown
  'Other Expenses': null,                                                         // ? Position unknown
  'Other Insurance': null,                                                        // ? Position unknown
  'Personal Insurance (Life, Health, Sickness and Personal Accident)': null,     // ? Seen in recording
  'Private School Fees': null,                                                    // ? Position unknown
  'Public or Government Primary/Secondary School Fees': null,                     // ? Partial in recording
  'Recreation & Entertainment': null,                                             // ? Possible duplicate
  'Rent': null,                                                                   // ? Position unknown
  'Superannuation & Investments': null,                                           // ? Position unknown
  'Telephone & Internet': null,                                                   // ? Position unknown
  'Transport': 22                                                                 // ✓ Confirmed (far down list!)
}

// Note: Positions are NOT sequential (Childcare=2, Clothing=5, Transport=22)
// This suggests alphabetical ordering or categorization in the dropdown

// To select a category:
function selectLivingExpenseCategory(categoryPosition) {
  const selector = `button.dropdown-item:nth-of-type(${categoryPosition}) > div.custom-checkbox.custom-control > label.custom-control-label`
  document.querySelector(selector).click()
}
```

### Frequency Options

```javascript
const FREQUENCY_OPTIONS = {
  'Annual': 'Annual',
  'Monthly': 'Monthly',
  'Fortnightly': 'Fortnightly',
  'Weekly': 'Weekly'
}

// To select frequency:
function selectFrequency(frequency) {
  const select = document.querySelector('#frequency')
  select.value = frequency
  select.dispatchEvent(new Event('change'))
}
```

### Recommended Selector Strategy

**Instead of position-based**:
```python
# DON'T USE (brittle):
driver.find_element(By.CSS_SELECTOR, f'button.dropdown-item:nth-of-type({pos})')
```

**Use text-based (more reliable)**:
```python
# USE THIS (robust):
items = driver.find_elements(By.CSS_SELECTOR, 'button.dropdown-item')
for item in items:
    if category_name in item.text:
        item.find_element(By.TAG_NAME, 'label').click()
        break
```

---

## Testing Checklist

### Manual Testing Points
- [ ] Navigate to Financials tab successfully
- [ ] Open Living Expense dropdown
- [ ] Select each category and verify form appears
- [ ] Test all frequency options
- [ ] Enter various amount formats
- [ ] Verify multi-entry capability
- [ ] Check form persistence/clearing
- [ ] Test timeout thresholds (40s+)

### Automation Testing Points
- [ ] Selector reliability (CSS vs XPath)
- [ ] Wait time adequacy (40s+ for page load)
- [ ] Dynamic element detection
- [ ] Multi-entry loop execution
- [ ] Error handling for missing elements
- [ ] Form state validation
- [ ] Text-based category selection
- [ ] Frequency dropdown selection
- [ ] Amount input with various formats

---

## Quick Start Guide for AI Agent

### Minimal Viable Workflow

```python
# 1. Navigate to page
driver.get('https://crm.connective.com.au/#/')

# 2. Click Financials tab (WAIT for load - 40s timeout)
WebDriverWait(driver, 40).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '#financials > span'))
).click()

# 3. Open Living Expense dropdown
driver.find_element(By.CSS_SELECTOR, '.dropdown-toggle.btn.btn-light.btn-sm').click()

# 4. Select category (e.g., Childcare = position 2)
driver.find_element(By.CSS_SELECTOR,
    'button.dropdown-item:nth-of-type(2) > div.custom-checkbox > label').click()

# 5. Set frequency
Select(driver.find_element(By.ID, 'frequency')).select_by_value('Monthly')

# 6. Enter amount
driver.find_element(By.ID, 'amount').send_keys('300')

# 7. Repeat steps 3-6 for additional categories
```

### Error Handling Template

```python
def add_living_expense(category_position, frequency, amount):
    try:
        # Open dropdown with retry
        for attempt in range(3):
            try:
                dropdown = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, '.dropdown-toggle.btn.btn-light.btn-sm'))
                )
                dropdown.click()
                break
            except TimeoutException:
                if attempt == 2:
                    raise
                time.sleep(2)

        # Select category
        category_selector = f'button.dropdown-item:nth-of-type({category_position}) > div.custom-checkbox > label'
        driver.find_element(By.CSS_SELECTOR, category_selector).click()

        # Wait for form fields
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, 'frequency'))
        )

        # Set frequency
        Select(driver.find_element(By.ID, 'frequency')).select_by_value(frequency)

        # Enter amount
        amount_field = driver.find_element(By.ID, 'amount')
        amount_field.clear()
        amount_field.send_keys(str(amount))

        return True

    except Exception as e:
        print(f"Error adding expense: {e}")
        return False
```

---

## Summary Statistics

### Recording Data: Living Expenses
- **Duration**: 4m 34s (274 seconds)
- **Total Events**: 164
- **Clicks**: 135
- **Inputs**: 24
- **Voice Annotations**: 3
- **Categories Added**: ~9 different expense types
- **Average time per category**: ~30 seconds

### Key Metrics for Automation
- **Page Load Wait**: 40 seconds minimum
- **Field Interaction Wait**: 2-5 seconds
- **Multi-entry Capable**: Yes, tested with 9+ categories
- **Form Complexity**: Medium (3 fields per entry, dynamic loading)

---

## Known Behaviors & Gotchas

### ⏱️ Wait Times

**CRITICAL**: Long wait times detected in automation hints:
```json
"estimated_timeout_needed": 39623.92908,
"potential_issues": ["Long wait times detected - may need custom timeouts"]
```

**Recommendation**:
- Set timeout to **40+ seconds** for initial page load
- Individual field interactions: 2-5 seconds
- Use `waitForElement()` with extended timeouts

### 🔄 Dynamic Content Loading

**Behavior**:
- Categories load asynchronously
- Form fields appear/disappear based on selection
- Multi-select checkboxes rebuild on each open

**Strategy**:
```javascript
// Don't assume immediate availability
await waitFor(() => document.querySelector('#type'))
await waitFor(() => document.querySelector('#frequency'))

// Verify element is interactable
await waitForClickable('#amount')
```

### 📝 Form State Persistence

**Observed**:
- Previously entered values may persist
- Clearing selections requires explicit clicks
- "<Clear>" option appears in dropdowns

**Best Practice**:
```javascript
// Always check current value before setting
const currentValue = document.querySelector('#type').value
if (currentValue !== expectedValue) {
  selectOption('#type', expectedValue)
}
```

### 🎯 Multi-Select Filter Behavior

**Pattern**:
1. Click opens dropdown
2. Each category is a checkbox (can select multiple)
3. Form shows ALL selected categories
4. Each gets its own frequency + amount fields

**Gotcha**:
```javascript
// Clicking outside dropdown may close it
// Use explicit close/open for reliability
```

### 🔢 Numeric Input Handling

**Observed User Behavior**:
```javascript
// User types: "3" -> "30" -> "300"
// NOT: Types "300" directly

// Amount field accepts:
- Incremental typing (captured as separate events)
- No currency symbol in input
- Likely validates on blur/submit
```

**For Automation**:
```javascript
// Single setValue preferred over typing
document.querySelector('#amount').value = '300'
document.querySelector('#amount').dispatchEvent(new Event('input'))
document.querySelector('#amount').dispatchEvent(new Event('blur'))
```

### 📊 Frequency Defaults

**Most Common**: "Monthly" (appears as default in many entries)

**Full Options**:
- Annual (less common)
- Monthly (default/common)
- Fortnightly (moderate use)
- Weekly (occasional use)

**Tip**: If automating, check for "Monthly" pre-selection before changing

---

## Document History

| Date | Change | Source |
|------|--------|--------|
| 2025-10-06 | Initial creation from recording analysis | WorkflowCapture (connectivelivingexpenses.json) |
| 2025-10-06 | Extracted to modular structure | Knowledge base integration |

---

**🔗 Quick Links**
- ⬆️ [Back to Master Reference](./CONNECTIVE_CRM_KNOWLEDGE_ENHANCED.md)
- 📙 [Quick Reference for Coding](./AUTOMATION_QUICK_REFERENCE.md)
- 📓 [Workflow Implementation Guide](./CLAUDE.md)

---

*This detailed guide is part of the modular Connective CRM knowledge base. For strategic overview and pattern status, see the Master Reference.*
