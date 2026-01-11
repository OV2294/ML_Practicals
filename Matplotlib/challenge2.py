import matplotlib.pyplot as plt

complaint_type = ["Network Issue", "Billing Errors", 
                  "Recharge Problem", "Server Issue"]
complaint_count = [120, 80, 50, 30]

plt.bar(complaint_type, complaint_count, color="red", alpha=0.5)
plt.title("Recharge Plan Usage")
plt.xlabel("Complaint Type")
plt.ylabel("No. of Users")
plt.show()