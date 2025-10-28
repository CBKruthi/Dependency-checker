import os
import subprocess
from urllib.parse import urlparse, urlunparse
import getpass

def clone_bitbucket_repo():
    print("=== Bitbucket Repo Cloner ===")

    # Get repo URL (user may paste with or without username)
    repo_url = input("Enter the HTTPS URL of the Bitbucket repository: ").strip()

    # If user pasted with "git clone ..." at start, clean it
    if repo_url.startswith("git clone "):
        repo_url = repo_url[len("git clone "):].strip()

    # Parse URL
    parsed = urlparse(repo_url)
    username_from_url = parsed.username  # extract username if present

    # Remove username from netloc
    netloc = parsed.hostname
    if parsed.port:
        netloc += f":{parsed.port}"
    repo_url = urlunparse((parsed.scheme, netloc, parsed.path, "", "", ""))

    # Ask for folder name (default = repo name)
    folder_name = input("Enter the folder name to clone into (leave blank to use repo name): ").strip()
    if not folder_name:
        folder_name = os.path.basename(repo_url).replace(".git", "")

    folder_name = os.path.normpath(folder_name).replace("\\", "/")

    # Try cloning without authentication first (works for public repos)
    try:
        print(f"\nCloning repository into '{folder_name}'...")
        subprocess.run(
            ["git", "clone", repo_url, folder_name],
            check=True,
            capture_output=True,
            text=True
        )
        abs_path = os.path.abspath(folder_name)
        print(f"✅ Repository cloned successfully at: {abs_path}")
        return
    except subprocess.CalledProcessError as e:
        print(⚠️ Public clone failed. Git says:\n", e.stderr)

    # If that fails, ask for username + token
    print("\n🔒 This repo may be private. Let's use authentication.")
    username = username_from_url if username_from_url else input("Enter your Bitbucket username: ").strip()
    token = getpass.getpass("Enter your Bitbucket app password (token): ").strip()

    # Insert auth into URL
    auth_url = repo_url.replace("https://", f"https://{username}:{token}@")

    try:
        print(f"\nRetrying with authentication...")
        subprocess.run(
            ["git", "clone", auth_url, folder_name],
            check=True
        )
        abs_path = os.path.abspath(folder_name)
        print(f"✅ Repository cloned successfully at: {abs_path}")
    except subprocess.CalledProcessError as e2:
        print("❌ Clone failed even with authentication.")
        print("🔍 Git says:\n", e2.stderr)

if __name__ == "__main__":
    clone_bitbucket_repo()
