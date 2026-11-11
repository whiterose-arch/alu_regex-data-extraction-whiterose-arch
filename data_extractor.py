"""
Extract emails, URLs, phones, credit cards, times, HTML tags,
hashtags, and currency amounts from a block of text using regex.
"""

import re
from regex_patterns import PATTERN_LABELS


def extract_all(text):
    """
    Run every regex pattern against `text` and return a dict
    of label -> list of matches (empty list if nothing found).
    """
    if text is None:
        text = ""

    results = {}
    for label, pattern in PATTERN_LABELS.items():
        matches = re.findall(pattern, text)
        # Keep unique matches while preserving order
        seen = set()
        unique = []
        for match in matches:
            if match not in seen:
                seen.add(match)
                unique.append(match)
        results[label] = unique
    return results


def print_results(results):
    """Pretty-print extraction results to the console."""
    print("=" * 50)
    print("REGEX DATA EXTRACTION RESULTS")
    print("=" * 50)

    for label, matches in results.items():
        title = label.replace("_", " ").title()
        print(f"\n{title} ({len(matches)} found):")
        if matches:
            for item in matches:
                print(f"  - {item}")
        else:
            print("  (none)")

    print("\n" + "=" * 50)


def main():
    sample_path = "sample_data.txt"

    try:
        with open(sample_path, "r", encoding="utf-8") as file:
            text = file.read()
    except FileNotFoundError:
        print(f"Could not find {sample_path}. Using built-in sample text.")
        text = (
            "Contact user@example.com or firstname.lastname@company.co.uk. "
            "Visit https://www.example.com and https://subdomain.example.org/page. "
            "Call (123) 456-7890, 123-456-7890, or 123.456.7890. "
            "Card: 1234 5678 9012 3456 or 1234-5678-9012-3456. "
            "Meeting at 14:30 or 2:30 PM. "
            "Tags: <p> <div class=\"example\"> "
            '<img src="image.jpg" alt="description"> '
            "Follow #example and #ThisIsAHashtag. "
            "Prices: $19.99 and $1,234.56."
        )

    results = extract_all(text)
    print_results(results)
    return results


if __name__ == "__main__":
    main()
