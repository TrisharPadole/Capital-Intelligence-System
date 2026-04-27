import os
import joblib
import numpy as np
import math

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "startup_lr.pkl")

pipeline = joblib.load(MODEL_PATH)

def predict_pd(feature_vector):
    """
    Returns a JSON-safe probability of default.
    """

    X = np.array(feature_vector, dtype=float).reshape(1, -1)
    prob = pipeline.predict_proba(X)[0][1]
    prob = float(prob)

    if math.isnan(prob) or math.isinf(prob):
        return 0.5

    return min(max(prob, 0.0), 1.0)
