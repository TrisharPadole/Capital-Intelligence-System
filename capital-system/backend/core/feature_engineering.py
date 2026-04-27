from backend.core.financial_metrics import (
    compute_ebitda,
    compute_ebitda_margin,
    compute_dscr,
    compute_burn_rate,
    compute_runway,
    compute_leverage
)


import math


def sanitize(value, default=0.0):
    if value is None:
        return default
    if isinstance(value, (int, float)):
        if math.isnan(value) or math.isinf(value):
            return default
        return float(value)
    return default


def build_startup_features(data):
    
    revenue = sanitize(data.get("monthly_revenue"))
    expenses = sanitize(data.get("monthly_operating_expenses"))
    debt_payment = sanitize(data.get("monthly_debt_payment"))
    cash_balance = sanitize(data.get("cash_balance"))
    existing_debt = sanitize(data.get("existing_debt"))

    ebitda = sanitize(compute_ebitda(revenue, expenses))
    burn = sanitize(compute_burn_rate(revenue, expenses))

    features = {
        
        "monthly_revenue": revenue,
        "ebitda": ebitda,
        "ebitda_margin": sanitize(
            compute_ebitda_margin(ebitda, revenue)
        ),
        "dscr": sanitize(
            compute_dscr(ebitda, debt_payment)
        ),
        "burn_rate": burn,
        "runway": sanitize(
            compute_runway(cash_balance, burn)
        ),
        "leverage": sanitize(
            compute_leverage(existing_debt, revenue * 12)
        ),

        "business_age": sanitize(data.get("business_age_years")),
        "employee_count": sanitize(data.get("employee_count")),
        "founder_experience": sanitize(
            data.get("founder_experience_years")
        )
    }

    return features
