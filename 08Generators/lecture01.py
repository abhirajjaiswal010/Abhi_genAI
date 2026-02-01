# basic

def serve_chai():
    yield "cup1: masala chai"
    yield "cup2: ginger chai"
    yield "cup3: elaichi chai"
    
stall =serve_chai()
for cup in stall:
    print(cup)

def getChaiList():
    return ["cup 1","cup 2","cup 3"]

def getChaiGet():
    yield "cup1"
    yield "cup2"
    yield "cup3"

chai=getChaiGet()
print(next(chai))