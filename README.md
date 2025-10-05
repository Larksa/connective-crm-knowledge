# Connective CRM Knowledge Base

> **MCP Server for mortgage broking automation**
> Provides instant access to Connective CRM field selectors, lenders, brokers, and validation logic.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

---

## 🎯 What This Does

This MCP (Model Context Protocol) server gives you **instant answers** about Connective CRM fields:

- ✅ **Field selectors** - "What's the selector for lender?" → `#lender`
- ✅ **Valid options** - "List all lenders" → 54 lenders with exact names
- ✅ **Smart matching** - "Is 'CBA' valid?" → Matches to "Commonwealth Bank" (95% confidence)
- ✅ **Validation** - Check CSV/Excel data before automation
- ✅ **Workflows** - Step-by-step navigation instructions

**Perfect for:** Mortgage broking teams automating Connective CRM data entry.

---

## 🚀 Quick Setup (Team Members)

### Step 1: Clone Repository

```bash
cd ~
git clone https://github.com/Larksa/connective-crm-knowledge.git
cd connective-crm-knowledge
```

### Step 2: Install Dependencies

```bash
# Create virtual environment
python3 -m venv venv  # Mac/Linux
# OR
py -m venv venv       # Windows

# Activate it
source venv/bin/activate  # Mac/Linux
# OR
venv\Scripts\activate     # Windows

# Install
pip install -r requirements.txt
```

### Step 3: Test MCP Server

```bash
python mcp_server/connective_crm_server.py
```

**Expected:** Server starts without errors
**To stop:** Press `Ctrl+C`

### Step 4: Configure Claude Code

Add to your automation project's `.claude.json`:

**Mac/Linux:**
```json
{
  "mcpServers": {
    "connective-crm": {
      "command": "python",
      "args": [
        "/Users/YOUR_USERNAME/connective-crm-knowledge/mcp_server/connective_crm_server.py"
      ],
      "env": {}
    }
  }
}
```

**Windows:**
```json
{
  "mcpServers": {
    "connective-crm": {
      "command": "python",
      "args": [
        "C:\\Users\\YOUR_USERNAME\\connective-crm-knowledge\\mcp_server\\connective_crm_server.py"
      ],
      "env": {}
    }
  }
}
```

**Replace `YOUR_USERNAME`** with your actual username!

### Step 5: Test in Claude Code

Restart Claude Code, then ask:

```
"What's the selector for lender?"
"How many brokers are available?"
"Is 'Commonwealth Bank' a valid lender?"
"List all property types"
```

✅ **You're done!** MCP is now available in all your automation projects.

---

## 📊 Knowledge Base Contents

| Category | Count | Examples |
|----------|-------|----------|
| **Lenders** | 54 | Commonwealth Bank, Westpac, ANZ, NAB, Macquarie... |
| **Brokers/Agents** | 19 | Team members available in dropdown |
| **Property Types** | 63 | Residential, Commercial, Investment, Vacant Land... |
| **Liability Types** | 18 | Credit Card, Personal Loan, Mortgage, HECS... |
| **Transaction Types** | 6 | Purchase, Refinance, Equity Release... |
| **Total Elements** | 74 | All Connective CRM fields mapped |
| **Dropdown Options** | 286+ | Validated values for automation |

---

## 💡 How to Use

### Use Case 1: Quick Field Lookup

**In Claude Code:**
```
You: "What's the selector for property value?"
Claude: "#propertyValue (input type, number)"
```

### Use Case 2: Validate CSV Before Automation

**In Python:**
```python
from sdk import CRMReference

crm = CRMReference()

# Check if lender is valid
result = crm.validate_and_correct("lender", "CBA")
print(result)
# Output: {'valid': False, 'corrected': 'Commonwealth Bank', 'confidence': 95.2}
```

### Use Case 3: Get All Options for Dropdown

**In Claude Code:**
```
You: "List all lenders"
Claude: [Returns 54 lenders with exact names for automation]
```

### Use Case 4: Smart Matching (Abbreviations)

**In Python:**
```python
match = crm.fuzzy_match("lender", "Comm Bank")
print(match.matched_value)  # "Commonwealth Bank"
print(match.confidence)     # 88.5
```

