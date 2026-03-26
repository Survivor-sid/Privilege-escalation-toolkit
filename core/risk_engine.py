GTFOBINS = [
"vim","find","perl","awk","python","python3",
"bash","sh","nano","less","more","cp","mv"
]

HIGH_RISK_PATHS = [
"/etc/passwd",
"/etc/shadow",
"/etc/sudoers"
]

def classify(text):

    severity = "LOW"
    mitigation = "Review configuration"

    for g in GTFOBINS:
        if g in text:
            severity = "HIGH"
            mitigation = "Remove SUID bit or restrict execution"

    for p in HIGH_RISK_PATHS:
        if p in text:
            severity = "CRITICAL"
            mitigation = "Restrict file permissions immediately"

    return severity, mitigation
