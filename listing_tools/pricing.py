PACKAGES = {"photos": 175, "photos+drone": 275, "photos+video": 425}
TWILIGHT_ADD_ON = 95


def package_price(package: str, twilight: bool = False) -> int:
    """Price in dollars for a package, plus the twilight add-on if requested."""
    if package not in PACKAGES:
        raise ValueError(f"Unknown package: {package}")
    return PACKAGES[package] + (TWILIGHT_ADD_ON if twilight else 0)
