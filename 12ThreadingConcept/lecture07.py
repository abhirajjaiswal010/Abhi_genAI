import threading
import time

def prepareChai(type_,wait_time):
    print(f"{type_} chai : brewing ....")
    time.sleep(wait_time)
    print(f"{type_} chai : Ready.")


t1=threading.Thread(target=prepareChai,args=("masala",2))
t2=threading.Thread(target=prepareChai,args=("ginger",3))

t1.start()
t2.start()
t1.join()
t2.join()
