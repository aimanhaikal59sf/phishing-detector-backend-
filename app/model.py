import joblib, os
from app.utils import extract_features
model_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "model", "phishing_model.pkl")
model = joblib.load(model_path)
def predict_url(url: str) -> str:
    try:
        pred = model.predict([url])[0]
        return "Phishing" if int(pred) == 1 else "Legitimate"
    except Exception:
        feats = extract_features(url)
        pred = model.predict([feats])[0]
        return "Phishing" if int(pred) == 1 else "Legitimate"
