"""
Simple test cases for the regex data extractor.
Run with: python test_extractor.py
"""

from data_extractor import extract_all


SAMPLE = """
Emails: user@example.com and firstname.lastname@company.co.uk
Bad email: not-an-email
URLs: https://www.example.com https://subdomain.example.org/page
Phones: (123) 456-7890, 123-456-7890, 123.456.7890
Cards: 1234 5678 9012 3456 and 1234-5678-9012-3456
Times: 14:30 and 2:30 PM
HTML: <p> <div class="example"> <img src="image.jpg" alt="description">
Tags: #example #ThisIsAHashtag
Money: $19.99 $1,234.56
"""


def assert_contains(actual, expected_items, label):
    missing = [item for item in expected_items if item not in actual]
    if missing:
        raise AssertionError(f"{label}: missing {missing}. Got {actual}")


def run_tests():
    results = extract_all(SAMPLE)

    assert_contains(
        results["emails"],
        ["user@example.com", "firstname.lastname@company.co.uk"],
        "emails",
    )
    assert "not-an-email" not in results["emails"]

    assert_contains(
        results["urls"],
        ["https://www.example.com", "https://subdomain.example.org/page"],
        "urls",
    )

    assert_contains(
        results["phone_numbers"],
        ["(123) 456-7890", "123-456-7890", "123.456.7890"],
        "phone_numbers",
    )

    assert_contains(
        results["credit_cards"],
        ["1234 5678 9012 3456", "1234-5678-9012-3456"],
        "credit_cards",
    )

    assert_contains(results["times"], ["14:30", "2:30 PM"], "times")

    assert_contains(
        results["html_tags"],
        ['<p>', '<div class="example">', '<img src="image.jpg" alt="description">'],
        "html_tags",
    )

    assert_contains(
        results["hashtags"],
        ["#example", "#ThisIsAHashtag"],
        "hashtags",
    )

    assert_contains(
        results["currency_amounts"],
        ["$19.99", "$1,234.56"],
        "currency_amounts",
    )

    # Empty / malformed input should not crash
    empty = extract_all("")
    for label, matches in empty.items():
        if matches:
            raise AssertionError(f"Expected no matches for empty text in {label}")

    none_result = extract_all(None)
    if not isinstance(none_result, dict):
        raise AssertionError("None input should still return a dict")

    print("All tests passed.")
    return True


if __name__ == "__main__":
    run_tests()
