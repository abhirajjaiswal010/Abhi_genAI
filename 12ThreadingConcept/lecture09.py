# Thread synchronization using Lock
# Prevents race condition on shared data

import threading

# Shared resource accessed by all threads
counter = 0

# Lock to ensure mutual exclusion
lock = threading.Lock()

def increment():
    global counter
    
    # Each thread increments counter 100000 times
    for _ in range(100000):
        
        # Acquire lock before entering critical section
        # Only one thread can execute this at a time
        with lock:
            counter += 1
        # Lock automatically released here

# Create 10 threads running the same function
threads = [
    threading.Thread(target=increment)
    for _ in range(10)
]

# Start all threads
for t in threads:
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()

# After all threads complete, counter is consistent
print(f"final counter : {counter}")
