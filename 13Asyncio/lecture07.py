# Daemon vs Non-Daemon Thread example
# Ye code samjhata hai daemon thread ka behavior

import threading
import time

def monitorTeaTemp():
    """
    Ye function background me tea ka temperature monitor karta rahega.
    Ye infinite loop hai, isliye normally ye kabhi khud se stop nahi hota.
    """
    while True:
        print("Monitoring tea temperature")
        time.sleep(2)  # 2 second ka delay

# Thread create kar rahe hain
# daemon=True ka matlab:
# - Ye background thread hai
# - Main program khatam hote hi ye thread automatically stop ho jayega
t = threading.Thread(
    target=monitorTeaTemp,
    daemon=True
)

# Thread start kar rahe hain
t.start()

# Main thread ka kaam
print("Main program done")

# Jaise hi main thread end hota hai,
# daemon thread bhi kill ho jata hai
