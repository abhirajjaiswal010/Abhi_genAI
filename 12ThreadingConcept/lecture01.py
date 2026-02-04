"""
TYPE: CONCURRENCY (Multithreading in Python)

DEFINITION:
Concurrency means handling multiple tasks by switching between them
so that they make progress together. Tasks do NOT run truly at the same
time, but they overlap in execution.

In Python, concurrency is commonly achieved using THREADS and is best
suited for I/O-bound or waiting tasks.

WHY THIS IS CONCURRENCY (NOT PARALLELISM):
- Python has a Global Interpreter Lock (GIL)
- Only ONE thread can execute Python bytecode at a time
- Threads switch execution (context switching)
- Tasks appear to run together but are not truly simultaneous

REAL-WORLD EXAMPLE:
A chaiwala:
- Takes orders
- While chai is brewing, takes the next order
- Switches between tasks instead of waiting idle

TOOLS / FUNCTIONS USED:
1. threading.Thread()  -> create a thread
2. thread.start()      -> start thread execution
3. thread.join()       -> wait for thread to finish
4. time.sleep()        -> simulate waiting (I/O)

SYNTAX:
thread = threading.Thread(target=function_name)
thread.start()
thread.join()
"""

import threading
import time


# Task 1: Taking orders (I/O-bound task)
def takeOrder():
    for i in range(1, 4):
        print(f"Taking order for #{i}")
        time.sleep(2)   # Simulates waiting for customer response


# Task 2: Brewing chai (I/O-bound task)
def brewChai():
    for i in range(1, 4):
        print(f"Brewing chai for #{i}")
        time.sleep(3)   # Simulates brewing time


# Creating threads for concurrent execution
orderThread = threading.Thread(target=takeOrder)
brewThread = threading.Thread(target=brewChai)


# Starting both threads
# OS will switch between these threads
orderThread.start()
brewThread.start()


# Waiting for both threads to complete
orderThread.join()
brewThread.join()


# Final message after both tasks finish
print("All orders taken and chai brewed")
