# GitHub Setup Instructions

**How to push this repository to GitHub and share with your team**

---

## 🎯 Quick Overview

You have a fully prepared repository that's ready to push to GitHub. This guide will help you:
1. Create the repository on GitHub
2. Push your code
3. Share with team members

---

## 📋 Prerequisites

- ✅ Git repository initialized (already done!)
- ✅ Initial commit created (already done!)
- ✅ GitHub account: **Larksa** (andrew@suelarkey.com.au)
- ✅ GitHub CLI installed OR access to github.com

---

## 🚀 Method 1: Using GitHub CLI (Recommended)

### Step 1: Verify GitHub CLI Authentication

```bash
gh auth status
```

**Expected:** Shows you're logged in as Larksa

**If not logged in:**
```bash
gh auth login
# Follow prompts
# Choose: GitHub.com → HTTPS → Login with web browser
```

### Step 2: Create Repository and Push

```bash
# Navigate to your repo
cd ~/connective-intelligence/connective-crm-mcp-template

# Create GitHub repo and push (Public)
gh repo create Larksa/connective-crm-knowledge --public --source=. --remote=origin --push

# OR create as Private (if you prefer)
gh repo create Larksa/connective-crm-knowledge --private --source=. --remote=origin --push
```

**That's it!** ✅ Repository is now on GitHub

**View your repo:**
```bash
gh repo view --web
```

---

## 🌐 Method 2: Using GitHub Web Interface

### Step 1: Create Repository on GitHub

1. Go to https://github.com/new
2. Fill in:
   - **Owner:** Larksa
   - **Repository name:** `connective-crm-knowledge`
   - **Description:** `Connective CRM MCP Server - Field Knowledge Base for Automation`
   - **Visibility:**
     - ✅ Public (recommended - no sensitive data)
     - OR Private (if you prefer team-only access)
   - **Do NOT** initialize with README, .gitignore, or license (we already have these)
3. Click **Create repository**

### Step 2: Push Your Code

GitHub will show instructions. Use these commands:

```bash
# Navigate to your repo
cd ~/connective-intelligence/connective-crm-mcp-template

# Add GitHub remote
git remote add origin https://github.com/Larksa/connective-crm-knowledge.git

# Push code
git branch -M main
git push -u origin main
```

**Enter credentials when prompted**

✅ **Done!** Your code is now on GitHub

**View at:** https://github.com/Larksa/connective-crm-knowledge

---

## 👥 Sharing with Team Members

### Option A: Public Repository

**If you made it public:**

Share this with team:
```
Repository: https://github.com/Larksa/connective-crm-knowledge

To set up:
1. Clone: git clone https://github.com/Larksa/connective-crm-knowledge.git
2. Follow: README.md for setup instructions
```

No GitHub account needed for cloning!

---

### Option B: Private Repository

**If you made it private:**

1. **Invite team members:**
   ```bash
   # Using GitHub CLI
   gh repo edit --add-collaborator username1
   gh repo edit --add-collaborator username2

   # OR via web interface:
   # Go to: https://github.com/Larksa/connective-crm-knowledge/settings/access
   # Click "Add people"
   # Enter their GitHub usernames
   # Choose role: "Write" (for contributors) or "Read" (for users)
   ```

2. **Share with team:**
   ```
   Repository: https://github.com/Larksa/connective-crm-knowledge (private)

   You've been added as a collaborator!

   To set up:
   1. Accept invitation (check your email)
   2. Clone: git clone https://github.com/Larksa/connective-crm-knowledge.git
   3. Follow: README.md for setup
   ```

---

## 📧 Team Announcement Template

**Copy-paste this email/message to your team:**

---

### Subject: New Team Resource - Connective CRM Knowledge Base

Hi Team,

I've set up a shared knowledge base for Connective CRM automation! This will help us all:
- Look up field selectors instantly
- Validate data before automation
- Keep our knowledge synchronized
- Build automations faster

