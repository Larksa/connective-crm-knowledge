# Team Member Onboarding Checklist

**Welcome to the Connective CRM Automation Team!**

This checklist will get you up and running with our shared knowledge base.

---

## 📋 Prerequisites (Before Starting)

- [ ] **GitHub account created**
  - If not: https://github.com/signup
  - Username: _________________
  - Email: _________________

- [ ] **Access to team GitHub repository**
  - Repository: `Larksa/connective-crm-knowledge`
  - Ask team lead to add you (if private)

- [ ] **Computer meets requirements**
  - [ ] Operating System: Windows 10+ / macOS 10.15+ / Linux
  - [ ] Git installed (test: `git --version`)
  - [ ] Python 3.8+ installed (test: `python3 --version`)
  - [ ] 500MB free disk space
  - [ ] Internet connection

- [ ] **Tools installed**
  - [ ] Claude Code (https://claude.com/code)
  - [ ] Text editor (VS Code, Sublime, Notepad++, or any)
  - [ ] Terminal/Command Prompt access

**All checked above?** ✅ Proceed to setup!

---

## 🚀 Setup (Day 1 - Allow 30 minutes)

### Part 1: Clone Repository (5 minutes)

- [ ] Open Terminal/Git Bash/Command Prompt
- [ ] Navigate to home directory
  ```bash
  cd ~
  ```

- [ ] Clone the repository
  ```bash
  git clone https://github.com/Larksa/connective-crm-knowledge.git
  ```

- [ ] Verify files downloaded
  ```bash
  cd connective-crm-knowledge
  ls
  ```
  **Expected:** Should see `mcp_server/`, `sdk/`, `knowledge/`, `README.md`

**Checkpoint:** ✅ Repository cloned successfully

---

### Part 2: Install Dependencies (10 minutes)

- [ ] Create virtual environment
  **Windows:**
  ```bash
  py -m venv venv
  ```
  **Mac/Linux:**
  ```bash
  python3 -m venv venv
  ```

- [ ] Activate virtual environment
  **Windows:**
  ```bash
  venv\Scripts\activate
  ```
  **Mac/Linux:**
  ```bash
  source venv/bin/activate
  ```
  **Expected:** Prompt shows `(venv)`

- [ ] Install dependencies
  ```bash
  pip install -r requirements.txt
  ```
  **Expected:** `Successfully installed rapidfuzz-3.x.x`

**Checkpoint:** ✅ Dependencies installed

---

### Part 3: Test MCP Server (3 minutes)

- [ ] Test MCP server starts
  ```bash
  python mcp_server/connective_crm_server.py
  ```
  **Expected:** Server starts without errors

- [ ] Stop server (Press `Ctrl+C`)

- [ ] Test SDK works
  ```bash
  python -c "from sdk import CRMReference; crm = CRMReference(); print(f'✅ {len(crm.elements)} elements loaded')"
  ```
  **Expected:** `✅ 74 elements loaded` (or similar)

**Checkpoint:** ✅ MCP server working

---

### Part 4: Configure Claude Code (10 minutes)

- [ ] Find your username
  **Windows:**
  ```bash
  echo %USERNAME%
  ```
  **Mac/Linux:**
  ```bash
  whoami
  ```
  **My username:** _________________

- [ ] Navigate to your automation project
  ```bash
  cd ~/your-automation-project
  ```

- [ ] Create or edit `.claude.json` in project root

- [ ] Add MCP configuration (choose your OS):

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

  **Mac:**
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

  **Linux:**
  ```json
  {
    "mcpServers": {
      "connective-crm": {
        "command": "python",
        "args": [
          "/home/YOUR_USERNAME/connective-crm-knowledge/mcp_server/connective_crm_server.py"
        ],
        "env": {}
      }
    }
  }
  ```

- [ ] **Replace `YOUR_USERNAME`** with actual username from above

- [ ] Save `.claude.json` file

- [ ] Restart Claude Code **completely** (Quit and reopen)

**Checkpoint:** ✅ Claude Code configured

---

### Part 5: Verify Everything Works (5 minutes)

- [ ] Open automation project in Claude Code

- [ ] Test query #1:
  ```
  Ask: "What's the selector for lender?"
  Expected: "#lender" with details
  ```
  **Result:** ☐ Works ☐ Doesn't work

- [ ] Test query #2:
  ```
  Ask: "How many brokers are available?"
  Expected: "19 brokers" (or current count)
  ```
  **Result:** ☐ Works ☐ Doesn't work

- [ ] Test query #3:
  ```
  Ask: "Is 'Commonwealth Bank' a valid lender?"
  Expected: "Yes" or "true"
  ```
  **Result:** ☐ Works ☐ Doesn't work

**All 3 working?** ✅ Setup complete!

**Not working?** → See [Troubleshooting](#-troubleshooting) below

---

## 📚 Learning Phase (Days 2-3)

### Familiarize Yourself (30 minutes)

- [ ] Read `README.md` fully
- [ ] Review `TEAM_SETUP_GUIDE.md` for your OS
- [ ] Skim `KNOWLEDGE_UPDATES.md` (you'll need this later)
- [ ] Browse `knowledge/COMPLETE_CONNECTIVE_CRM_REFERENCE.md`

### Try Example Queries (15 minutes)

Test each type of query in Claude Code:

- [ ] **Field lookup:**
  "What's the selector for property value?"

- [ ] **List options:**
  "List all lenders"

- [ ] **Validation:**
  "Is 'CBA' a valid lender?"

- [ ] **Search:**
  "Search for fields related to property"

- [ ] **Fuzzy matching:**
  "Match 'Comm Bank' to lender field"

**Checkpoint:** ✅ Understand how to use MCP queries

---

### Practice With Real Data (20 minutes)

- [ ] Open a CSV/Excel file with client data

- [ ] Use MCP to validate data before automation:
  ```
  Ask: "Is '[Lender Name from CSV]' a valid lender?"
  Ask: "Is '[Broker Name from CSV]' a valid broker?"
  ```

- [ ] Fix any mismatches found

**Checkpoint:** ✅ Can validate data using MCP

---

## 🔄 Daily Workflow (Ongoing)

### Morning Routine (2 minutes)

- [ ] Check team chat for knowledge base updates
- [ ] Pull latest changes if updated:
  ```bash
  cd ~/connective-crm-knowledge
  git pull origin main
  # Restart Claude Code if updates pulled
  ```

### During Automation Work (As needed)

- [ ] Use MCP queries to look up field info
- [ ] Validate CSV data before running automation
- [ ] Check dropdown options are current

### Weekly (5 minutes)

- [ ] Pull latest updates (even if no notification):
  ```bash
  cd ~/connective-crm-knowledge
  git pull
  ```

**Checkpoint:** ✅ Integrated into daily workflow

---

## 🔍 Contributing (When Ready)

### When You Find New Information (15 minutes)

- [ ] Read `KNOWLEDGE_UPDATES.md` first
- [ ] Document the change (screenshot, field name, selector)
- [ ] Update knowledge file or notify team lead
- [ ] Test your changes
- [ ] Commit and push (or create issue)

**Checkpoint:** ✅ Contributing to knowledge base

---

## 🚨 Troubleshooting

### Setup Issues

**Issue:** Git clone fails
- [ ] Check GitHub access (private repo requires invite)
- [ ] Try HTTPS instead of SSH: `git clone https://github.com/Larksa/connective-crm-knowledge.git`

**Issue:** Python version too old
- [ ] Check: `python3 --version` (need 3.8+)
- [ ] Install latest from https://python.org

**Issue:** MCP not showing in Claude Code
- [ ] Check `.claude.json` syntax (valid JSON)
- [ ] Use absolute path (not relative `./`)
- [ ] Restart Claude Code completely
- [ ] Test MCP starts manually first

**Issue:** "ModuleNotFoundError"
- [ ] Activate venv first
- [ ] Run: `pip install -r requirements.txt`

**Still stuck?**
- [ ] Check `TEAM_SETUP_GUIDE.md` for detailed troubleshooting
- [ ] Ask team lead or colleague
- [ ] Create GitHub issue with error details

---

## ✅ Onboarding Complete!

**When you can do all of these:**

- ✅ Clone and update the repository
- ✅ Query MCP from Claude Code
- ✅ Validate data using MCP
- ✅ Pull updates from team
- ✅ Understand when/how to update knowledge

**You're fully onboarded!** 🎉

**Time to proficiency:** 1-2 weeks of daily use

---

## 📞 Who to Ask

**Technical setup issues:**
- Team lead: _________________
- Technical contact: _________________

**Knowledge base questions:**
- Documentation: See guides in repo
- GitHub Issues: https://github.com/Larksa/connective-crm-knowledge/issues

**Automation questions:**
- Team lead or senior automation team member

---

## 🎓 Next Steps After Onboarding

1. **Week 1:** Use MCP for all field lookups
2. **Week 2:** Start contributing field updates
3. **Week 3:** Help onboard next team member
4. **Month 2:** Become MCP expert on the team

---

## 📝 Onboarding Feedback

**After completing setup, please provide feedback:**

- **Setup time:** ________ minutes (vs estimated 30 min)
- **Issues encountered:** _________________
- **Suggestions for improvement:** _________________
- **Documentation clarity (1-10):** _____
- **Ready to use independently:** ☐ Yes ☐ Need more help

**Share with team lead to improve onboarding!**

---

**Welcome to the team! You're now equipped with our core automation resource.** 🚀
