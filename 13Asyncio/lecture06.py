# asyncio + threading example
# Ye code dikhata hai kaise background me ek thread
# continuously kaam karta rahe, aur asyncio async task
# ko non-blocking tarike se execute kare

import asyncio
import threading
import time

def backgroundWorker():
    """
    Ye function ek alag thread me chalega.
    Iska kaam background me system health log karna hai.
    Ye infinite loop me chal raha hai.
    """
    while True:
        time.sleep(1)  # 1 second ke liye thread ko sleep kar rahe hain
        print("logging the system health")

async def fetchOrder():
    """
    Ye ek async function hai.
    Ye kisi I/O operation (jaise API / DB call) ko simulate karta hai.
    """
    await asyncio.sleep(3)  # Non-blocking sleep (event loop free rehta hai)
    print("order fetched")

# Ek background thread start kar rahe hain
# daemon=True ka matlab:
# - Program exit hote hi ye thread automatically stop ho jayega
threading.Thread(
    target=backgroundWorker,
    daemon=True
).start()

# asyncio event loop start kar rahe hain
# Ye async function ko run karega
asyncio.run(fetchOrder())