---

## 🔄 Staying Updated

**When team updates the knowledge base:**

```bash
cd ~/connective-crm-knowledge
git pull origin main
```

**Restart Claude Code** to use the latest knowledge.

---

## 👥 Team Collaboration

### Report Issues
Found a missing field or outdated selector?
→ [Create an Issue](https://github.com/Larksa/connective-crm-knowledge/issues)

### Submit Updates
Have new field information?
→ [Submit a Pull Request](https://github.com/Larksa/connective-crm-knowledge/pulls)

### Share Tips
Automation tricks and patterns
→ [Discussions](https://github.com/Larksa/connective-crm-knowledge/discussions)

---

## 📚 Documentation

| Guide | Purpose |
|-------|---------|
| **TEAM_SETUP_GUIDE.md** | Detailed setup for Windows/Mac/Linux |
| **KNOWLEDGE_UPDATES.md** | How to update the knowledge base |
| **ONBOARDING_CHECKLIST.md** | New team member checklist |
| **MCP_TEMPLATE_GUIDE.md** | Create MCPs for other portals |
| **ARCHITECTURE_GUIDE.md** | How the system works |

---

## 🛠️ Troubleshooting

### "ModuleNotFoundError: No module named 'rapidfuzz'"
```bash
pip install -r requirements.txt
```

### "MCP not showing in Claude Code"
1. Check `.claude.json` has valid JSON syntax
2. Use **absolute path** to MCP server (not relative)
3. Restart Claude Code completely
4. Check Claude Code logs for errors

### "Wrong Python version"
```bash
python3 --version  # Should be 3.8+
python3 -m venv venv  # Use python3, not python
```

### Windows: "python not found"
Use `py` instead of `python3`:
```bash
py -m venv venv
venv\Scripts\activate
py -m pip install -r requirements.txt
```

**Still stuck?** See [TEAM_SETUP_GUIDE.md](TEAM_SETUP_GUIDE.md) or create an issue.

---

## 🔐 Security Note

**This repository contains:**
- ✅ Field selectors (e.g., `#lender`, `#propertyType`)
- ✅ Dropdown options (lender names, property types)
- ✅ Navigation workflows

**This repository does NOT contain:**
- ❌ Login credentials
- ❌ API keys
- ❌ Client data
- ❌ Actual automation scripts

Safe to share within your team!

---

## 🎓 For New Team Members

**Start here:**
1. Read this README
2. Follow Quick Setup (Steps 1-5)
3. Review [ONBOARDING_CHECKLIST.md](ONBOARDING_CHECKLIST.md)
4. Test with example queries
5. Ask questions in team chat or GitHub Discussions

**Time to setup:** ~10 minutes

---

## 📈 Project Stats

- **Total Code:** ~1,569 lines
- **Languages:** Python 100%
- **Dependencies:** 1 (rapidfuzz for fuzzy matching)
- **Tested on:** Python 3.8, 3.9, 3.10, 3.11
- **Platforms:** macOS, Linux, Windows

---

## 🤝 Contributing

### Adding New Fields

See [KNOWLEDGE_UPDATES.md](KNOWLEDGE_UPDATES.md) for detailed instructions.

**Quick version:**
1. Edit `knowledge/COMPLETE_CONNECTIVE_CRM_REFERENCE.md`
2. Test locally: `python -c "from sdk import CRMReference; crm = CRMReference(); print(crm.get_selector('new_field'))"`
3. Commit: `git commit -m "Add new field: [name]"`
4. Push: `git push`
5. Notify team to pull

---

## 📞 Support

- **Documentation:** See guides above
- **Issues:** [GitHub Issues](https://github.com/Larksa/connective-crm-knowledge/issues)
- **Team Chat:** Ask your team lead

---

## 📄 License

MIT License - Free to use for your mortgage broking automation.

---

## 🙏 Credits

**Developed for:** Mortgage broking teams automating Connective CRM
**Maintained by:** Team Larksa
**Version:** 1.0.0
**Last Updated:** 2025-10-06

---

**Questions?** Start with [TEAM_SETUP_GUIDE.md](TEAM_SETUP_GUIDE.md) or create an issue!
