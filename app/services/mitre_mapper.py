def map_finding_to_mitre(finding: dict) -> list[dict]:
    finding_type = finding.get("finding_type")
    mappings = []

    if finding_type == "password_exposure":
        count = finding.get("password_seen_count", 0)

        mappings.append({
            "tactic_id": "TA0006",
            "tactic_name": "Credential Access",
            "technique_id": "T1110.004",
            "technique_name": "Credential Stuffing",
            "reason": "A password found in breach corpora may be reused against other accounts and services."
        })

        mappings.append({
            "tactic_id": "TA0001 / TA0003 / TA0004 / TA0005",
            "tactic_name": "Initial Access / Persistence / Privilege Escalation / Defense Evasion",
            "technique_id": "T1078",
            "technique_name": "Valid Accounts",
            "reason": "If the exposed password is valid and reused, an adversary may gain access using legitimate credentials."
        })

        if finding.get("account_scope") == "cloud":
            mappings.append({
                "tactic_id": "TA0001 / TA0003 / TA0004 / TA0005",
                "tactic_name": "Initial Access / Persistence / Privilege Escalation / Defense Evasion",
                "technique_id": "T1078.004",
                "technique_name": "Valid Accounts: Cloud Accounts",
                "reason": "If reused against Microsoft 365, Google Workspace, or other SaaS, the exposure may enable cloud account abuse."
            })

        if count >= 100000:
            mappings.append({
                "tactic_id": "TA0006",
                "tactic_name": "Credential Access",
                "technique_id": "T1110.003",
                "technique_name": "Password Spraying",
                "reason": "Extremely common passwords are also relevant to password spraying risk because attackers often test commonly used choices."
            })

    return mappings