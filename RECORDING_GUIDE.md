# Recording Guide for Connective CRM Documentation

**Purpose**: Guide for creating effective recordings to extract workflows and field metadata

**Last Updated**: 2025-10-08

---

## 📋 Quick Reference

| Recording Type | Duration | Purpose | Label When Submitting |
|----------------|----------|---------|----------------------|
| **Workflow** | 2-3 mins | Clean step-by-step process | "Workflow recording for [section]" |
| **Field Discovery** | 5-10 mins | Test all fields/options | "Field discovery for [section]" |
| **Comprehensive** | 7-15 mins | Both workflow + all fields | "Comprehensive recording for [section]" |
| **Edge Case** | 1-3 mins | Special scenarios | "[Scenario] edge case for [section]" |

---

## 🎯 Recording Types Explained

### Type 1: Workflow Recording ⚡ (PRIORITY)

**Goal**: Capture ONE clean, perfect example from start to finish

**Duration**: 2-3 minutes

**Focus On**:
- ✅ Navigation path (which tabs to click)
- ✅ Field order (which fields to fill first)
- ✅ Timing (wait for page loads, auto-save)
- ✅ Common/typical values
- ✅ Happy path only (no errors)

**Do NOT**:
- ❌ Test every dropdown option
- ❌ Fill optional fields
- ❌ Click extra buttons
- ❌ Test edge cases

**Example Session: "Add Liability Workflow"**
```
1. Click Financials tab → wait 1s
2. Click Liabilities → wait 2s
3. Click Add button → wait 1s
4. Select "Credit Card" from liability type
5. Enter "Commonwealth Bank" in institution
6. Enter "Personal Card" in account name
7. Enter "5000" in balance
8. Enter "15000" in limit
9. Enter "250" in repayment
10. Select "Monthly" from frequency
11. Wait 2 seconds (auto-save)
12. DONE ✅
```

**Result**: Clean queryable workflow that can be added to MCP

---

### Type 2: Field Discovery Recording 🔍 (WHEN TIME PERMITS)

**Goal**: Test EVERYTHING - all fields, all options, all buttons

**Duration**: 5-10 minutes

**Focus On**:
- ✅ Test ALL dropdown options (all 18 liability types)
- ✅ Fill ALL fields (including optional ones)
- ✅ Click ALL buttons (ownership, evidence, etc.)
- ✅ Test conditional fields (vehicleType, ABN, etc.)
- ✅ Try different values (long text, numbers, dates)
- ✅ Observe validation (what's required? what's optional?)

**Do NOT**:
- ❌ Worry about speed
- ❌ Skip any options
- ❌ Ignore anonymous buttons

**Example Session: "Liabilities Field Discovery"**
```
1. Add liability #1: Test "Buy Now Pay Later"
   - Fill ALL fields (even optional BSB, account number)
   - Click ownership button (even if not needed)
   - Click evidence button
   - Test priority dropdown (all options)
   - Check "clearing from loan" checkbox

2. Add liability #2: Test "Car Loan"
   - Fill all fields again
   - Test different values

3. Continue through ALL 18 liability types...

4. Test edge cases:
   - Leave required fields empty (validation?)
   - Enter very long account name
   - Try negative balance
```

**Result**: Complete field metadata, all dropdown options verified, conditional fields discovered

---

### Type 3: Comprehensive Recording 📦 (BEST OF BOTH)

**Goal**: Capture workflow AND thoroughly test fields in ONE session

**Duration**: 7-15 minutes

**Focus On**:
- ✅ Start with clean workflow (first entry)
- ✅ Then systematically test remaining options
- ✅ Balance speed with thoroughness

**Structure**:
```
Part 1 (3 mins): Clean workflow
- One perfect example start to finish

Part 2 (7 mins): Field discovery
- Test remaining options
- Click all buttons
- Fill all fields
```

**Example Session: "Assets - Other Comprehensive"**
```
Part 1: Workflow (3 mins)
1. Navigate to Assets - Other
2. Add one "Boat" asset
3. Fill core fields (name, value, basis)
4. Complete and save

Part 2: Field Discovery (7 mins)
1. Add "Motor Vehicle" → discover vehicleType field!
2. Test all 18 asset types
3. Test all value basis options
4. Test all vehicle types (if Motor Vehicle)
5. Click ownership button
6. Click evidence button
```

