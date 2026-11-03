import re


def folder_name(address: str) -> str:
    """Folder name for a property address: lowercase words joined by hyphens."""
    words = re.findall(r"[a-z0-9]+", address.lower())
    return "-".join(words)
