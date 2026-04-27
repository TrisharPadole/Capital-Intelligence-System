from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

#from services.startup_service import evaluate_startup


from backend.services.startup_service import evaluate_startup


app = FastAPI(
    title="Startup Capital Intelligence System",
    description="AI-powered financial decisioning platform for startups",
    version="1.0.0"
    openapi_url=None 
)


class StartupInput(BaseModel):
    monthly_revenue: float
    monthly_operating_expenses: float
    monthly_debt_payment: float
    cash_balance: float
    existing_debt: float
    business_age_years: int
    employee_count: int
    founder_experience_years: int
    capital_need: float



@app.post("/startup/evaluate")
def evaluate_startup_api(
    data: StartupInput,
    session_id: Optional[str] = None
):
    try:
        return evaluate_startup(data.dict(), session_id)
    except Exception as e:
        
        raise HTTPException(
            status_code=500,
            detail=f"Startup evaluation failed: {str(e)}"
        )
