#https://tinyurl.com/advdataset

# Import required libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 1. Load CSV file
data = pd.read_csv("D:\\Advertising.csv")   # change to your file name

# 2. Separate features and target
# Assume last column is target
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

# 3. Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4. Standardize features (important before PCA)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 5. Apply PCA
pca = PCA(n_components=2)  # change number of components if needed
X_train_pca = pca.fit_transform(X_train_scaled)
X_test_pca = pca.transform(X_test_scaled)



#6. Convert PCA results to DataFrame
pca_df_train = pd.DataFrame(X_train_pca, columns=["PCA1", "PCA2"])
pca_df_test = pd.DataFrame(X_test_pca, columns=["PCA1", "PCA2"])

print("All PCA1 values (train):")
print(pca_df_train["PCA1"])

print("\nAll PCA1 values (test):")
print(pca_df_test["PCA1"])

# 7. Train Linear Regression model
model = LinearRegression()
model.fit(X_train_pca, y_train)

# 8. Make predictions
y_pred = model.predict(X_test_pca)

# 9. Evaluate model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error:", mse)
print("R2 Score:", r2)