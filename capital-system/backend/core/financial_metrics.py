import math


def safe_divide(numerator, denominator, default=0.0):
    """
    Safe division to avoid NaN / inf.
    """
    if denominator == 0 or denominator is None:
        return default
    return float(numerator / denominator)


def compute_ebitda(revenue, operating_expenses):
    return float(revenue - operating_expenses)


def compute_ebitda_margin(ebitda, revenue):
    # EBITDA margin bounded between -1 and +1
    margin = safe_divide(ebitda, revenue, default=0.0)
    return max(min(margin, 1.0), -1.0)


def compute_dscr(ebitda, total_emi):
    # DSCR capped to avoid infinity
    dscr = safe_divide(ebitda, total_emi, default=10.0)
    return min(dscr, 10.0)


def compute_burn_rate(revenue, expenses):
    # Burn rate should never be negative
    burn = expenses - revenue
    return max(burn, 0.0)


def compute_runway(cash_balance, burn_rate):
    # Runway capped (months)
    runway = safe_divide(cash_balance, burn_rate, default=24.0)
    return min(runway, 24.0)


def compute_leverage(existing_debt, annual_revenue):
    # Debt / revenue ratio capped
    leverage = safe_divide(existing_debt, annual_revenue, default=0.0)
    return min(leverage, 10.0)
