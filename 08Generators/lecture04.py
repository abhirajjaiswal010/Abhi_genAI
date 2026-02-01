def localChai():
    yield "masala chai"
    yield "masala chai"

def importedChai():
    yield "matcha"
    yield "oolong"

def fullMenu():
    yield from localChai()
    yield from importedChai()

for chai in fullMenu():
    print(chai)


def chaiStall():
    try:
        while True:
            order= yield "waiting for chai order"
    except:
        print("stall closed ,no more chai")

stall = chaiStall()
print(next(stall))
stall.close()
     