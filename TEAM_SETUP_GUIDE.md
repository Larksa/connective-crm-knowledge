# Team Setup Guide - Connective CRM Knowledge Base

**Detailed setup instructions for Windows, Mac, and Linux users**

---

## 📋 Prerequisites

Before starting, ensure you have:

- [ ] **GitHub account** (for cloning the repository)
- [ ] **Git installed** ([Download here](https://git-scm.com/downloads))
- [ ] **Python 3.8 or higher** ([Download here](https://www.python.org/downloads/))
- [ ] **Claude Code installed** ([Get it here](https://claude.com/code))
- [ ] **Terminal/Command Prompt access**

---

## 🖥️ Platform-Specific Setup

Choose your operating system:

- [Windows Setup](#windows-setup)
- [macOS Setup](#macos-setup)
- [Linux Setup](#linux-setup)

---

## 🪟 Windows Setup

### Step 1: Install Prerequisites

#### 1.1 Install Git
1. Download from https://git-scm.com/download/win
2. Run installer, use default settings
3. Open **Git Bash** (installed with Git)

#### 1.2 Install Python
1. Download from https://www.python.org/downloads/
2. **IMPORTANT:** Check "Add Python to PATH" during installation
3. Verify installation:
   ```bash
   py --version
   # Should show: Python 3.8.x or higher
   ```

### Step 2: Clone Repository

Open **Git Bash** (not Command Prompt):

```bash
cd ~
git clone https://github.com/Larksa/connective-crm-knowledge.git
cd connective-crm-knowledge
```

**Expected output:**
```
Cloning into 'connective-crm-knowledge'...
...
Resolving deltas: 100% (x/x), done.
```

### Step 3: Create Virtual Environment

```bash
# Create virtual environment
py -m venv venv

# Activate it
venv\Scripts\activate

# Your prompt should now show: (venv)
```

**Troubleshooting:** If activation fails with "cannot be loaded because running scripts is disabled":
```powershell
# Open PowerShell as Administrator, run:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Step 4: Install Dependencies

```bash
# Ensure venv is activated (you should see "(venv)" in prompt)
pip install -r requirements.txt
```

**Expected output:**
```
Collecting rapidfuzz>=3.5.0
Installing collected packages: rapidfuzz
Successfully installed rapidfuzz-3.x.x
```

### Step 5: Test MCP Server

```bash
python mcp_server/connective_crm_server.py
```

**Expected:** Server starts, shows initialization messages
**To stop:** Press `Ctrl+C`

### Step 6: Configure Claude Code

**Important:** The MCP server configuration goes in your **user-level** `.claude.json` file, NOT the project-level file.

1. Find your Windows username:
   ```bash
   echo %USERNAME%
   ```

2. Find your Python installation path:
   ```bash
   where python
   # Example output: C:\Python313\python.exe
   ```

3. Create or edit `C:\Users\YOUR_USERNAME\.claude.json` (user-level config):
   ```json
   {
     "mcpServers": {
       "connective-crm": {
         "command": "C:\\Python313\\python.exe",
         "args": [
           "C:\\Users\\YOUR_USERNAME\\Documents\\connective-crm-knowledge\\mcp_server\\connective_crm_server.py"
         ],
         "env": {}
       }
     }
   }
   ```

4. **Replace:**
   - `YOUR_USERNAME` with the output from step 1
   - `C:\\Python313\\python.exe` with your Python path from step 2

5. Save file and **restart Claude Code**

### Step 7: Test in Claude Code

Open your automation project in Claude Code and ask:
```
"What's the selector for lender?"
```

**Expected:** Response with `#lender` and details

✅ **Setup complete!**

---

## 🍎 macOS Setup

### Step 1: Install Prerequisites

#### 1.1 Install Homebrew (if not installed)
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

#### 1.2 Install Git (usually pre-installed)
```bash
git --version
# If not installed:
brew install git
```

#### 1.3 Install Python
```bash
# Check if Python 3.8+ is installed
python3 --version

# If needed, install via Homebrew:
brew install python@3.11
```

### Step 2: Clone Repository

```bash
cd ~
git clone https://github.com/Larksa/connective-crm-knowledge.git
cd connective-crm-knowledge
```

### Step 3: Create Virtual Environment

```bash
# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate

# Your prompt should now show: (venv)
```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Test MCP Server

```bash
python mcp_server/connective_crm_server.py
```

**Expected:** Server starts without errors
**To stop:** Press `Ctrl+C`

### Step 6: Configure Claude Code

**Important:** The MCP server configuration goes in your **user-level** `~/.claude.json` file, NOT the project-level file.

1. Find your macOS username:
   ```bash
   whoami
   ```

2. Create or edit `~/.claude.json` (user-level config):
   ```json
   {
     "mcpServers": {
       "connective-crm": {
         "command": "python3",
         "args": [
           "/Users/YOUR_USERNAME/connective-crm-knowledge/mcp_server/connective_crm_server.py"
         ],
         "env": {}
       }
     }
   }
   ```

3. **Replace `YOUR_USERNAME`** with the output from step 1

4. Save and **restart Claude Code**

### Step 7: Test in Claude Code

Ask: `"What's the selector for lender?"`

✅ **Setup complete!**

---

## 🐧 Linux Setup

### Step 1: Install Prerequisites

#### Ubuntu/Debian:
```bash
sudo apt update
sudo apt install git python3 python3-venv python3-pip
```

#### Fedora/RHEL:
```bash
sudo dnf install git python3 python3-pip
```

#### Arch:
```bash
sudo pacman -S git python python-pip
```

### Step 2: Clone Repository

```bash
cd ~
git clone https://github.com/Larksa/connective-crm-knowledge.git
cd connective-crm-knowledge
```

### Step 3: Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Test MCP Server

```bash
python mcp_server/connective_crm_server.py
```

### Step 6: Configure Claude Code

**Important:** The MCP server configuration goes in your **user-level** `~/.claude.json` file, NOT the project-level file.

1. Get username:
   ```bash
   whoami
   ```

2. Create or edit `~/.claude.json` (user-level config):
   ```json
   {
     "mcpServers": {
       "connective-crm": {
         "command": "python3",
         "args": [
           "/home/YOUR_USERNAME/connective-crm-knowledge/mcp_server/connective_crm_server.py"
         ],
         "env": {}
       }
     }
   }
   ```

3. **Replace `YOUR_USERNAME`** with the output from step 1

4. Save and **restart Claude Code**

### Step 7: Test in Claude Code

Ask: `"How many brokers are available?"`

✅ **Setup complete!**

---

## 🔄 Daily Usage

### Activating Virtual Environment

**Every time** you work with the MCP (for testing/updates):

**Windows:**
```bash
cd ~/connective-crm-knowledge
venv\Scripts\activate
```

**Mac/Linux:**
```bash
cd ~/connective-crm-knowledge
source venv/bin/activate
```

### Using in Claude Code

No activation needed! Claude Code handles this automatically when you query.

---

## 📥 Getting Updates

When the team updates the knowledge base:

```bash
cd ~/connective-crm-knowledge
git pull origin main
```

**Restart Claude Code** to use updated knowledge.

---

## 🧪 Verification Tests

### Test 1: Python Installation
```bash
python3 --version  # Mac/Linux
py --version       # Windows
# Should show: Python 3.8.x or higher
```

### Test 2: Git Installation
```bash
git --version
# Should show: git version 2.x.x
```

### Test 3: Repository Cloned
```bash
ls ~/connective-crm-knowledge
# Should show: mcp_server/ sdk/ knowledge/ requirements.txt README.md
```

### Test 4: Dependencies Installed
```bash
cd ~/connective-crm-knowledge
source venv/bin/activate  # Mac/Linux
# OR
venv\Scripts\activate     # Windows

python -c "import rapidfuzz; print('✅ Dependencies OK')"
# Should print: ✅ Dependencies OK
```

### Test 5: MCP Server Starts
```bash
python mcp_server/connective_crm_server.py
# Should start without errors (Ctrl+C to stop)
```

### Test 6: Claude Code Integration
In Claude Code (in your automation project):
```
"What's the selector for lender?"
# Should return: #lender with details
```

---

## 🚨 Common Issues & Solutions

### Issue: "git: command not found"

**Solution:**
- **Windows:** Install Git from https://git-scm.com/download/win
- **Mac:** Run `xcode-select --install` or install via Homebrew
- **Linux:** `sudo apt install git` (Ubuntu) or equivalent

---

### Issue: "python: command not found"

**Solution:**
- Try `python3` instead of `python` (Mac/Linux)
- Try `py` instead of `python` (Windows)
- Install Python from https://www.python.org/downloads/

---

### Issue: "Permission denied" when activating venv (Windows)

**Solution:**
Open PowerShell as Administrator:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

### Issue: "ModuleNotFoundError: No module named 'rapidfuzz'"

**Solution:**
```bash
# Make sure venv is activated
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

# Reinstall dependencies
pip install -r requirements.txt
```

---

### Issue: "MCP not showing in Claude Code"

**Checklist:**
1. ✅ Configuration is in **user-level** `~/.claude.json` (NOT project-level `.claude.json`)
2. ✅ `.claude.json` has valid JSON (no trailing commas, correct brackets)
3. ✅ Used **absolute path** to MCP server (not relative `./` path)
4. ✅ Replaced `YOUR_USERNAME` with actual username
5. ✅ Windows: Used full Python path like `C:\\Python313\\python.exe`
6. ✅ Restarted Claude Code **completely** (quit and reopen)
7. ✅ MCP server starts without errors when run manually

**Common mistake:** If your user-level `~/.claude.json` has a project entry with empty `"mcpServers": {}`, it will override the project-level config. Solution: Add the MCP config to the user-level file instead.

**Debug:**
```bash
# Test MCP manually
cd ~/connective-crm-knowledge
source venv/bin/activate
python mcp_server/connective_crm_server.py
# If this fails, fix errors first

# Verify configuration location (should be in user-level file)
# Windows: C:\Users\YOUR_USERNAME\.claude.json
# Mac/Linux: ~/.claude.json
```

---

### Issue: Wrong Python Version

**Check version:**
```bash
python3 --version  # Should be 3.8 or higher
```

**If too old:**
- **Windows:** Download latest from python.org
- **Mac:** `brew install python@3.11`
- **Linux:** `sudo apt install python3.11` or use pyenv

---

### Issue: "fatal: could not create work tree dir"

**Solution:**
Permission issue. Try:
```bash
# Clone to different location
cd ~/Desktop
git clone https://github.com/Larksa/connective-crm-knowledge.git
```

Then update path in `.claude.json` accordingly.

---

## 💡 Pro Tips

### Tip 1: Use Absolute Paths
Always use full path in `.claude.json`:
```json
// ✅ Good:
"/Users/andrew/connective-crm-knowledge/mcp_server/connective_crm_server.py"

// ❌ Bad:
"./mcp_server/connective_crm_server.py"  // Breaks when Claude Code switches dirs
```

### Tip 2: Keep Venv Out of Git
The `venv/` folder is auto-ignored. Never commit it!

### Tip 3: Pull Updates Weekly
```bash
cd ~/connective-crm-knowledge
git pull
# Restart Claude Code
```

### Tip 4: Test After Each Step
Don't skip the test steps! Catch issues early.

### Tip 5: Use Git Bash on Windows
Git Bash is more reliable than Command Prompt for these commands.

---

## 📞 Getting Help

**Still stuck?**

1. Check this guide again (most issues covered above)
2. Ask team lead or colleague who has it working
3. Create issue: https://github.com/Larksa/connective-crm-knowledge/issues
4. Include:
   - Your OS (Windows/Mac/Linux)
   - Python version (`python3 --version`)
   - Error message (copy-paste full output)
   - What step failed

---

## ✅ Setup Checklist

Print this out and check off as you go:

- [ ] Git installed and working
- [ ] Python 3.8+ installed
- [ ] Claude Code installed
- [ ] Repository cloned to `~/connective-crm-knowledge`
- [ ] Virtual environment created
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] MCP server starts successfully
- [ ] `.claude.json` configured in automation project
- [ ] Claude Code restarted
- [ ] Test query works: "What's the selector for lender?"
- [ ] Can pull updates: `git pull`

**All checked?** ✅ You're ready to use the MCP!

---

## 🎓 Next Steps

1. Review [ONBOARDING_CHECKLIST.md](ONBOARDING_CHECKLIST.md)
2. Try example queries (see README.md)
3. Review [KNOWLEDGE_UPDATES.md](KNOWLEDGE_UPDATES.md) if you'll be updating fields
4. Join team discussions on GitHub

**Time to proficiency:** 1-2 days of usage

---

**Questions?** Create an issue or ask your team lead!
