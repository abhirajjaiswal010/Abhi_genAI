
# A tea stall offers different prices for different cup sizes.
# Write a program that calculates the price based on size.

# Task:
# · Input: "small", "medium", "large"
# · Small -> ₹10, Medium -> ₹15, Large -> ₹20
# . If invalid: show"Unknown cup size"

print("Choose the tea cup size below is list")
print("small -> 10 rupees")
print("medium -> 15 rupees")
print("large-> 20 rupees")
print("="*50)
size=input("enter the cup size of your tea :").lower()

if size=="small":
    print(f"you choose {size} , price is 10 rupee")
elif size=="large":
     print(f"you choose {size} , price is 15 rupee")
elif size=="medium":
     print(f"you choose {size} , price is 20 rupee")
else : 
     print("unknown cup size")