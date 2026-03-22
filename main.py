from app.sources.hibp_passwords import get_pwned_password_count
from app.services.exposure_analyzer import analyze_exposure

email = "mxsewell@gmail.com"
password = "Password123"

count = get_pwned_password_count(password)

if count > 0:
    severity = "high" if count >= 1000 else "medium"

    finding = {
        "email": email,
        "source": "HIBP",
        "finding_type": "password_exposure",
        "password_seen_count": count,
        "severity": severity,
        "account_scope": "cloud"
    }

    result = analyze_exposure(finding)
    print(result)
else:
    print("✅ Password not found in known breaches.")