from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os
from datetime import datetime


def generate_startup_pdf(result: dict):
    os.makedirs("backend/generated_reports", exist_ok=True)

    filename = f"startup_credit_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    filepath = os.path.join("backend/generated_reports", filename)

    c = canvas.Canvas(filepath, pagesize=A4)
    width, height = A4

    y = height - 50

    # Title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, y, "Startup Capital Intelligence Report")
    y -= 30

    c.setFont("Helvetica", 10)
    c.drawString(50, y, f"Generated on: {datetime.now().strftime('%d %b %Y')}")
    y -= 40

    # Decision
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "Decision Summary")
    y -= 20

    c.setFont("Helvetica", 10)
    c.drawString(50, y, f"Decision: {result['decision']}")
    y -= 15
    c.drawString(50, y, f"Probability of Default: {result['probability_of_default']}")
    y -= 30

    # Financial Metrics
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "Key Financial Metrics")
    y -= 20

    c.setFont("Helvetica", 10)
    for key, value in result["financial_metrics"].items():
        c.drawString(50, y, f"{key.replace('_',' ').title()}: {value}")
        y -= 15

    y -= 20

    # Explanation
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y, "AI Explanation")
    y -= 20

    c.setFont("Helvetica", 9)
    text = c.beginText(50, y)
    for line in result["llm_explanation"].split("\n"):
        text.textLine(line)
    c.drawText(text)

    c.save()

    return filename
