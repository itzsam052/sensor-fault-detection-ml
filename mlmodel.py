
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
import os
os.makedirs("outputs/plots", exist_ok=True)

# Load data
df = pd.read_csv("data/processed_data.csv")

# Features & target
X = df[["signal", "rolling_mean", "rolling_std", "diff", "rolling_mean_long"]]
y = df["fault"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = RandomForestClassifier(
    n_estimators=300,
    max_depth=12,
    class_weight='balanced',
    random_state=42
)

model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Report
print(classification_report(y_test, y_pred))

# ✅ Confusion Matrix (AFTER prediction)
cm = confusion_matrix(y_test, y_pred)

sns.heatmap(cm, annot=True, fmt='d')
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.savefig("outputs/plots/confusion_matrix.png")
plt.show()

# Save model
joblib.dump(model, "model.pkl")