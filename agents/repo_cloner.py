from crewai import Agent
import subprocess, os
from urllib.parse import urlparse, urlunparse

class RepoCloner(Agent):
    def __init__(self):
        super().__init__(
            role="Repository Cloner",
            goal="Clone a Bitbucket repository (public or private) to local storage for analysis.",
            backstory="You are an expert in fetching repositories from Git, handling authentication when needed.",
            tools=[],  # optional, add Git helper tools if needed
            verbose=True
        )

    def run(self, inputs):
        repo_url = inputs.get("repo_url")
        folder_name = inputs.get("folder_name")

        parsed = urlparse(repo_url)
        username_from_url = parsed.username

        # Remove username from URL
        netloc = parsed.hostname
        if parsed.port:
            netloc += f":{parsed.port}"
        repo_url_clean = urlunparse((parsed.scheme, netloc, parsed.path, "", "", ""))

        if not folder_name:
            folder_name = os.path.basename(repo_url_clean).replace(".git", "")

        # Try public clone first
        try:
            subprocess.run(["git", "clone", repo_url_clean, folder_name], check=True)
            return {"repo_path": os.path.abspath(folder_name)}
        except subprocess.CalledProcessError:
            username = inputs.get("username")
            token = inputs.get("token")
            if not username or not token:
                return {"error": "Private repo requires username + token."}

            auth_url = repo_url_clean.replace("https://", f"https://{username}:{token}@")
            subprocess.run(["git", "clone", auth_url, folder_name], check=True)
            return {"repo_path": os.path.abspath(folder_name)}
