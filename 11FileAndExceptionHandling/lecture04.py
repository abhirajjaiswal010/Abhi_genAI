# ───────────────────── Raising Your Own Exception ─────────────────────
# Definition:
# Raising your own exception allows you to manually trigger an error
# when a specific condition is not met.
#
# This is useful for input validation and enforcing business rules
# instead of allowing the program to fail silently or behave incorrectly.
#
# Syntax:
# raise ExceptionType("Custom error message")
#
# Example:
# raise ValueError("Unsupported chai flavor")
# ───────────────────────────────────────────────────────────────────────


def brewChai(flavor):
    if flavor not in ["masala","ginger","elaichai"]:
        raise ValueError("Unsupported chai flavor....")
    print(f"breing {flavor} chai....")

brewChai("mint")