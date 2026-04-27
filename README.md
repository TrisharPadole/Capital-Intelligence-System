# 🏦 Capital Intelligence System
> An explainable AI-driven capital decisioning platform for startups & MSMEs

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?style=flat&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![XGBoost](https://img.shields.io/badge/XGBoost-91.5%25_Accuracy-FF6600?style=flat)](https://xgboost.readthedocs.io)
[![Gemini](https://img.shields.io/badge/Gemini_2.5-LLM_Explainability-4285F4?style=flat&logo=google&logoColor=white)](https://deepmind.google/technologies/gemini/)
[![IEEE](https://img.shields.io/badge/IEEE-Published-00629B?style=flat&logo=ieee&logoColor=white)](https://ieee.org)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat)](LICENSE)

---

## 📌 Overview

India has over **63 million MSMEs** contributing ~30% of national GDP, yet most are denied credit due to thin credit histories and collateral-based underwriting. The **Capital Intelligence System** tackles this by shifting from bureau scores to **real-time cash-flow intelligence**, explainable ML, and policy-enforced decisioning.

This is not just a model — it's a full **SaaS-grade credit intelligence platform** that:
- Predicts probability of default with 91.5% accuracy
- Increases loan approval rates by **16 percentage points**
- Maintains a stable default rate (~8.2%)
- Explains every decision in plain language via **Google Gemini 2.5**
- Complies with **RBI Digital Lending Guidelines 2022**

> 📄 **Published Research:** *"A Data-Driven Intelligent Capital Management System Using Machine Learning for Financial Prediction and Optimization"* — IEEE Conference, 2024

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│                  API Gateway (FastAPI)                   │
└───────────────────────┬─────────────────────────────────┘
                        │
        ┌───────────────▼───────────────┐
        │   Financial Intelligence      │
        │   DSCR · Burn Rate · EBITDA   │
        │   Cash Runway · Op. Margin    │
        └───────────────┬───────────────┘
                        │
        ┌───────────────▼───────────────┐
        │     Machine Learning Layer    │
        │   XGBoost · SHAP · Scikit     │
        │   Probability of Default (PD) │
        └───────────────┬───────────────┘
                        │
        ┌───────────────▼───────────────┐
        │       Policy Engine           │
        │  Min DSCR · Max DTI · RBI     │
        │  Deterministic Underwriting   │
        └───────────────┬───────────────┘
                        │
        ┌───────────────▼───────────────┐
        │   Explainability Layer        │
        │   SHAP Feature Importance     │
        │   Gemini 2.5 Plain-Language   │
        │   Guidance & Scheme Matching  │
        └───────────────────────────────┘
```

---

## ✨ Key Features

| Feature | Detail |
|---|---|
| 🔬 Cash-Flow Underwriting | DSCR, Burn Rate, Cash Runway, EBITDA Margin, Operating Margin |
| 🤖 ML Risk Scoring | XGBoost (91.5% acc) benchmarked vs. 5 algorithms |
| 🔍 Explainability | SHAP feature-level explanations per prediction |
| 🗣️ LLM Guidance | Gemini 2.5 for plain-language borrower feedback |
| 🏛️ Policy Engine | Deterministic RBI-aligned underwriting rules |
| 🏢 SaaS-Ready | Multi-tenant, RBAC, API-driven onboarding |
| 📊 Capital Matching | Recommends debt / equity / grants / alternative finance |

---

## 📊 Model Performance

### Algorithm Benchmark

| Algorithm | Accuracy | Precision | Recall | F1-Score |
|---|---|---|---|---|
| Logistic Regression | 84.0% | 82.1% | 79.8% | 81.0% |
| Random Forest | 89.2% | 88.5% | 86.4% | 87.2% |
| SVM | 87.1% | 85.3% | 84.2% | 84.7% |
| **XGBoost** ✅ | **91.5%** | **90.5%** | **89.0%** | **90.1%** |
| Neural Network | 90.0% | 86.4% | 80.7% | 85.0% |

### Financial Inclusion Impact

| Model | Approval Rate | Default Rate |
|---|---|---|
| Traditional (Bureau-based) | 52.0% | 8.5% |
| **Capital Intelligence System** | **68.0%** | **8.2%** |

> ✅ **+16% inclusion with lower default risk** — intelligent policy controls keep credit quality intact.

---

## 🛠️ Tech Stack

```
Backend        →  Python 3.10+, FastAPI, Uvicorn, Pydantic
ML / AI        →  Scikit-learn, XGBoost, SHAP, NumPy, Pandas
LLM            →  Google Gemini 2.5 (google-generativeai)
Reporting      →  ReportLab, Plotly
Persistence    →  Joblib (model serialization)
Config         →  python-dotenv
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- Google Gemini API key

### Installation

```bash
# Clone the repository
git clone https://github.com/trisharpadole/capital-intelligence-system.git
cd capital-intelligence-system

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Configuration

```bash
# Create .env file
cp .env.example .env

# Add your Gemini API key
GEMINI_API_KEY=your_api_key_here
```

### Run the Server

```bash
uvicorn main:app --reload
```

API docs available at: `http://localhost:8000/docs`

---

## 📁 Project Structure

```
capital-intelligence-system/
│
├── main.py                    # FastAPI entry point
├── requirements.txt           # Dependencies
├── .env.example               # Environment template
│
├── core/
│   ├── financial_metrics.py   # DSCR, Burn Rate, EBITDA etc.
│   ├── ml_model.py            # XGBoost training & inference
│   ├── shap_explainer.py      # SHAP feature explanations
│   ├── policy_engine.py       # Deterministic underwriting rules
│   └── gemini_advisor.py      # Gemini 2.5 LLM integration
│
├── api/
│   ├── routes.py              # API endpoints
│   └── schemas.py             # Pydantic request/response models
│
├── models/
│   └── xgboost_model.joblib   # Serialized trained model
│
└── reports/
    └── report_generator.py    # ReportLab PDF generation
```

---

## 🔑 Core Financial Metrics

```python
# Debt Service Coverage Ratio
DSCR = Net Operating Income / Total Debt Service

# EBITDA Margin
EBITDA Margin = (EBITDA / Total Revenue) × 100

# Cash Runway
Cash Runway = Current Cash Balance / Monthly Burn Rate
```

---

## ⚖️ Responsible AI Principles

- **ML estimates risk** — XGBoost outputs a probability of default score
- **Gemini explains decisions** — plain-language guidance for borrowers
- **AI never makes financial decisions** — all final decisions go through the deterministic Policy Engine
- **Full auditability** — every decision is traceable and explainable, per RBI guidelines

---

## 📄 Research Paper

**Title:** A Data-Driven Intelligent Capital Management System Using Machine Learning for Financial Prediction and Optimization

**Authors:** Bhargavi G, Trishar Padole, Rishabh Dhatrak

**Institution:** SRM Institute of Science and Technology, Chennai

**Published:** IEEE Conference, 2024

**Key References:** RBI Digital Lending Guidelines · SHAP (Lundberg & Lee, 2017) · XGBoost · OECD SME Finance Scoreboard

---

## 🤝 Contributing

Contributions are welcome! Please open an issue first to discuss what you'd like to change.

```bash
# Fork the repo, then:
git checkout -b feature/your-feature
git commit -m "Add your feature"
git push origin feature/your-feature
# Open a Pull Request
```

---

## 📬 Contact

**Trishar Padole**
- 📧 trisharpadole1@gmail.com
- 🔗 [LinkedIn](https://linkedin.com/in/trisharpadole)
- 💻 [GitHub](https://github.com/trisharpadole)

---

<p align="center">Built with ❤️ at SRM Institute of Science and Technology · IEEE Published · Promoting Financial Inclusion through Explainable AI</p>
