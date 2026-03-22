from app.claude_client import send_prompt
from app.services.mitre_mapper import map_finding_to_mitre


def analyze_exposure(finding: dict) -> str:
    mitre_mappings = map_finding_to_mitre(finding)

    mitre_text = ""
    if mitre_mappings:
        mitre_lines = []
        for item in mitre_mappings:
            mitre_lines.append(
                f'- {item["technique_id"]} {item["technique_name"]}: {item["reason"]}'
            )
        mitre_text = "\n".join(mitre_lines)
    else:
        mitre_text = "No ATT&CK mappings identified."

    if finding.get("finding_type") == "password_exposure":
        prompt = f"""
You are a cybersecurity exposure analyst.

A password exposure finding was detected.

Email: {finding["email"]}
Source: {finding["source"]}
Finding Type: {finding["finding_type"]}
Password Seen Count: {finding["password_seen_count"]}
Severity: {finding["severity"]}

Relevant MITRE ATT&CK mappings:
{mitre_text}

Write a concise security exposure report with these sections:
1. Summary
2. Risk Level
3. Recommended Actions
4. MITRE ATT&CK Context

Important:
- Do not claim active compromise unless evidence says so.
- Frame ATT&CK techniques as likely follow-on abuse paths.
- Keep it professional and practical.
"""
    else:
        prompt = f"""
You are a cybersecurity exposure analysis assistant.

A credential-related finding was detected.

Finding:
{finding}

Relevant MITRE ATT&CK mappings:
{mitre_text}

Write a concise security exposure report with these sections:
1. Summary
2. Risk Level
3. Recommended Actions
4. MITRE ATT&CK Context

Important:
- Do not claim active compromise unless evidence says so.
- Frame ATT&CK techniques as likely follow-on abuse paths.
- Keep it professional and practical.
"""

    return send_prompt(prompt)