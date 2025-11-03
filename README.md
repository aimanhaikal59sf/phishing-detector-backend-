# Phishing Detector Backend

Repo contains a FastAPI backend that exposes an endpoint `/predict`.

## Run locally
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Generate model locally
```bash
python training/train_model.py
```
