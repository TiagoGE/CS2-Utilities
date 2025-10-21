import re

def get_latest_version_info(changelog_path="CHANGELOG.md"):
    """
    Reads CHANGELOG.md and returns the latest version and date.
    Returns a tuple: (version, date)
    """
    try:
        with open(changelog_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Regex to match the first version line: ## [0.2.1] - 2025-10-19
        match = re.search(r"\[\d+\.\d+\.\d+\]\s*-\s*(\d{4}-\d{2}-\d{2})", content)
        version_match = re.search(r"\[(\d+\.\d+\.\d+)\]", content)

        if match and version_match:
            version = version_match.group(1)
            date = match.group(1)
            return version, date
        else:
            return "0.0.0", "2003-01-06"
    except FileNotFoundError:
        return "0.0.0", "2003-01-06"
