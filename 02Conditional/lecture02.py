# A local cafe wants a program that suggests a snack.
# If a customer asks for cookies or samosa, it confirms the order.
# Otherwise, it says it's not available.

# Task:
# · Take snack input
# . If it's "cookies"
# · Else, show unavailability
# or
# "samosa" , confirm the order


snack = input("Enter Snack (samosa or cookie) :").lower()
if snack == "samosa" or snack == "cookie":
    print(f"your {snack} is available ,order has been taken !")
else:
    print(f"your {snack} is not available , sorry !")
