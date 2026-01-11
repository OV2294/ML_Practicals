import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("recharge_data.csv")

print(df["Region"].value_counts().head(5))
df["Region"].value_counts().head(5).plot(kind = 'bar')
plt.title("Top 5 Regions")
plt.show()