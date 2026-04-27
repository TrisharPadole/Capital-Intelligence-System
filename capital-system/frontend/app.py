import streamlit as st
import requests
import plotly.graph_objects as go
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import tempfile

API_URL = "http://127.0.0.1:8000/startup/evaluate"

st.set_page_config(page_title="Startup Capital Intelligence", layout="centered")

st.title("📊 Startup Capital Intelligence System")

# -------------------------
# INPUT FORM
# -------------------------
with st.form("startup_form"):
    st.subheader("Startup Financial Inputs")

    monthly_revenue = st.number_input("Monthly Revenue (₹)", value=1500000)
    operating_expenses = st.number_input("Monthly Operating Expenses (₹)", value=900000)
    debt_payment = st.number_input("Monthly Debt Payment (₹)", value=180000)
    cash_balance = st.number_input("Cash Balance (₹)", value=4200000)
    existing_debt = st.number_input("Existing Debt (₹)", value=2500000)
    business_age = st.number_input("Business Age (Years)", value=4)
    employees = st.number_input("Employee Count", value=22)
    founder_experience = st.number_input("Founder Experience (Years)", value=8)

    submitted = st.form_submit_button("Evaluate Startup")

# -------------------------
# CALL BACKEND
# -------------------------
if submitted:
    payload = {
        "monthly_revenue": monthly_revenue,
        "monthly_operating_expenses": operating_expenses,
        "monthly_debt_payment": debt_payment,
        "cash_balance": cash_balance,
        "existing_debt": existing_debt,
        "business_age_years": business_age,
        "employee_count": employees,
        "founder_experience_years": founder_experience
    }

    response = requests.post(API_URL, json=payload)

    if response.status_code != 200:
        st.error("Backend error. Check FastAPI logs.")
    else:
        result = response.json()
        st.success(f"Decision: {result['decision']}")

        metrics = result["financial_metrics"]

        # -------------------------
        # PLOTLY VISUALS
        # -------------------------
        st.subheader("📈 Financial Health Indicators")

        fig = go.Figure()

        fig.add_trace(go.Bar(
            x=["EBITDA", "Monthly Revenue"],
            y=[metrics["ebitda"], metrics["monthly_revenue"]],
            name="Profitability"
        ))

        fig.add_trace(go.Bar(
            x=["DSCR", "Runway (months)"],
            y=[metrics["dscr"], metrics["runway"]],
            name="Liquidity"
        ))

        st.plotly_chart(fig, use_container_width=True)

        st.subheader("🧠 AI Explanation")
        st.write(result["llm_explanation"])

        # -------------------------
        # PDF GENERATION
        # -------------------------
        def generate_pdf(data):
            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
            c = canvas.Canvas(temp_file.name, pagesize=A4)
            width, height = A4

            y = height - 50
            c.setFont("Helvetica-Bold", 14)
            c.drawString(50, y, "Startup Capital Intelligence Report")

            c.setFont("Helvetica", 10)
            y -= 40

            for key, value in data.items():
                c.drawString(50, y, f"{key}: {value}")
                y -= 18

            c.save()
            return temp_file.name

        pdf_path = generate_pdf({
            "Decision": result["decision"],
            "Probability of Default": result["probability_of_default"],
            "EBITDA": metrics["ebitda"],
            "DSCR": metrics["dscr"],
            "Runway (months)": metrics["runway"],
            "Leverage": metrics["leverage"]
        })

        with open(pdf_path, "rb") as f:
            st.download_button(
                "📄 Download PDF Report",
                f,
                file_name="startup_capital_report.pdf"
            )
