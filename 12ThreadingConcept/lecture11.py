#multiprocess with queue and value

from multiprocessing import Process
import time 

def cpuHeavy():
    print(f"cruncing some number.....")
    total=0
    for i in range(10**9):
        total +=i
    print("done")

if __name__=="__main__":
    start=time.time()
    processes=[Process(target=cpuHeavy) for _ in range(2)]
    [t.start() for t in processes]
    [t.join() for t in processes]

    print(f"time taken:{time.time()-start:.2f} seconds")