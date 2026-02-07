# Daemon vs Non-Daemon Thread example (Non-Daemon case)
# Ye code dikhata hai default thread behavior (daemon=False)

import threading
import time

def monitorTeaTemp():
    """
    Ye function tea ka temperature monitor karta rahega.
    Kyunki ye infinite loop me hai aur thread non-daemon hai,
    isliye program tab tak band nahi hoga jab tak ye thread chal raha hai.
    """
    while True:
        print("Monitoring tea temperature")
        time.sleep(2)  # 2 second ka delay

# Thread create kar rahe hain
# By default daemon=False hota hai
t = threading.Thread(
    target=monitorTeaTemp
)

# Thread start kar rahe hain
t.start()

# Main thread ka kaam
print("Main program done")

# IMPORTANT:
# - Yaha program exit nahi karega
# - Ye line print hone ke baad bhi
#   background thread chalta rahega
