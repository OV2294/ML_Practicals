import matplotlib.pyplot as plt

labels = ["Prepaid", "Postpaid"]
sizes = [85, 15]
#autopct for decimal places
plt.pie(sizes, labels = labels, autopct = '%1.2f%%') 
plt.title("User Type Distribution")
plt.show()