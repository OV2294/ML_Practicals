from pandas import DataFrame
import matplotlib.pyplot as plt

data = {'Plan' : ['199', '399', '599'], 
        'Users': [100, 80, 60]}
df = DataFrame(data)
plt.bar(df["Plan"], df["Users"])
plt.title("Recharge Plan Popularity")
plt.show()