# You want to simulate tea heating.
# It starts at 40C and boils at 100°℃.
# Task:
# · Use a while loop.
# · Increase temperature by 15 until it reaches or exceeds 100.
# · Print each temperature step.

i=40
while i<=100:
    print(f"temperature {i}")
    i+=15
print("tea is ready to boil")