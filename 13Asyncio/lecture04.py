# ==================================================
# Handling Blocking Code in asyncio using ThreadPoolExecutor
# ==================================================
import asyncio
import time 
from concurrent.futures import ThreadPoolExecutor

# --------------------------------------------------
# SYNC / BLOCKING FUNCTION
# --------------------------------------------------
def checkStock(item):
    # Ye normal synchronous function hai
    # Isme time.sleep() use ho raha hai
    # time.sleep() BLOCKING hota hai
    # Isliye ise direct async function ke andar
    # call nahi kar sakte
    print(f"checking {item} in store...")

    time.sleep(3)   # ❌ BLOCKING (but yahan safe hai kyunki thread mein chalega)

    return f"{item} stock: 42"


# --------------------------------------------------
# ASYNC FUNCTION (EVENT LOOP KE ANDAR CHALTA HAI)
# --------------------------------------------------
async def main():

    # Current running event loop le rahe hain
    loop = asyncio.get_running_loop()

    # ThreadPoolExecutor:
    # -------------------
    # Ye threads ka pool banata hai
    # Blocking kaam ko in threads mein bheja jaata hai
    # Taaki event loop BLOCK na ho
    with ThreadPoolExecutor() as pool:

        # run_in_executor():
        # ------------------
        # checkStock() ko thread mein run karta hai
        # Event loop free rehta hai
        # await yahan NON-BLOCKING wait karta hai
        result = await loop.run_in_executor(
            pool,              # thread pool
            checkStock,        # blocking function
            "MASALA CHAI"      # argument
        )

        # Jab thread ka kaam complete ho jaata hai
        # result wapas async function ko mil jaata hai
        print(result)


# --------------------------------------------------
# PROGRAM START
# --------------------------------------------------
# asyncio.run():
# - Event loop start karta hai
# - main() coroutine ko run karta hai
# - Kaam khatam hone par loop close karta hai
asyncio.run(main())