**Result**: Both queryable workflow AND complete field documentation

---

### Type 4: Edge Case Recording 🎯 (AS DISCOVERED)

**Goal**: Document specific scenarios, conditional logic, or error states

**Duration**: 1-3 minutes

**Focus On**:
- ✅ Specific trigger condition
- ✅ What changes when condition is met
- ✅ Validation errors
- ✅ Conditional field appearance

**Examples**:

**"Motor Vehicle Conditional Field"**
```
1. Add asset
2. Select "Motor Vehicle"
3. → vehicleType field appears!
4. Test all vehicle types
```

**"Dual Applicant Ownership"**
```
1. Add liability
2. Click ownership button
3. → Allocation modal appears
4. Test "Allocate Evenly" vs "Custom"
```

**"Self-Employed ABN Field"**
```
1. Add employment
2. Select "Self-Employed"
3. → ABN field appears!
4. Test ABN validation
```

**Result**: Edge case documentation added to relevant workflow/field docs

---

## 📝 How to Label Recordings When Submitting

### For Workflow Recordings

**Use this phrase**:
```
"Workflow recording for [SECTION NAME]"
```

**Examples**:
- "Workflow recording for Employment"
- "Workflow recording for Real Estate Assets"
- "Quick workflow for Details section"
- "Happy path for Other Income"

---

### For Field Discovery Recordings

**Use this phrase**:
```
"Field discovery for [SECTION NAME]"
```

**Examples**:
- "Field discovery for Liabilities"
- "Complete field test for Living Expenses"
- "All options test for Assets - Other"

---

### For Comprehensive Recordings

**Use this phrase**:
```
"Comprehensive recording for [SECTION NAME]"
```

**Examples**:
- "Comprehensive recording for Employment"
- "Full documentation for Real Estate Assets"

---

### For Edge Case Recordings

**Use this phrase**:
```
"[SCENARIO] edge case for [SECTION]"
```

**Examples**:
- "Motor Vehicle edge case for Assets"
- "Dual applicant workflow for Liabilities"
- "Self-employed ABN field for Employment"
- "Validation testing for Living Expenses"

---

## 🎬 Recording Best Practices

### Before Recording

**1. Plan Your Approach**
- [ ] Decide: Workflow, Field Discovery, or Comprehensive?
- [ ] Know which section you're documenting
- [ ] Have test data ready (names, numbers, values)

**2. Prepare the CRM**
- [ ] Login to Connective CRM
- [ ] Navigate to relevant opportunity/application
- [ ] Clear any existing test data (fresh start)

**3. Start WorkflowCapture**
- [ ] Launch recording tool
- [ ] Give recording a descriptive name
- [ ] Add description noting the type and section

---

### During Recording

