# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

## 🎯 Project Purpose

This is a **knowledge base repository** (not application code) containing:
- Connective CRM field mappings and selectors
- Dropdown option lists (lenders, property types, brokers, etc.)
- Validated automation workflows
- MCP (Model Context Protocol) server for Claude Code integration
- Python SDK for querying CRM reference data

**Primary Users**: Mortgage broking teams automating Connective CRM data entry

---

## 🏗️ Architecture

### Repository Structure

```
connective-crm-knowledge/
├── knowledge/                              # Core knowledge base
│   └── COMPLETE_CONNECTIVE_CRM_REFERENCE.md  # 74 elements, 286+ dropdown options
├── mcp_server/
│   └── connective_crm_server.py           # MCP server for Claude Code integration
├── sdk/                                   # Python SDK for querying reference data
│   ├── __init__.py                        # Exports CRMReference class
│   ├── reference_loader.py                # Parses knowledge markdown → Python objects
│   ├── query_engine.py                    # Field lookups, validation, search
│   ├── fuzzy_matcher.py                   # Smart matching (CBA → Commonwealth Bank)
│   └── models.py                          # Data models (Element, Workflow, etc.)
└── examples/
    └── team-automation-template/          # Template for team automation projects
```

### Data Flow

```
COMPLETE_CONNECTIVE_CRM_REFERENCE.md
    ↓ (parsed by)
reference_loader.py
    ↓ (creates)
Python objects (Element, Workflow)
    ↓ (queried via)
query_engine.py ←→ MCP Server ←→ Claude Code
    ↓
fuzzy_matcher.py (handles abbreviations/typos)
```

---

## 🔧 Development Commands

### Testing SDK

```bash
# Test SDK can parse knowledge base
python -c "from sdk import CRMReference; crm = CRMReference(); print(crm.get_summary())"

# Test specific field lookup
python -c "from sdk import CRMReference; crm = CRMReference(); print(crm.get_selector('lender'))"

# Test fuzzy matching
python -c "from sdk import CRMReference; crm = CRMReference(); match = crm.fuzzy_match('lender', 'CBA'); print(f'{match.matched_value} ({match.confidence}%)')"

# Test dropdown validation
python -c "from sdk import CRMReference; crm = CRMReference(); print(crm.validate_dropdown('lender', 'Commonwealth Bank'))"
```

### Testing MCP Server

```bash
# Start MCP server (should run without errors)
python mcp_server/connective_crm_server.py

# Stop with Ctrl+C
```

### Git Workflow

```bash
# Update knowledge base
git pull origin main
# Edit knowledge/COMPLETE_CONNECTIVE_CRM_REFERENCE.md
python -c "from sdk import CRMReference; CRMReference()"  # Verify parsing works
git add knowledge/COMPLETE_CONNECTIVE_CRM_REFERENCE.md
git commit -m "Add new lender: [Name]"  # Use descriptive messages
git push origin main
```

---

## 📝 Knowledge Base Updates

### Critical: The Single Source of Truth

**All CRM knowledge lives in**: `knowledge/COMPLETE_CONNECTIVE_CRM_REFERENCE.md`

This markdown file is parsed by `reference_loader.py` into Python objects. Changes to this file automatically propagate to:
- SDK queries
- MCP server responses
- Team automation scripts (after `git pull`)

### Adding New Dropdown Options

Find the element section in the knowledge file and add alphabetically:

```markdown
#### Element: Lender
- **Field Name:** lender
- **Selector:** #lender
- **Type:** select
- **Options:**
  - AMP
  - ANZ
  - Commonwealth Bank
  - [NEW LENDER HERE]  ← Add alphabetically
  ...
```

### Adding New Fields

Follow this exact format:

```markdown
#### Element: [Field Name]
- **Field Name:** [camelCase]
- **Label:** [Human readable]
- **Selector:** [CSS selector - prefer data-testid > ID > class]
- **Type:** [input|select|textarea|button]
- **Options:** [if type is select]
  - Option 1
  - Option 2
- **Section:** [section_name]
- **Description:** [Purpose of field]
- **Fallback Selectors:** [Optional - for backwards compatibility]
  - [Alternative selector 1]
```

### Selector Priority

When adding selectors, follow this hierarchy:
1. `data-testid` attributes (most stable)
2. `id` attributes
3. Descriptive text content
4. Class names (least stable)

---

## 🧪 Testing Changes

**Always test before pushing**:

```bash
# 1. Pull latest
git pull origin main

# 2. Make changes to knowledge/COMPLETE_CONNECTIVE_CRM_REFERENCE.md

# 3. Verify SDK parses correctly
python -c "from sdk import CRMReference; CRMReference()"

# 4. Test specific changes
python -c "from sdk import CRMReference; crm = CRMReference(); print(crm.get_all_options('lender'))"

# 5. If all tests pass, commit
git add knowledge/COMPLETE_CONNECTIVE_CRM_REFERENCE.md
git commit -m "Descriptive message"
git push
```

---

## 🔑 Key Concepts

### Elements vs Workflows

- **Elements**: Individual form fields, buttons, dropdowns (74 total)
- **Workflows**: Multi-step processes combining elements (e.g., "add_note", "upload_file")

### Fuzzy Matching

The SDK automatically handles abbreviations and typos:
- "CBA" → "Commonwealth Bank" (95% confidence)
- "Comm Bank" → "Commonwealth Bank" (88% confidence)

Uses `rapidfuzz` library for smart matching.

### MCP Integration

When properly configured in `.claude.json`, Claude Code can:
- Look up field selectors instantly
- Validate dropdown values before automation
- Get complete lists of options
- Suggest corrections for typos/abbreviations

---

## 📊 Statistics

Current knowledge base contains:
- **74 elements** across 8 sections
- **54 lenders**
- **19 brokers/agents**
- **63 property types**
- **18 liability types**
- **6 transaction types**
- **286+ total dropdown options**

Update these counts in README.md when making significant changes.

---

## ⚠️ Important Notes

### Breaking Changes

If updating selectors that may break existing automations:

1. Add old selector as fallback:
   ```markdown
   - **Selector:** #new-selector
   - **Fallback Selectors:**
     - #old-selector  ← Keep for compatibility
   ```

2. Use "BREAKING:" prefix in commit message:
   ```bash
   git commit -m "BREAKING: Update lender selector (Connective UI change)"
   ```

3. Notify team immediately to update automation scripts

### Security

This repo contains:
- ✅ Field selectors and navigation workflows
- ✅ Dropdown option lists
- ❌ NO credentials, API keys, or client data

Safe to share within team.

---

## 🎓 For New Contributors

1. Read this CLAUDE.md first
2. Review `README.md` for setup instructions
3. See `KNOWLEDGE_UPDATES.md` for detailed update procedures
4. Check `QUICK_REFERENCE.md` for common commands
5. Test locally before pushing changes

**Essential principle**: The knowledge base must always be parseable by the SDK. Test before every commit.

---

## 📞 Getting Help

- **Documentation**: See guides in root directory
- **Issues**: https://github.com/Larksa/connective-crm-knowledge/issues
- **Discussions**: https://github.com/Larksa/connective-crm-knowledge/discussions
