import os
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
import joblib

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "startup_synthetic_dataset.xlsx")
MODEL_PATH = os.path.join(BASE_DIR, "models", "startup_lr.pkl")

df = pd.read_excel(DATA_PATH)

features = [
    "monthly_revenue",
    "ebitda",
    "employee_count",
    "business_age_years",
    "founder_experience_years",
    "existing_debt"
]

X = df[features]
y = (df["capital_readiness_score"] >= 65).astype(int)

pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LogisticRegression())
])

pipeline.fit(X, y)

joblib.dump(pipeline, MODEL_PATH)

print("Model pipeline trained and saved successfully.")
