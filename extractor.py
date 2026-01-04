import re

def _safe_search(patterns, text, cast=None):
    """
    Try multiple regex patterns safely.
    """
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            value = match.group(1).strip()
            return cast(value) if cast else value
    return None


def extract_fields(email_text: str) -> dict:
    product = _safe_search(
        patterns=[
            r"model\s+([A-Z0-9\-]+)",
            r"product\s+([A-Z0-9\-]+)",
            r"item\s+([A-Z0-9\-]+)"
        ],
        text=email_text
    )

    quantity = _safe_search(
        patterns=[
            r"(\d+)\s*pcs",
            r"quantity\s*[:\-]?\s*(\d+)",
            r"(\d+)\s*units?"
        ],
        text=email_text,
        cast=int
    )

    city = _safe_search(
        patterns=[
            r"in\s+([A-Za-z]+)",
            r"delivery\s+to\s+([A-Za-z]+)"
        ],
        text=email_text
    )

    timeline = _safe_search(
        patterns=[
            r"within\s+([^\n\.]+)",
            r"delivery\s+in\s+([^\n\.]+)",
            r"lead\s*time\s*[:\-]?\s*([^\n\.]+)"
        ],
        text=email_text
    )

    email = _safe_search(
        patterns=[
            r"([\w\.-]+@[\w\.-]+\.\w+)"
        ],
        text=email_text
    )

    phone = _safe_search(
        patterns=[
            r"(\+?\d{8,15})"
        ],
        text=email_text
    )

    name = _safe_search(
        patterns=[
            r"Regards,\s*(.+)",
            r"Best regards,\s*(.+)",
            r"Thanks,\s*(.+)"
        ],
        text=email_text
    )

    return {
        "product": product or "Unknown",
        "quantity": quantity or 0,
        "city": city or "Unknown",
        "timeline": timeline or "Not specified",
        "contact_email": email or "Unknown",
        "contact_name": name or "Unknown",
        "phone": phone or "Unknown"
    }
