CI/CD Security Pipeline (DevSecOps)

⚠️ Scanning Scope

This project scans the entire Git commit history, not just the latest code.

👉 This is achieved using:

fetch-depth: 0 in GitHub Actions

This ensures that even deleted or exposed secrets in past commits are detected.


🚀 What This Project Is

A fully automated CI/CD Security Pipeline that runs on every code commit using GitHub Actions.

Every time code is pushed:

Security tools automatically scan the project
Vulnerabilities are detected before merge

👉 This follows the DevSecOps approach — integrating security into development.

⚙️ How It Works — Full Flow

🧪 Job 1: Bandit (SAST)
Scans Python code line-by-line
Detects:
SQL Injection
Weak Cryptography
Shell Injection
Hardcoded Passwords
Covers 30+ vulnerability types

📦 Job 2: Safety
Scans requirements.txt
Matches dependencies with CVE database
Outputs:
CVE ID
Severity
Fixed version

🔑 Job 3: TruffleHog
Scans entire Git history
Detects:
API Keys
AWS Credentials
Tokens
Private Keys
Config:
fetch-depth: 0 → full history scan
--only-verified → reduces false positives
📊 Job 4: Summary
Runs after all jobs
Generates pass/fail result
Saves reports as artifacts
🧩 Component Breakdown
⚡ GitHub Actions Workflow

📁 .github/workflows/security-pipeline.yml

on: push / pull_request → auto trigger
runs-on: ubuntu-latest → fresh Linux environment
actions/checkout@v3 → clone repo
actions/upload-artifact@v3 → save reports
needs: → job dependency control
🛡️ Tools Used
🔍 Bandit — SAST
AST-based security scanning
Command:
bandit -r . -ll -f json

Common issues:

B201 → Flask debug mode
B303 → MD5 weak hash
B608 → SQL Injection
B602 → subprocess shell=True


📦 Safety — Dependency Scanner
Command:
safety check -r requirements.txt

💡 Example: Log4Shell vulnerability


🔑 TruffleHog — Secret Scanner
Scans full Git history
Detects 700+ credential types


📁 Project Structure
.
├── .github/workflows/security-pipeline.yml   # CI/CD pipeline configuration
├── app.py                                   # Main sample vulnerable application
├── app1.py                                  # Safe Python app (test case 1)
├── app2.py                                  # Safe Python app (test case 2)
├── requirements.txt                         # Dependencies for Safety scanning


▶️ How to Set Up & Run
Create a new GitHub repository
Push all project files
Go to the Actions tab
Make a change in app.py
Push code → pipeline runs automatically
Download reports from Artifacts

⚠️ Note on Test Results

The “Safe Python App” test case may still show a failure.

This happens because:

The pipeline scans the entire Git commit history
The main sample file (app.py) contains intentionally vulnerable code
Even if app1.py or app2.py are safe, vulnerabilities from other files or past commits are still detected

👉 As a result, the pipeline correctly reports a failure.
