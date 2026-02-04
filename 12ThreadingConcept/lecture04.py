import threading
import time

# -------------------------------------------------
# GIL DEMO CODE
# -------------------------------------------------
# This program shows that Python threads do NOT run
# CPU-heavy work in parallel because of the GIL
# (Global Interpreter Lock)
# -------------------------------------------------


def BrewChai():
    """
    This function represents a CPU-bound task.
    CPU-bound means:
    - No waiting
    - Continuous calculation
    - CPU is busy all the time

    Because of GIL, only ONE thread can execute
    this Python code at a time.
    """

    # Get current thread name (just for clarity)
    print(f"{threading.current_thread().name} started brewing...")

    count = 0

    # Heavy loop (CPU-bound work)
    # While this loop runs, the thread HOLDS the GIL
    # Other threads must WAIT
    for _ in range(100_000_000):
        count += 1

    print(f"{threading.current_thread().name} finished brewing...")


# -------------------------------------------------
# Creating two threads
# -------------------------------------------------
# Both threads run the SAME function
# But due to GIL, they will NOT run in parallel
thread1 = threading.Thread(target=BrewChai, name="barista-1")
thread2 = threading.Thread(target=BrewChai, name="barista-2")


# -------------------------------------------------
# Measuring total execution time
# -------------------------------------------------
start = time.time()

# Start both threads
thread1.start()
thread2.start()

# join() makes main thread wait
# until both threads finish execution
thread1.join()
thread2.join()

end = time.time()

# Total time taken by both threads
print(f"Total time taken: {end - start:.2f} seconds")


# -------------------------------------------------
# IMPORTANT LEARNING (READ THIS)
# -------------------------------------------------
# 1. Even though we used two threads,
#    CPU-heavy work is NOT parallel in Python.
#
# 2. Reason: GIL (Global Interpreter Lock)
#    - Only one thread can execute Python code at a time
#
# 3. Threads here run one after another (switching),
#    not at the same time.
#
# 4. Threading is GOOD for:
#    - time.sleep()
#    - file I/O
#    - network calls
#
# 5. Threading is BAD for:
#    - heavy loops
#    - calculations
#    - CPU-bound work
#
# 6. For real parallelism, use multiprocessing.
# -------------------------------------------------
