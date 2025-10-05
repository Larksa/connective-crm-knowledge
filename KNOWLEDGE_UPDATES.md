# Knowledge Updates Guide

**How to maintain and update the Connective CRM knowledge base**

---

## 🎯 Overview

This knowledge base is a **living document** that needs updates when:
- Connective adds new fields
- Dropdown options change (new lenders, brokers)
- Field selectors change (UI updates)
- Workflows are discovered or modified

**Who should update?**
- Anyone on the team who discovers changes
- Team lead reviews and approves major changes

---

## 📋 Quick Update Process

### Simple Updates (No Review Needed)

**Examples:** Adding a new lender, updating broker list, fixing typos

```bash
# 1. Pull latest
cd ~/connective-crm-knowledge
git pull origin main

# 2. Edit knowledge file
nano knowledge/COMPLETE_CONNECTIVE_CRM_REFERENCE.md
# OR use your favorite editor

# 3. Test locally
python -c "from sdk import CRMReference; crm = CRMReference(); print(crm.get_summary())"

# 4. Commit and push
git add knowledge/COMPLETE_CONNECTIVE_CRM_REFERENCE.md
git commit -m "Add new lender: [Lender Name]"
git push origin main

# 5. Notify team
# Slack/Email: "Knowledge base updated! Please run: cd ~/connective-crm-knowledge && git pull"
```

---

## 🔍 When Connective Changes

### Scenario 1: New Dropdown Option

**Example:** Connective adds a new lender "Example Bank"

1. **Document the change:**
   ```bash
   cd ~/connective-crm-knowledge
   git pull
   ```

2. **Edit reference file:**
   ```bash
   nano knowledge/COMPLETE_CONNECTIVE_CRM_REFERENCE.md
   ```

3. **Find the lender section:**
   ```markdown
   #### Element: Lender
   - **Field Name:** lender
   - **Selector:** #lender
   - **Type:** select
   - **Options:**
     - AMP
     - ANZ
     ...
     - Westpac
   ```

4. **Add new option (alphabetically):**
   ```markdown
     - Example Bank
   ```

5. **Test:**
   ```bash
   python -c "from sdk import CRMReference; crm = CRMReference(); print(len(crm.get_all_options('lender')))"
   # Should be one more than before
   ```

6. **Commit:**
   ```bash
   git add knowledge/COMPLETE_CONNECTIVE_CRM_REFERENCE.md
   git commit -m "Add new lender: Example Bank"
   git push
   ```

---

### Scenario 2: Field Selector Changed

**Example:** Property Type selector changed from `#propertyType` to `#property-type`

1. **Document the OLD selector:**
   ```bash
   # Screenshot or note the old selector
   ```

2. **Update reference:**
   ```markdown
   #### Element: Property Type
   - **Field Name:** propertyType
   - **Selector:** #property-type  ← CHANGED
   - **Fallback Selectors:**
     - #propertyType  ← ADD OLD AS FALLBACK
     - [data-testid="property-type"]
   ```

3. **Test with real page:**
   ```python
   # In automation script
   element = crm.get_selector("propertyType")
   print(element.selector)  # Should show new selector
   print(element.fallback_selectors)  # Should include old one
   ```

4. **Commit:**
   ```bash
   git commit -m "Update propertyType selector (Connective UI change)"
   ```

---

### Scenario 3: Entirely New Field

**Example:** Connective adds "Solar Panel Rebate" field

1. **Inspect the field in Connective:**
   - Right-click → Inspect Element
   - Note: ID, name, type, options (if dropdown)

2. **Add to reference file:**
   ```markdown
   #### Element: Solar Panel Rebate
   - **Field Name:** solarPanelRebate
   - **Label:** Solar Panel Rebate
   - **Selector:** #solarPanelRebate
   - **Type:** select
   - **Options:**
     - Yes
     - No
   - **Section:** property_assets
   - **Description:** Indicates if property qualifies for solar panel rebate
   ```

