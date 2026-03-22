import hashlib
import httpx

HIBP_PASSWORD_API = "https://api.pwnedpasswords.com/range/{prefix}"


def get_pwned_password_count(password: str) -> int:
    # Step 1: SHA-1 hash locally
    sha1_hash = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()

    prefix = sha1_hash[:5]
    suffix = sha1_hash[5:]

    url = HIBP_PASSWORD_API.format(prefix=prefix)

    headers = {
        "user-agent": "exposure-agent-by-ruin"
    }

    # Step 2: Send only prefix
    response = httpx.get(url, headers=headers, timeout=10.0)

    if response.status_code != 200:
        raise Exception(f"HIBP Password API error: {response.status_code}")

    # Step 3: Check suffix locally
    hashes = response.text.splitlines()

    for line in hashes:
        returned_suffix, count = line.split(":")
        if returned_suffix == suffix:
            return int(count)

    return 0