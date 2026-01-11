import matplotlib.pyplot as plt

user_types = ["Prepaid", "Postpaid"]
user_counts = [650, 350]

plt.figure(figsize = (5,5))
plt.pie(user_counts, labels = user_types, autopct = '%1.1f%%', 
        startangle= 90, colors=["red", "blue"])
plt.title("Prepaid Vs Postpaid User Ratio", fontsize = 14)
plt.show()