**What it is:**
An MCP server that gives Claude Code instant access to all Connective CRM field information (lenders, brokers, property types, selectors, etc.)

**How to get it:**

1. **Clone the repository:**
   ```bash
   cd ~
   git clone https://github.com/Larksa/connective-crm-knowledge.git
   ```

2. **Follow setup guide:**
   Open `README.md` and follow the 5-step Quick Setup

   OR use detailed guide: `TEAM_SETUP_GUIDE.md` (has Windows/Mac/Linux instructions)

3. **New team members:**
   Use `ONBOARDING_CHECKLIST.md` for step-by-step onboarding

**Time to setup:** ~10 minutes

**Questions?**
- Check the documentation in the repo
- Ask me
- Create a GitHub issue

**Updates:**
When fields change, I'll update the knowledge base. Just run:
```bash
cd ~/connective-crm-knowledge
git pull
```

Looking forward to seeing how this speeds up our automation work!

[Your name]

---

---

## 🔄 Updating the Repository (For You)

**When you make changes:**

```bash
cd ~/connective-intelligence/connective-crm-mcp-template

# Pull latest (if team members contributed)
git pull origin main

# Make your changes
# ... edit files ...

# Stage and commit
git add .
git commit -m "Add new lender: Example Bank"

# Push
git push origin main

# Notify team
# Send message: "Knowledge base updated! Run: git pull"
```

---

## 📊 Repository Settings (Optional)

### Enable GitHub Discussions

Perfect for team Q&A and sharing tips:

```bash
gh repo edit --enable-discussions
```

Or via web: Settings → Features → ✓ Discussions

### Add Description and Topics

```bash
gh repo edit --description "Connective CRM MCP Server - Field Knowledge Base for Automation" \
  --add-topic mortgage-broking \
  --add-topic automation \
  --add-topic mcp-server \
  --add-topic connective-crm
```

### Create Issue Templates

Helps team report missing fields or bugs:

1. Go to: Settings → Features → Set up templates
2. Add templates for:
   - "New Field Request"
   - "Selector Broken"
   - "Bug Report"

---

## ✅ Verification Checklist

After pushing, verify:

- [ ] Repository visible at: https://github.com/Larksa/connective-crm-knowledge
- [ ] README displays correctly
- [ ] All files present (check file count: 20 files)
- [ ] Can clone from different location:
  ```bash
  cd ~/Desktop
  git clone https://github.com/Larksa/connective-crm-knowledge.git test-clone
  cd test-clone
  ls  # Should see all files
  ```
- [ ] Team members can access (if private)

---

## 🚨 Troubleshooting

### "Permission denied (publickey)"

**Solution:** Use HTTPS instead of SSH:
```bash
git remote set-url origin https://github.com/Larksa/connective-crm-knowledge.git
git push
```

### "Repository already exists"

**Solution:**
1. Delete the repo on GitHub
2. OR use a different name:
   ```bash
   gh repo create Larksa/connective-crm-mcp --public --source=. --remote=origin --push
   ```

### "Authentication failed"

**Solution:**
```bash
# Re-authenticate GitHub CLI
gh auth login

# OR use Personal Access Token for HTTPS
# Generate at: https://github.com/settings/tokens
```

---

## 📞 Support

**GitHub CLI issues:**
- Docs: https://cli.github.com/manual/

**Git issues:**
- Check: `git status` and `git remote -v`

**Team access issues:**
- Verify invitations sent
- Check repository visibility settings

---

## 🎉 Success!

**When complete, your team will have:**

- ✅ Shared knowledge base on GitHub
- ✅ Version-controlled field information
- ✅ Easy updates via `git pull`
- ✅ Collaboration via issues and PRs
- ✅ Central resource for all Connective automations

**Your repository is ready to be a key team resource!** 🚀

---

**Next:** Share the repository link with your team and send them the onboarding email template above!
