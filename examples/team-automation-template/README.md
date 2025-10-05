# Team Automation Template

**Quick-start template for Connective CRM automation projects**

This template is pre-configured to use the shared Connective CRM knowledge base.

---

## 🚀 Quick Start

### 1. Copy This Template

```bash
# Copy to new project location
cp -r ~/connective-crm-knowledge/examples/team-automation-template ~/my-new-automation

cd ~/my-new-automation
```

### 2. Configure MCP Path

Edit `.claude.json` and replace `YOUR_USERNAME`:

**Mac/Linux:**
```json
{
  "mcpServers": {
    "connective-crm": {
      "command": "python",
      "args": [
        "/Users/YOUR_ACTUAL_USERNAME/connective-crm-knowledge/mcp_server/connective_crm_server.py"
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
        "C:\\Users\\YOUR_ACTUAL_USERNAME\\connective-crm-knowledge\\mcp_server\\connective_crm_server.py"
      ],
      "env": {}
    }
  }
}
```

### 3. Install Dependencies

```bash
python3 -m venv venv
source venv/bin/activate  # Mac/Linux
# venv\Scripts\activate   # Windows

pip install -r requirements.txt
```

### 4. Test MCP Access

Open in Claude Code and ask:
```
"What's the selector for lender?"
```

**Expected:** Returns `#lender` with details

✅ **Template ready!** Start building your automation.

---

## 📁 Project Structure

```
my-new-automation/
├── .claude.json          ← MCP configuration (edit YOUR_USERNAME)
├── scripts/              ← Your automation scripts
│   └── validate_csv.py   ← Example: CSV validation
├── data/                 ← Input data (CSV/Excel)
│   └── sample_data.csv   ← Example data
├── requirements.txt      ← Python dependencies
├── venv/                 ← Virtual environment (git-ignored)
└── README.md            ← This file
```

---

## 💡 Example Scripts

### Example 1: Validate CSV Data

See `scripts/validate_csv.py` for a complete example of:
- Loading CSV data
- Using MCP to validate lender/broker names
- Fuzzy matching for abbreviations
- Generating validation report

**Run it:**
```bash
python scripts/validate_csv.py data/sample_data.csv
```

---

## 🎯 Common Use Cases

### Use Case 1: Field Lookup

**In Claude Code:**
```
"What's the selector for property value?"
"List all property types"
```

### Use Case 2: Data Validation

**In Python:**
```python
from sdk import CRMReference

crm = CRMReference()

# Validate lender
result = crm.validate_and_correct("lender", "CBA")
if not result['valid']:
    print(f"Corrected: {result['corrected']}")
```

### Use Case 3: Get Dropdown Options

**In Python:**
```python
lenders = crm.get_all_options("lender")
print(f"Available lenders: {', '.join(lenders[:5])}...")
```

---

## 📚 Documentation

**Connective CRM Knowledge Base:**
- Main repo: `~/connective-crm-knowledge/`
- README: How to use MCP
- TEAM_SETUP_GUIDE: Detailed setup instructions
- KNOWLEDGE_UPDATES: How to update fields

**This Project:**
- Customize as needed for your automation
- Add your scripts to `scripts/`
- Add your data to `data/`

---

## 🔄 Updating Knowledge Base

**When Connective fields change:**

```bash
cd ~/connective-crm-knowledge
git pull origin main
# Restart Claude Code
```

Your automation automatically uses updated knowledge!

---

## 🛠️ Dependencies

Included in `requirements.txt`:
- `pandas` - CSV/Excel processing
- `playwright` - Browser automation (optional)
- No need to install `rapidfuzz` - already in knowledge base venv

---

## 🎓 Next Steps

1. **Customize this README** for your specific automation
2. **Add your scripts** to `scripts/` folder
3. **Add test data** to `data/` folder
4. **Build your automation** using MCP for field lookups
5. **Share with team** - they can copy this template too!

---

**Questions?** Check `~/connective-crm-knowledge/README.md` or ask team lead.
