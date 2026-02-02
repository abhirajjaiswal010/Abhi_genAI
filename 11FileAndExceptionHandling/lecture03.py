# ───────────────────── Catching Multiple Exceptions ─────────────────────
# Definition:
# Catching multiple exceptions allows handling more than one
# possible error using a single except block, when the handling
# logic is the same for those exceptions.
#
# Syntax:
# except (ExceptionType1, ExceptionType2, ...):
#     handle_error
#
# Example:
# except (ValueError, TypeError):
#     print("Invalid input")
# ─────────────────────────────────────────────────────────────────────────

def processOrder(item, quantity):
    try:
        price = {"masala": 20}[item]   # lookup item price
        quantity = int(quantity)       # ensure quantity is a number
        cost = price * quantity
        print(f"Total cost is {cost}")

    except KeyError:
        print("Sorry, this item is not on the menu")

    except ValueError:
        print("Quantity must be a valid number")

    except TypeError:
        print("Quantity must be a number")

processOrder("ginger",2)
processOrder("masala","two")