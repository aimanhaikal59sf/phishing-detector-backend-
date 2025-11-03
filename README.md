# Phishing URL Detection API

A FastAPI service that predicts whether a URL is **phishing** or **legitimate** using machine learning.

## 🚀 Endpoints

| Method | Route     | Description |
|--------|----------|-------------|
| GET    | `/`       | Health check |
| POST   | `/predict` | Predict phishing |

## ✅ Request Example

```json
{
  "url_length": 25,
  "num_subdomains": 1,
  "has_https": 1,
  "has_ip": 0,
  "special_chars": 2,
  "suspicious_keywords": 1,
  "shortened": 0,
  "uncommon_tld": 0,
  "raw_url": "https://paypal.verify-account-login.com"
}
