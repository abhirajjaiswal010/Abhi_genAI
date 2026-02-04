#multiprocess with queue and value

import threading
import time 

def cpuHeavy():
    print(f"cruncing some number.....")
    total=0
    for i in range(10**7):
        total +=i
    print("done")

start=time.time()
threads=[threading.Thread(target=cpuHeavy) for _ in range(2)]
[t.start() for t in threads]
[t.join() for t in threads]

print(f"time taken:{time.time()-start:.2f} seconds")