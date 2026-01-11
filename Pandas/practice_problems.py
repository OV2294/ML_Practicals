import pandas as pd
import numpy as np
"""df = pd.read_csv("recharge_data.csv")
print("Total recharge by plan: ", df.groupby("Contract")["TotalCharges"].sum())"""

df = pd.read_csv('Complaint_data_for_section5.csv')

#df["Churn_Label"] = df["days_since_last_recharge"] > 30
df["Churn_Label"] = np.where(df["days_since_last_recharge"] > 30, "Churned", "Not Churned")
print(df["Churn_Label"])