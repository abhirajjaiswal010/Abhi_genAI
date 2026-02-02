# ───────────────────── Custom Exception Class ─────────────────────
# Definition:
# A custom exception is a user-defined error type created by
# inheriting from Python’s built-in Exception class.
#
# It allows raising meaningful, domain-specific errors instead
# of using generic exceptions.
#
# Use case:
# Custom exceptions improve readability, debugging, and
# error handling in larger applications.
#
# Example:
# class OutOfIngredientError(Exception):
#     pass
#
# raise OutOfIngredientError("Missing milk or sugar")
# ──────────────────────────────────────────────────────────────────


class outofIngredientError(Exception):
    pass

def make_chai(milk,sugar):
    if milk ==0 or sugar ==0:
        raise outofIngredientError("Missing Milk or sugar")
    print("chai is ready ...")

make_chai(0,1)