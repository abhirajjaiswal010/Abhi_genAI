# You run an online tea store.
# If the order amount is more than ₹300, delivery is free;
# otherwise, it costs ₹30.

# Task:

# . Input: order_amount
# · Use ternary operator to decide delivery fee

order_amount=int(input("enter the order amount :"))

print(f"Order amount : {order_amount}")
# if order_amount>300:
#     print("delivery is free")
# else :
#     print("delivery charge will be 30")

delivery_fees=0 if order_amount>300 else 30
print(f"your delivery charge will be {delivery_fees}")
