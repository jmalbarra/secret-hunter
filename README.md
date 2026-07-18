# secret-hunter

A small toolkit for finding and validating leaked API keys/secrets in a codebase or file dump.

## What it does

1. `app.py` — scans target files/text for secret-shaped patterns (API keys, tokens, credentials) and writes matches to `secrets.txt`.
2. `openai_key_checker.py` — takes the candidates in `secrets.txt` and checks which ones are actually live OpenAI keys, splitting results into `valid_secrets.txt` and `invalid_secrets.txt` (with the API error code for invalid ones).

## Usage

```bash
python app.py
python openai_key_checker.py
```

Detection rules live in `secret_detector.yaml`, so patterns can be extended without touching the scanning code.

## Why

Leaked keys in public repos, logs, or config dumps are a common and cheap-to-exploit finding. This automates the first two steps of triage: find candidates, then confirm which ones are real before reporting them.

## Responsible use

Only run this against code/data you own or are authorized to test. Confirmed valid secrets should be reported and rotated immediately, not used.
