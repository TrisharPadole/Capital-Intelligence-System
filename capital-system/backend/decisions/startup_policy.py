def startup_decision(pd, metrics):
    if metrics["ebitda"] < 0:
        return "Grant / Equity", "Negative EBITDA"

    if metrics["ebitda_margin"] < 0.1:
        return "Avoid Debt", "Low operating margin"

    if metrics["runway"] < 6:
        return "Grant / Bridge Capital", "Low cash runway"

    if metrics["dscr"] < 1.2:
        return "Smaller Loan / Longer Tenure", "Weak debt coverage"

    if pd > 0.6:
        return "High Risk", "High probability of default"

    return "Term Loan / MSME Loan", "Healthy financial profile"