3. **Test:**
   ```python
   from sdk import CRMReference
   crm = CRMReference()
   result = crm.get_selector("solarPanelRebate")
   print(result)  # Should find the new field
   ```

4. **Commit:**
   ```bash
   git commit -m "Add new field: Solar Panel Rebate"
   ```

---

### Scenario 4: Broker/Agent List Updated

**Example:** New team member "Jane Smith" added as broker

1. **Edit broker section:**
   ```markdown
   #### Element: Agent/Broker
   - **Field Name:** agent
   - **Selector:** #agent
   - **Type:** select
   - **Options:**
     - Andrew Larkey
     - James Curtis
     - Jane Smith  ← NEW
     ...
   ```

2. **Commit:**
   ```bash
   git commit -m "Add new broker: Jane Smith"
   ```

---

## ✅ Testing Your Changes

### Test 1: SDK Can Parse
```bash
cd ~/connective-crm-knowledge
source venv/bin/activate
python -c "from sdk import CRMReference; crm = CRMReference(); print('✅ Parsed OK')"
# Should print: ✅ Parsed OK
```

### Test 2: Count Updated
```bash
python -c "from sdk import CRMReference; crm = CRMReference(); print(crm.get_summary())"
# Check counts match your expectations
```

### Test 3: Specific Field
```bash
python -c "from sdk import CRMReference; crm = CRMReference(); print(crm.get_selector('field_name'))"
# Should return your new/updated field
```

### Test 4: Dropdown Options
```bash
python -c "from sdk import CRMReference; crm = CRMReference(); print(crm.get_all_options('lender'))"
# Should include new lender
```

---

## 📝 Commit Message Guidelines

### Good Commit Messages

✅ `Add new lender: Example Bank`
✅ `Update propertyType selector (Connective UI change 2025-10-06)`
✅ `Add 3 new brokers: Jane Smith, John Doe, Mary Johnson`
✅ `Fix typo in lender name: Commomwealth → Commonwealth`
✅ `Add new field: Solar Panel Rebate (property_assets section)`

### Bad Commit Messages

❌ `update`
❌ `fixes`
❌ `changed stuff`
❌ `asdf`

**Format:**
```
[Action] [What]: [Details]

Examples:
Add new lender: XYZ Bank
Update lender selector: #lender → #lender-select
Fix typo: Commonweath Bank → Commonwealth Bank
```

---

## 🔄 Pull Request Workflow (Optional)

For major changes, use Pull Requests for review:

```bash
# 1. Create branch
git checkout -b add-new-fields-oct-2025

# 2. Make changes
nano knowledge/COMPLETE_CONNECTIVE_CRM_REFERENCE.md

# 3. Commit
git add knowledge/COMPLETE_CONNECTIVE_CRM_REFERENCE.md
git commit -m "Add 5 new property fields from Connective update"

# 4. Push branch
git push origin add-new-fields-oct-2025

# 5. Create PR on GitHub
# Team lead reviews and merges
```

---

## 🗓️ Maintenance Schedule

### Weekly (Team Lead)
- [ ] Check for Connective UI changes
- [ ] Review any team-submitted updates
- [ ] Test MCP still works
- [ ] Notify team of updates

### Monthly (Team)
- [ ] Review accuracy of all dropdowns
- [ ] Check for deprecated fields
- [ ] Update broker/agent list
- [ ] Verify workflows still valid

### After Connective Updates (Anyone)
- [ ] Test automation scripts
- [ ] Note any breaking changes
- [ ] Update knowledge base ASAP
- [ ] Test and push updates

---

## 🚨 Breaking Changes

**If a change will break existing automations:**

1. **Document the change clearly:**
   ```markdown
   <!-- BREAKING CHANGE 2025-10-06:
   propertyType selector changed from #propertyType to #property-type
   Old selector added as fallback for compatibility
   -->
   ```

2. **Add fallback selector:**
   ```markdown
   - **Selector:** #property-type
   - **Fallback Selectors:**
     - #propertyType  ← OLD (still works for now)
   ```

