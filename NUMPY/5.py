import numpy as np

recharges = np.array([199, 299, 579, 399, 599, 699])
avg = np.mean(recharges)
print(f"Average recharge: {avg}")
print()

high_value = recharges[recharges > 500]
print("High Value: ", high_value)
print()

jan = np.array([150, 200, 270, 250])
feb = np.array([180, 230, 210, 260])
diff = feb - jan
print("Monthly Growth: ", diff)
print()

#practice project
amount = np.array([199, 299, 579, 149, 599, 99])
print("Total amount : ", np.sum(amount))
print("Average Recharge: ", np.average(amount))
print("Average Recharge: ", np.mean(amount))
print()

print("Rechanges less than Rs200: " , amount[amount < 200])
print()

print("Simulate recharges value for 10 users: ", np.random.randint(199, 600, size = 10))