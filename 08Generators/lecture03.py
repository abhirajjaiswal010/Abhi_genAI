#send value to generators

def chaiCustomer():
    print("Welcome ! what chai would you like ?")
    order=yield
    while True:
        print(f"preparing :{order}")
        order=yield

stall=chaiCustomer()
next(stall)
stall.send("masala chai")