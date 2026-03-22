# Exposure Agent (v1)

A lightweight security-focused AI assistant that evaluates password exposure risk using the Have I Been Pwned (HIBP) Pwned Passwords API and generates structured security analysis using Claude.

## Features

- Privacy-preserving password exposure checks (k-anonymity model)
- AI-generated security exposure reports
- MITRE ATT&CK technique mapping for potential follow-on abuse
- Local-only password handling (no plaintext storage or transmission)

## How It Works

1. Password is hashed locally (SHA-1)
2. Only the first 5 characters of the hash are sent to HIBP
3. Matching suffixes are returned and compared locally
4. Exposure count is used to assess risk
5. Claude generates a structured security report

## Example Output

- Summary
- Risk Level
- Recommended Actions
- MITRE ATT&CK Context

