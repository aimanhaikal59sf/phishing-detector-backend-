import os
import joblib
from typing import Any
from app.utils import extract_features

# Path to model file (adjust if your layout differs)
MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "model", "phishing_model.pkl")

# Load model once at import time
try:
    model = joblib.load(MODEL_PATH)
except Exception as e:
    # Fail loud so you notice in logs; you can handle fallback later
    raise RuntimeError(f"Failed to load model at {MODEL_PATH}: {e}")

def predict_url(url: str) -> dict:
    """
    Accept a URL string, return a prediction string or dict.
    This tries to use the model as a text pipeline first,
    then falls back to numeric features if needed.
    """
    # First attempt: text-based pipeline (TF-IDF, etc.)
    try:
        pred = model.predict([url])[0]
        # If predict_proba exists, get confidence
        if hasattr(model, "predict_proba"):
            proba = model.predict_proba([url])[0]
            confidence = float(proba[1]) if len(proba) > 1 else float(max(proba))
        else:
            confidence = 1.0
        verdict = "Phishing" if int(pred) == 1 else "Legitimate"
        return {"verdict": verdict, "confidence": confidence}
    except Exception:
        # Fallback: numeric features (if model expects numeric arrays)
        features = extract_features(url)               # returns list: numeric features + raw url maybe
        # If extract_features returns a list with raw url at end, ensure numeric-only
        if isinstance(features, (list, tuple)) and len(features) >= 1 and isinstance(features[-1], str):
            numeric_feats = features[:-1]
        else:
            numeric_feats = features
        pred = model.predict([numeric_feats])[0]
        confidence = None
        if hasattr(model, "predict_proba"):
            proba = model.predict_proba([numeric_feats])[0]
            confidence = float(proba[1]) if len(proba) > 1 else float(max(proba))
        verdict = "Phishing" if int(pred) == 1 else "Legitimate"
        return {"verdict": verdict, "confidence": confidence}
