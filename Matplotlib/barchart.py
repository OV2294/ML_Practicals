import matplotlib.pyplot as plt

plans = ["₹199", "₹249", "₹399"]
users = [50, 80, 120]

plt.bar(plans, users, color="blue", alpha = 0.5)
plt.title("Recharge plan usage")
plt.ylabel("No. of Users")
plt.xlabel("Amount")
plt.show()