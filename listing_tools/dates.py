from datetime import date


def shoot_label(day: date) -> str:
    """Label for a shoot date, e.g. "Tue, Nov 4, 2026"."""
    return day.strftime("%a, %b %m, %Y")
