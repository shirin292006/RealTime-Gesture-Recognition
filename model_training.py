# model_training.py

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

# 1. Load your combined gesture data
df = pd.read_csv("gesture_data/combined_data.csv")

# 2. Split into features (X) and labels (y)
X = df.drop('label', axis=1)
y = df['label']

# 3. Split data into training and testing sets (80/20 split)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4. Train the model (Random Forest)
model = RandomForestClassifier()
model.fit(X_train, y_train)

# 5. Test the model
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))

# 6. Save the trained model to a file
joblib.dump(model, "gesture_model.pkl")
print("✅ Model saved as 'gesture_model.pkl'")
