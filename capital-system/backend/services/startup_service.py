from backend.core.feature_engineering import build_startup_features
from backend.ml.predict import predict_pd
from backend.decisions.startup_policy import startup_decision
from backend.llm.gemini_client import call_gemini
from backend.llm.prompts import startup_explanation_prompt
from backend.llm.memory import store_context
from backend.reports.pdf_generator import generate_startup_pdf
from backend.reports.plot_generator import generate_financial_plots


import math
import numpy as np


def make_json_safe(obj):
    if isinstance(obj, float):
        if math.isnan(obj) or math.isinf(obj):
            return 0.0
        return float(obj)

    if isinstance(obj, np.generic):
        return float(obj)

    if isinstance(obj, dict):
        return {k: make_json_safe(v) for k, v in obj.items()}

    if isinstance(obj, list):
        return [make_json_safe(v) for v in obj]

    return obj


def evaluate_startup(data, session_id=None):
    
    metrics = build_startup_features(data)

    ml_features = [
        data["monthly_revenue"],
        metrics["ebitda"],
        data["employee_count"],
        data["business_age_years"],
        data["founder_experience_years"],
        data["existing_debt"]
    ]

    probability_of_default = predict_pd(ml_features)

    decision, reason = startup_decision(
        probability_of_default,
        metrics
    )

    # 5. LLM explanation (NON-BLOCKING)
    try:
        explanation = call_gemini(
            startup_explanation_prompt(metrics, decision)
        )
    except Exception:
        explanation = "Explanation currently unavailable."

    # 6. Memory (optional)
    if session_id:
        store_context(session_id, metrics)

    # 7. Final response (JSON SAFE)
    response = {
        "probability_of_default": round(float(probability_of_default), 3),
        "decision": decision,
        "policy_reason": reason,
        "financial_metrics": metrics,
        "llm_explanation": explanation
    }
    # Generate reports
    pdf_file = generate_startup_pdf(response)
    chart_file = generate_financial_plots(metrics)

    response["pdf_report_url"] = f"/download/pdf/{pdf_file}"
    response["charts_url"] = f"/view/charts/{chart_file}"


    return make_json_safe(response)
