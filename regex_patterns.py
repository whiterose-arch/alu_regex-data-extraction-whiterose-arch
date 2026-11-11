"""
Regex patterns for extracting common data types from text.
Each pattern is documented with examples and notes about edge cases.
"""

# Email: local part, @, domain with at least one dot
# Handles: user@example.com, firstname.lastname@company.co.uk
# Rejects bare words without @ or domain dots when matched carefully
EMAIL_REGEX = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

# URL: http or https with optional path
# Handles: https://www.example.com, https://subdomain.example.org/page
URL_REGEX = r"https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/[^\s]*)?"

# Phone: (123) 456-7890, 123-456-7890, 123.456.7890
PHONE_REGEX = (
    r"(?:\(?\d{3}\)?[-.\s]\d{3}[-.\s]\d{4})"
)

# Credit card: 16 digits with spaces or dashes between groups of 4
# Handles: 1234 5678 9012 3456, 1234-5678-9012-3456
CREDIT_CARD_REGEX = r"\b\d{4}[-\s]\d{4}[-\s]\d{4}[-\s]\d{4}\b"

# Time: 12-hour first (2:30 PM), then 24-hour (14:30)
# 12-hour must come first so "2:30 PM" is not truncated to "2:30"
TIME_REGEX = (
    r"\b(?:(?:0?[1-9]|1[0-2]):[0-5]\d\s?[APap][Mm]|(?:[01]?\d|2[0-3]):[0-5]\d)\b"
)

# HTML tags: opening tags with optional attributes
# Handles: <p>, <div class="example">, <img src="image.jpg" alt="description">
HTML_TAG_REGEX = r"<[a-zA-Z][^>]*>"

# Hashtags: # followed by word characters
# Handles: #example, #ThisIsAHashtag
HASHTAG_REGEX = r"#[A-Za-z0-9_]+"

# Currency (USD): $19.99, $1,234.56
CURRENCY_REGEX = r"\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?"

# Friendly names used when printing results
PATTERN_LABELS = {
    "emails": EMAIL_REGEX,
    "urls": URL_REGEX,
    "phone_numbers": PHONE_REGEX,
    "credit_cards": CREDIT_CARD_REGEX,
    "times": TIME_REGEX,
    "html_tags": HTML_TAG_REGEX,
    "hashtags": HASHTAG_REGEX,
    "currency_amounts": CURRENCY_REGEX,
}
