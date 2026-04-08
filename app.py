"""
Sample Python application for the CI/CD Security Pipeline to scan.
This file intentionally contains some security issues for demonstration.
"""

import sqlite3
import subprocess
import hashlib


def get_user(username):
    """Fetch user from database - vulnerable to SQL injection (demo)."""
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    # INSECURE: direct string formatting - flagged by Bandit
    query = "SELECT * FROM users WHERE username = '%s'" % username
    cursor.execute(query)
    return cursor.fetchone()


def hash_password(password):
    """Hash a password - using weak algorithm (demo)."""
    # INSECURE: MD5 is weak - flagged by Bandit
    return hashlib.md5(password.encode()).hexdigest()


def run_command(user_input):
    """Run a system command - vulnerable to injection (demo)."""
    # INSECURE: shell=True with user input - flagged by Bandit
    result = subprocess.run(user_input, shell=True, capture_output=True)
    return result.stdout


def secure_hash(password):
    """Correct way to hash passwords."""
    import hashlib
    salt = b"random_salt_here"
    return hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 100000)


if __name__ == "__main__":
    print("Security Pipeline Demo App")
    print("This app is intentionally vulnerable for scanning demonstration.")
