# Import libraries
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, auc, confusion_matrix, classification_report
import matplotlib.pyplot as plt
import numpy as np

# Generate dataset
X, y = make_classification(n_samples=1000, n_classes=2, random_state=42)

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Probabilities
y_probs = model.predict_proba(X_test)[:, 1]
print(y_probs)

# ROC + AUC
fpr, tpr, thresholds = roc_curve(y_test, y_probs)
roc_auc = auc(fpr, tpr)

print("AUC Score:", roc_auc)

# Find best threshold (Youden's J)
j_scores = tpr - fpr
best_idx = np.argmax(j_scores)
best_threshold = thresholds[best_idx]

print("Best Threshold:", best_threshold)

# Apply best threshold
y_pred_custom = (y_probs >= best_threshold).astype(int)

print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred_custom))
print("\nClassification Report:\n", classification_report(y_test, y_pred_custom))

# Plot ROC
plt.figure(figsize=(8,6))
plt.plot(fpr, tpr, label=f"ROC curve (AUC = {roc_auc:.2f})")
plt.plot([0, 1], [0, 1], linestyle='--')

# Mark threshold points (avoid divide-by-zero bug)
step = max(1, len(thresholds)//10)
for i in range(0, len(thresholds), step):
    plt.scatter(fpr[i], tpr[i], color='red')
    plt.text(fpr[i], tpr[i], f"{thresholds[i]:.2f}", fontsize=8)

# Highlight best threshold
plt.scatter(fpr[best_idx], tpr[best_idx], color='blue', s=120,
            label=f"Best Threshold = {best_threshold:.2f}")

plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve with Thresholds")
plt.legend(loc="lower right")
plt.grid()
plt.show()