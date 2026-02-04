"""
TYPE: PARALLELISM (Multiprocessing in Python)

DEFINITION:
Parallelism means executing multiple tasks at the SAME TIME using
multiple CPU cores. Each task runs independently in its own process.

In Python, parallelism is achieved using the multiprocessing module,
where each process has its own memory space and its own Python interpreter.

WHY THIS IS PARALLELISM (NOT CONCURRENCY):
- Each Process runs on a separate CPU core (if available)
- No Global Interpreter Lock (GIL) issue between processes
- Tasks truly execute simultaneously

REAL-WORLD EXAMPLE:
A chai shop with MULTIPLE chai makers 
- Chai maker #1 brews chai
- Chai maker #2 brews chai
- Chai maker #3 brews chai
All chai are prepared at the same time.

TOOLS / FUNCTIONS USED:
1. multiprocessing.Process() -> create a new process
2. process.start()           -> start process execution
3. process.join()            -> wait for process to finish
4. time.sleep()              -> simulate heavy work (CPU / time)

IMPORTANT RULE:
The 'if __name__ == "__main__"' block is REQUIRED on Windows
to prevent infinite process creation.
"""

from multiprocessing import Process
import time


# Task: Brewing chai (CPU / time intensive task)
def brewChai(name):
    print(f"Start of {name} chai brewing")
    time.sleep(3)   # Simulates heavy work
    print(f"End of {name} chai brewing")


# Entry point for multiprocessing
if __name__ == "__main__":

    # Creating multiple processes (parallel execution)
    chaiMakers = [
        Process(target=brewChai, args=(f"chai maker #{i+1}",))
        for i in range(3)
    ]

    # Start all processes
    for p in chaiMakers:
        p.start()

    # Wait for all processes to complete
    for p in chaiMakers:
        p.join()

    print("All chai served")
