import joblib
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import os
os.makedirs('model', exist_ok=True)
X = np.random.randint(0, 10, (200, 8))
y = np.random.randint(0, 2, 200)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)
joblib.dump(model, 'model/phishing_model.pkl')
print('Saved model to model/phishing_model.pkl')
