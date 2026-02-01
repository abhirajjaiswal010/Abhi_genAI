# CASE STUDY: SHOP DISCOUNT CHECK
# Ek shop hai 🏪
# Rule:

# Agar customer premium member hai → 10% discount

# Normal customer → no discount

# Problem:
# ❌ Har bill function me discount logic likhna pade
# ❌ Code repeat hoga

from functools import wraps


def premiumCustomer(func):
    @wraps(func)
    def wrapper(customer, amount):
        if customer == "premium":
            amount = amount * 0.9
            print("your premium customer , you have 10%off in your bill ")
        return func(customer, amount)
    return wrapper

@premiumCustomer
def generateBill(customer,amount):
    print(f"final bill for {customer}:{amount}")


generateBill("normal",200)
generateBill("premium",300)