3. **Commit with BREAKING prefix:**
   ```bash
   git commit -m "BREAKING: Update propertyType selector (Connective UI change)"
   ```

4. **Notify team immediately:**
   > 🚨 **Breaking Change Alert**
   >
   > Property Type selector changed in Connective
   > Old: `#propertyType`
   > New: `#property-type`
   >
   > Action needed: Update automation scripts if using hardcoded selectors
   > Knowledge base updated with fallback for compatibility

---

## 📊 Version Tracking

### Simple Versioning

Update README.md version when making significant changes:

```markdown
**Version:** 1.1.0  ← Increment
**Last Updated:** 2025-10-06  ← Update date
```

**Version scheme:**
- `1.0.0` → `1.0.1` = Minor update (new lender, typo fix)
- `1.0.0` → `1.1.0` = New fields added (5+ changes)
- `1.0.0` → `2.0.0` = Major restructure or breaking changes

### Changelog (Optional)

Add to README or create CHANGELOG.md:

```markdown
## Changelog

### v1.1.0 (2025-10-06)
- Added 3 new lenders: Example Bank, Sample Credit Union, Demo Finance
- Updated broker list (added Jane Smith, removed John Retired)
- Fixed typo in Commonwealth Bank name

### v1.0.1 (2025-09-30)
- Fixed property type selector (Connective UI change)
- Added fallback selector for compatibility

### v1.0.0 (2025-09-15)
- Initial release
- 74 elements, 54 lenders, 19 brokers
```

---

## 🎓 Knowledge Structure Reference

### Required Fields for Each Element

```markdown
#### Element: [Field Name]
- **Field Name:** [camelCase name]
- **Label:** [Human readable label]
- **Selector:** [CSS selector]
- **Type:** [input/select/textarea/etc]
- **Options:** [if type is select]
  - Option 1
  - Option 2
- **Section:** [section name]
- **Description:** [What this field is for]
- **Fallback Selectors:** [Optional]
  - [Alternative selector 1]
  - [Alternative selector 2]
```

### Sections

Valid section names:
- `applicant_information`
- `property_assets`
- `employment_income`
- `liabilities`
- `finance_details`
- `home_loans_finance`

---

## 💡 Tips for Updating

### Tip 1: Always Pull First
```bash
git pull origin main  # Get latest before editing
```

### Tip 2: Test Before Pushing
```bash
python -c "from sdk import CRMReference; CRMReference()"
# Must work before pushing
```

### Tip 3: Use Descriptive Commits
Makes it easy to find changes later

### Tip 4: Update Documentation Too
If adding new fields, update README.md stats

### Tip 5: Notify Team
After pushing major updates, tell the team to pull

---

## 🔍 Discovering Field Information

### Method 1: Browser Inspector

1. Open Connective CRM
2. Right-click field → Inspect
3. Look for:
   - `id=` attribute (becomes `#id`)
   - `name=` attribute
   - `data-testid=` attribute

### Method 2: Discovery Agent (Advanced)

If you have the full connective-intelligence project:

```bash
cd ~/connective-intelligence
python scripts/01_discover_manual.py --focus-area home_loans_finance
# Generates comprehensive field documentation
```

### Method 3: Network Tab

1. Open Browser DevTools → Network
2. Interact with Connective form
3. Look at POST request payload
4. Field names are in the JSON data

---

## 📞 Questions?

**Before updating:**
- Check this guide
- Search existing commits: `git log --grep="lender"`
- Ask team lead if unsure

**After updating:**
- Test locally
- Notify team
- Monitor for issues

---

## ✅ Update Checklist

Before pushing changes:

- [ ] Pulled latest: `git pull`
- [ ] Made changes to knowledge file
- [ ] Tested parsing: SDK loads without errors
- [ ] Tested specific fields work
- [ ] Used descriptive commit message
- [ ] Pushed to GitHub
- [ ] Notified team (for major changes)

---

**Remember:** The knowledge base is the foundation of all team automations. Keep it accurate and up-to-date!
