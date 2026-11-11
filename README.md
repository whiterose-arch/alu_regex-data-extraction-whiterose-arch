# alu_regex-data-extraction-whiterose

Formative One – Regex Onboarding Hackathon

Python project that uses regular expressions to extract useful data from messy text strings (the kind of text you might get back from a web API).

## Project overview

This tool reads sample text and extracts:

1. Email addresses
2. URLs
3. Phone numbers
4. Credit card numbers
5. Times (12-hour and 24-hour)
6. HTML tags
7. Hashtags
8. Currency amounts (USD)

All eight patterns from the assignment are implemented so the extractor covers the full brief and common format variations.

## Project structure

```
alu_regex-data-extraction-whiterose/
├── README.md
├── regex_patterns.py   # All regex patterns
├── data_extractor.py   # Main script that runs the extraction
├── sample_data.txt     # Sample input text
└── test_extractor.py   # Simple test cases
```

## Requirements

- Python 3 (standard library only — no extra packages)

## Setup and usage

1. Clone this repository:

```bash
git clone https://github.com/<your-username>/alu_regex-data-extraction-whiterose.git
cd alu_regex-data-extraction-whiterose
```

2. Run the extractor on the sample file:

```bash
python data_extractor.py
```

3. Run the test cases:

```bash
python test_extractor.py
```

## Sample output

When you run `python data_extractor.py`, you should see groups like:

- Emails: `user@example.com`, `firstname.lastname@company.co.uk`
- URLs: `https://www.example.com`, `https://subdomain.example.org/page`
- Phone numbers: `(123) 456-7890`, `123-456-7890`, `123.456.7890`
- Credit cards: `1234 5678 9012 3456`, `1234-5678-9012-3456`
- Times: `14:30`, `2:30 PM`
- HTML tags: `<p>`, `<div class="example">`, `<img ...>`
- Hashtags: `#example`, `#ThisIsAHashtag`
- Currency: `$19.99`, `$1,234.56`

## Regex notes and edge cases

| Data type | Formats handled | Edge cases considered |
|-----------|-----------------|------------------------|
| Email | `user@example.com`, dotted names, multi-part domains | Ignores text without `@` and a domain |
| URL | `http://` and `https://` with optional path | Ignores links missing a scheme (e.g. `www.example.com`) |
| Phone | `(123) 456-7890`, `123-456-7890`, `123.456.7890` | Short / incomplete numbers are ignored |
| Credit card | Groups of 4 digits separated by space or `-` | Continuous 16-digit strings without separators are not matched |
| Time | `14:30`, `2:30 PM`, `09:05 am` | Invalid hours (e.g. `25:00`) are not matched |
| HTML tags | Opening tags with optional attributes | Looks for well-formed `<tag ...>` shapes |
| Hashtags | `#example`, `#ThisIsAHashtag` | Lone `#` is ignored |
| Currency | `$19.99`, `$1,234.56`, `$5` | `$` alone is ignored |

## How it works

1. Patterns live in `regex_patterns.py`.
2. `data_extractor.py` loads text, runs `re.findall` for each pattern, removes duplicates, and prints results.
3. `test_extractor.py` checks that the expected assignment examples are found and that empty input does not crash.

## Author

whiterose — ALU Formative One (Regex Onboarding Hackathon)
