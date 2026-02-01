# You're preparing an order summary with customer names
# and their total bill.
# Task:
# · Use two lists: one for names and one for bills.
# · Print: "[Name] paid ₹[amount]"

names=["abhiraj","raj","andy"]
bills=[20,50,30]

for name,amount in zip(names,bills):
    print(f"{name} paid {amount} rupees ")