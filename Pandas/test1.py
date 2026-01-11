import pandas as pd

df = pd.read_csv("recharge_data.csv")
"""print(df.head())  #first 5 rows
print(df.to_string()) #to display all records from table."""


"""print(df.shape)  #show no. of rows and cols.
print(df.columns) #column names.
print(df.info()) #datatypes and nulls.
print(df.describe()) #summary stats."""

"""print(df["Month"].head()) #prints month column data of 1st 5 rows.
print(df[["Month", "MonthlyCharges"]].head())
print(df.loc[0])
print(df.iloc[0:3])
print(df.CustomerID[1], df.MonthlyCharges[0], df.Month[5])"""

"""print(df["MonthlyCharges"].sum())
print()
print(df["MonthlyCharges"].mean())
print()
print(df["MonthlyCharges"].max())
print()
print(df["MonthlyCharges"].min())
print()
print(df["CustomerID"].value_counts())
print()"""

#print(df.groupby("Region")["MonthlyCharges"].sum())
#print(df.groupby(["Region", "Contract"])["MonthlyCharges"].sum())
#print(df.groupby(["Region", "Contract"])["MonthlyCharges"].count())

"""print(df.isnull().sum())
print(df.dropna())
print(df.fillna(0))"""

"""print(df.rename(columns = {'MonthlyCharges': 'RechargeAmount'}, inplace = True))
print(df.head())"""

#print(df[df["MonthlyCharges"] > 1000])
#print(df[df["Region"] == "West"])
#print(df[df["Contract"] == "Two year"])

"""df["Bonus"] = df["MonthlyCharges"] * 0.10
df["Recharge_Flag"] = df["MonthlyCharges"] > 500
print(df)
print(df["Bonus"].head())
print(df["Recharge_Flag"].head())"""

#print(df.sort_values("MonthlyCharges", ascending = False).head())

"""df.to_csv("cleaned_recharge_data.csv", index = False)
print(df)"""

print(df.tail())