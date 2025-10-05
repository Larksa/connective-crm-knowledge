# Quick Reference Card

**Essential commands for maintaining connective-crm-knowledge**

---

## 🚀 Deploy to GitHub (First Time)

```bash
cd ~/connective-intelligence/connective-crm-mcp-template
gh repo create Larksa/connective-crm-knowledge --public --source=. --remote=origin --push
```

**Verify:** https://github.com/Larksa/connective-crm-knowledge

---

## 👥 Team Member Setup

**Send them:**
```bash
cd ~
git clone https://github.com/Larksa/connective-crm-knowledge.git
cd connective-crm-knowledge
python3 -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

**Add to their `.claude.json`:**
```json
{
  "mcpServers": {
    "connective-crm": {
      "command": "python",
      "args": ["/Users/USERNAME/connective-crm-knowledge/mcp_server/connective_crm_server.py"],
      "env": {}
    }
  }
}
```

---

## 📝 Update Knowledge Base

```bash
cd ~/connective-crm-knowledge
git pull  # Get latest first
nano knowledge/COMPLETE_CONNECTIVE_CRM_REFERENCE.md
# Make changes
python -c "from sdk import CRMReference; CRMReference()"  # Test
git add knowledge/COMPLETE_CONNECTIVE_CRM_REFERENCE.md
git commit -m "Add new lender: [Name]"
git push
# Notify team to pull
```

---

## 🔄 Team Gets Updates

```bash
cd ~/connective-crm-knowledge
git pull
# Restart Claude Code
```

---

## 🧪 Test MCP

```bash
cd ~/connective-crm-knowledge
source venv/bin/activate
python mcp_server/connective_crm_server.py  # Should start without errors
```

**In Claude Code:**
```
"What's the selector for lender?"
"How many brokers?"
"List all lenders"
```

---

## 📊 Check Status

```bash
# See what's changed
git status

# See recent changes
git log --oneline -5

# Check if team pushed updates
git fetch
git status

# See who's using the repo
gh repo view --web
```

---

## 🐛 Troubleshooting

**MCP not working:**
```bash
# Test SDK
python -c "from sdk import CRMReference; print(CRMReference())"

# Check path in .claude.json
# Restart Claude Code completely
```

**Git issues:**
```bash
# Pull latest
git pull origin main

# Check remote
git remote -v

# Fix conflicts
git status  # shows conflicts
# Edit files, then:
git add .
git commit -m "Merge updates"
```

---

## 📁 File Locations

- **Repo:** `~/connective-crm-knowledge/`
- **Knowledge:** `knowledge/COMPLETE_CONNECTIVE_CRM_REFERENCE.md`
- **MCP Server:** `mcp_server/connective_crm_server.py`
- **SDK:** `sdk/`
- **Template:** `examples/team-automation-template/`

---

## 🎯 Common Tasks

### Add New Lender
1. Edit `knowledge/COMPLETE_CONNECTIVE_CRM_REFERENCE.md`
2. Find `#### Element: Lender` section
3. Add to Options list (alphabetically)
4. Test, commit, push

### Fix Broken Selector
1. Inspect element in Connective (right-click → Inspect)
2. Update selector in knowledge file
3. Add old selector as fallback
4. Test, commit, push

### Add New Broker
1. Edit broker section in knowledge file
2. Add to Options list
3. Test, commit, push

### Add Completely New Field
1. Inspect field in Connective
2. Add new Element section to knowledge file
3. Include: name, selector, type, options (if dropdown)
4. Test, commit, push

---

## 📞 Quick Help

**Documentation:**
- Team setup: `TEAM_SETUP_GUIDE.md`
- Updating: `KNOWLEDGE_UPDATES.md`
- Onboarding: `ONBOARDING_CHECKLIST.md`
- GitHub: `GITHUB_SETUP.md`

**Support:**
- GitHub Issues: https://github.com/Larksa/connective-crm-knowledge/issues
- Discussions: https://github.com/Larksa/connective-crm-knowledge/discussions

---

## 📧 Team Notification Template

**When you update:**
```
📢 Knowledge base updated!

Changes:
- [Describe changes]

To get updates:
cd ~/connective-crm-knowledge && git pull

Then restart Claude Code.
```

---

**Print this card for quick reference!**
