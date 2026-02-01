flavours=["masala","ginger","lemon","mint"]
print("available flavours :",flavours)
while (flavour := input("choose your flavours : "))not in flavours :
       print(f"sorry,{flavour} is not available")
print(f"you choose {flavour} chai")