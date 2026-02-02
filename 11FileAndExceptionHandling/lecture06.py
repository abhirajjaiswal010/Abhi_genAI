# ───────────────────── Custom Error + Billing Logic ─────────────────────
# This example demonstrates:
# 1. Creating a custom exception for business-rule validation
# 2. Manually raising errors using `raise`
# 3. Handling both custom and built-in exceptions
# 4. Using `finally` for guaranteed execution
#
# Workflow:
# - Validate chai flavor using a custom exception
# - Validate input type for number of cups
# - Calculate total bill if all validations pass
# - Catch any raised exception and display the error message
# - Execute cleanup / final message using `finally`
#
# Why this matters:
# - Custom exceptions clearly represent domain-specific errors
# - Centralized error handling prevents program crashes
# - `finally` ensures important code always runs
# ───────────────────────────────────────────────────────────────────────

class InvalidChaiError (Exception):pass

def bill(flavor,cups):
    menu = {"masala":20,"ginger":40}
    try:
        if flavor not in menu:
            raise InvalidChaiError("that chai is not available")
        if not isinstance(cups,int):
            raise TypeError("Number of cups must be an integer")
        total= menu[flavor]*cups 
        print(f"your bill for {cups} cups of {flavor} chai: rupees {total}")

    except Exception as e:
        print("Error :",e)
    finally : 
        print("Thank you for visiting cafe")

bill("mint",2)
bill("masala","three")
bill("ginger",3)

