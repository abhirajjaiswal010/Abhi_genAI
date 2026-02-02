# ───────────────────────── File Handling in Python ─────────────────────────
# This program demonstrates how to safely write data to a file using
# Python's `with` statement (context manager).
#
# Why use `with`?
# - Automatically opens the file
# - Ensures the file is properly closed after use
# - Prevents resource leaks, even if an error occurs
#
# This approach is preferred over manually using open() and close().
# ──────────────────────────────────────────────────────────────────────────


def save_order():
    """
    Writes a tea order to a file.
    The file is automatically closed after the block execution.
    """

    # Open the file in write mode ("w")
    # If the file does not exist, it will be created
    # If it exists, its content will be overwritten
    with open("order.txt", "w") as file:
        file.write("ginger tea - 4 cups")

    # This line executes after the file is safely closed
    print("Order saved successfully.")


# Function call
save_order()
