def clean_repo_url(repo_url: str) -> str:
    """Remove 'git clone' prefix and normalize repo URL."""
    if repo_url.startswith("git clone "):
        repo_url = repo_url[len("git clone "):].strip()
    return repo_url
