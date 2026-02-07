#daemon and non daemon

import threading
import time

def monitiorTeaTeamp():
    while True:
        print(f"Monitoring tea tempearture")
        timep.sleep(2)

t=threading.Thread(target=monitiorTeaTeamp,daemon=True)
t.start()

print("main program done")