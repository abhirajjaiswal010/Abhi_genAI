# Some chai flavors are out of stock.
# You want to skip those and stop entirely if
# someone requests a restricted flavor.
# Task:
# · Skip if flavor is "Out of Stock"
# . Break if flavor is "Discontinued"

flavours=["ginger","out of stock","lemon","discontinued"]

for flavour in flavours:
    if flavour=="out of stock":
        continue
    if flavour =="discontinued":
        break
    print(f"{flavour} item found")
print("out side of loop ")