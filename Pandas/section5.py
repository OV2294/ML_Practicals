import pandas as pd

df = pd.read_csv("Complaint_data_for_section5.csv")

#avg recharge by region.
#print(df.groupby("Region")["MonthlyCharges"].mean())

#Complaint type count
#print(df['issue'].value_counts())

print(df[df['days_since_last_recharge'] > 30])