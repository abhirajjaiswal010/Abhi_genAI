#infinite

def infinte():
    count=1
    while True:
        yield f"refil #{count}"
        count +=1

refill=infinte()

for _ in range(3):
    print(next(refill))