**For Workflows** (2-3 mins):
- [ ] Take your time - quality over speed
- [ ] Wait for page loads (don't rush)
- [ ] Use typical/common values
- [ ] Complete one perfect example
- [ ] Verify entry saved before stopping

**For Field Discovery** (5-10 mins):
- [ ] Be systematic - test options in order
- [ ] Click every button at least once
- [ ] Try different data types (text, numbers, dates)
- [ ] Note any validation messages
- [ ] Test optional vs required fields

**For Comprehensive** (7-15 mins):
- [ ] Start with clean workflow (first 3 mins)
- [ ] Then switch to field discovery mode
- [ ] Balance thoroughness with time

**For Edge Cases** (1-3 mins):
- [ ] Focus ONLY on the specific scenario
- [ ] Demonstrate the trigger condition
- [ ] Show what changes/appears
- [ ] Keep it short and focused

---

### After Recording

**1. Review the Recording**
- [ ] Playback to verify quality
- [ ] Check all interactions were captured
- [ ] Ensure no sensitive data visible

**2. Export the JSON**
- [ ] Save to appropriate location
- [ ] Use descriptive filename (e.g., `employment_workflow_2025-10-08.json`)

**3. Submit for Processing**
- [ ] Provide file path
- [ ] Label clearly: "Workflow recording for Employment"
- [ ] Mention any special notes or discoveries

---

## 📊 Recommended Recording Priority

### Phase 1: Quick Wins (7-10 minutes total)
Record **workflow-focused sessions** for high-value sections:

**Priority 1** (Most valuable):
- [ ] Employment (2 mins)
- [ ] Real Estate Assets (3 mins)
- [ ] Details section (2 mins)

**Result**: 3 new queryable workflows

---

### Phase 2: Field Discovery (Later)
When you have more time, record **field discovery** for:

**Priority 2** (Complex sections):
- [ ] Employment (all types, conditional ABN field)
- [ ] Real Estate (all property types, conditional fields)
- [ ] Living Expenses (all 22 categories)

**Result**: Complete field metadata for remaining sections

---

### Phase 3: Edge Cases (As Discovered)
Record **edge cases** as you encounter them:

**Priority 3** (Document as found):
- [ ] Motor Vehicle conditional field
- [ ] Dual applicant workflows
- [ ] Self-employed ABN field
- [ ] Validation error states

**Result**: Edge case documentation

---

## 💡 Tips for Great Recordings

### DO ✅

**Workflow Recordings**:
- ✅ Use common, realistic values
- ✅ Wait for page loads and auto-saves
- ✅ Follow natural user flow
- ✅ Complete one entry fully

**Field Discovery**:
- ✅ Test systematically (Type 1, Type 2, Type 3...)
- ✅ Click every button at least once
- ✅ Fill every field (even optional)
- ✅ Note which fields are required

**All Recordings**:
- ✅ Go at a natural pace
- ✅ Wait for elements to load
- ✅ Verify saves before moving on
- ✅ Use descriptive values ("Personal Card" not "test")

---

### DON'T ❌

**Workflow Recordings**:
- ❌ Test every option (save for field discovery)
- ❌ Rush through steps
- ❌ Skip navigation (start from dashboard)
- ❌ Click random buttons

**Field Discovery**:
- ❌ Skip any options
- ❌ Ignore anonymous buttons
- ❌ Rush (thoroughness matters)

**All Recordings**:
- ❌ Include sensitive client data
- ❌ Switch windows mid-recording
- ❌ Edit/delete entries during recording
- ❌ Record errors unless testing validation

---

## 🔄 What Happens After Submission

### When You Say: "Workflow recording for Employment"

**I Will**:
1. ✅ Extract navigation path and timing
2. ✅ Identify core field selectors
3. ✅ Create queryable workflow structure
4. ✅ Add to COMPLETE_CONNECTIVE_CRM_REFERENCE.md
5. ✅ Update SDK to parse new workflow
6. ✅ Test workflow is queryable via MCP

**You Get**:
- Queryable workflow in MCP: `crm.get_workflow("add_employment")`
- Step-by-step documentation with selectors
- Python code examples
- Critical timing requirements

---

### When You Say: "Field discovery for Employment"

**I Will**:
1. ✅ Extract ALL fields and selectors
2. ✅ Capture all dropdown options
3. ✅ Identify conditional fields
4. ✅ Document validation rules
5. ✅ Create field supplement document

**You Get**:
- Complete field metadata (selector, type, options, validation)
- Conditional field triggers documented
- All dropdown options verified
- Field relationship structure

---

### When You Say: "Comprehensive recording for Real Estate"

**I Will**:
1. ✅ Extract workflow from clean first example
2. ✅ Extract complete field metadata from testing
3. ✅ Create BOTH queryable workflow AND field supplement
4. ✅ Compare with existing docs (NEW vs VERIFIED vs ENHANCED)

**You Get**:
- Queryable workflow + complete field documentation
- Best of both approaches

---

### When You Say: "Motor Vehicle edge case for Assets"

**I Will**:
1. ✅ Document conditional trigger (Motor Vehicle → vehicleType)
2. ✅ Add note to assets_other workflow
3. ✅ Update field metadata with conditional logic

**You Get**:
- Edge case documented in workflow
- Conditional field logic preserved

---

## 📋 Example Recording Sessions

### Example 1: Employment Workflow (2 mins)

**Label**: "Workflow recording for Employment"

**What to do**:
```
1. Start at dashboard
2. Navigate to Employment tab
3. Click Add button
4. Select "PAYG Employee" (most common)
5. Fill employer name: "Acme Corporation"
6. Fill occupation: "Software Engineer"
7. Fill start date: "2020-01-15"
8. Fill gross salary: "120000"
9. Select frequency: "Annual"
10. Wait for auto-save
11. Stop recording ✅
```

**Duration**: ~2 minutes

**What I'll create**:
- Queryable workflow: `crm.get_workflow("add_employment")`
- 10 steps with selectors and timing

---

### Example 2: Living Expenses Field Discovery (8 mins)

**Label**: "Field discovery for Living Expenses"

**What to do**:
```
1. Add expense #1: Select "Groceries"
   - Test frequency: Annual
   - Enter amount: 1500
   - Save

2. Add expense #2: Select "Utilities"
   - Test frequency: Monthly
   - Enter amount: 300
   - Save

3. Continue through ALL 22 categories:
   - Childcare
   - Child support
   - Education
   - Entertainment
   - Fuel
   - ... etc (all 22)

4. For each, test different:
   - Frequencies (Annual, Monthly, Fortnightly, Weekly)
   - Amounts (various values)
```

**Duration**: ~8 minutes

**What I'll create**:
- Field supplement for living_expenses.md
- All 22 categories verified
- All frequency options confirmed
- Amount field validation documented

---

### Example 3: Real Estate Comprehensive (12 mins)

**Label**: "Comprehensive recording for Real Estate Assets"

**What to do**:
```
Part 1: Workflow (3 mins)
1. Navigate to Real Estate Assets
2. Add ONE property (Owner Occupied House)
3. Fill all core fields
4. Complete and save

Part 2: Field Discovery (9 mins)
1. Test property types (House, Unit, Townhouse, Land, etc.)
2. Test occupancy types (Owner Occupied, Investment, etc.)
3. Fill all fields (address, value, basis)
4. Test conditional fields (if any appear)
5. Click ownership button
6. Click evidence button
7. Test all dropdown options systematically
```

**Duration**: ~12 minutes

**What I'll create**:
- Queryable workflow: `crm.get_workflow("add_real_estate")`
- Complete field supplement
- All property types verified
- Conditional fields documented

---

### Example 4: Self-Employed Edge Case (2 mins)

**Label**: "Self-employed ABN field edge case for Employment"

**What to do**:
```
1. Navigate to Employment
2. Click Add
3. Select "Self-Employed" from employment type
4. → ABN field appears! (conditional)
5. Test ABN field (enter valid ABN: "12 345 678 901")
6. Fill other fields as needed
7. Verify ABN field only appears for Self-Employed
8. Stop recording ✅
```

**Duration**: ~2 minutes

**What I'll create**:
- Edge case note added to add_employment workflow
- Conditional field documentation: ABN only for Self-Employed
- Validation pattern documented

---

## 🚀 Quick Start Checklist

**For Your Next Recording Session**:

- [ ] **Decide** which type: Workflow, Field Discovery, or Comprehensive
- [ ] **Prepare** test data and login to CRM
- [ ] **Start** WorkflowCapture with descriptive name
- [ ] **Record** following the appropriate guidelines above
- [ ] **Review** recording to verify quality
- [ ] **Export** JSON file
- [ ] **Submit** with clear label: "Workflow recording for [section]"

---

## 📞 Submission Template

When providing a recording, use this template:

```
I have a [TYPE] recording for [SECTION]:

File path: C:\path\to\recording.json
Type: [Workflow | Field Discovery | Comprehensive | Edge Case]
Section: [Employment | Real Estate | etc.]
Notes: [Any special observations, discoveries, or issues]

Please extract accordingly.
```

**Example**:
```
I have a workflow recording for Employment:

File path: C:\Downloads\employment_workflow_2025-10-08.json
Type: Workflow
Section: Employment
Notes: Focused on PAYG employee (most common). Did not test
       self-employed or contractor types.

Please extract accordingly.
```

---

## ✅ Summary

**Remember**:
1. **Workflow recordings** = Quick & clean (2-3 mins) → Queryable workflows
2. **Field discovery** = Thorough & systematic (5-10 mins) → Complete metadata
3. **Comprehensive** = Both in one (7-15 mins) → Best of both
4. **Edge cases** = Specific scenarios (1-3 mins) → Document conditionals

**Label clearly** when submitting:
- "Workflow recording for [section]"
- "Field discovery for [section]"
- "Comprehensive recording for [section]"
- "[Scenario] edge case for [section]"

**Start with workflows** (quick wins), add field discovery later when you have time!

---

**Questions?** Just say:
- "I have a workflow recording for X" → I'll extract workflow
- "I have field discovery for X" → I'll extract all fields
- "I have a comprehensive recording for X" → I'll extract both
- "I have [scenario] edge case" → I'll document the edge case

Happy recording! 🎬
