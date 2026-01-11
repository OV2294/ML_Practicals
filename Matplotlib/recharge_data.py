import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('recharge_data.csv')
#print(df)
"""if 'plan_name' in df.columns:
    df['plan_name'].value_counts().head(5).plot(kind = 'bar')

    plt.title("Top 5 Recharges Plan")
    plt.xlabel("Recharge Plan")
    plt.ylabel("Frequency")

    plt.show()
else:
    print("The 'Plan' colume does not exist in the file.")"""

if 'amount' in df.columns:
    df['bonus1'] = df['amount'] * 0.10
    df.to_csv('recharge_dat.csv', index=False)
    print("Bonus col is added")
else:
    print("Couldn't add")