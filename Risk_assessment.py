
# Cybersecurity Risk Assessment Tool
# Project 1 - Cybersecurity Governance Portfolio

def assess_risk(risk_name, likelihood, impact):
    score = likelihood * impact

    if score >= 20:
        level = "Critical"
    elif score >= 12:
        level = "High"
    elif score >= 6:
        level = "Medium"
    else:
        level = "Low"

    return score, level


# Sample organizational cybersecurity risks
risks = [
    ("Phishing Attack", 4, 5),
    ("Weak Passwords", 3, 4),
    ("Unpatched Software", 4, 4),
    ("Insider Threat", 2, 5),
    ("Data Loss", 3, 5)
]

print("=" * 50)
print("CYBERSECURITY RISK ASSESSMENT REPORT")
print("=" * 50)

for name, likelihood, impact in risks:
    score, level = assess_risk(name, likelihood, impact)

    print(f"\nRisk: {name}")
    print(f"Likelihood: {likelihood}/5")
    print(f"Impact: {impact}/5")
    print(f"Risk Score: {score}/25")
    print(f"Risk Level: {level}")

print("\nAssessment Complete.")
