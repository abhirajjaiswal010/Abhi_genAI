"""
===============================
ASYNC IO – FOUNDATION FILE
===============================

Core Definition:
----------------
Async IO (Asynchronous Input Output) ek programming technique hai
jisme program slow operations (I/O) ka wait nahi karta.

Jab koi kaam time leta hai (network, sleep, file, DB),
to program us waqt rukta nahi, balki dusra kaam karta hai.

Key Idea:
---------
"Don't wait. Resume when ready."
"""

# asyncio = Python ka async framework
# Ye event loop, tasks, coroutines sab manage karta hai
import asyncio


# --------------------------------------------------
# 1️⃣ ASYNC FUNCTION (Coroutine)
# --------------------------------------------------
"""
async def = coroutine function

- Ye function turant execute nahi hota
- Ye ek coroutine object return karta hai
- Iske andar await use kar sakte ho
"""

async def hello():
    print("Hello")

    # await = non-blocking wait
    # asyncio.sleep() CPU ko block nahi karta
    # Event loop ko bolta hai: "2 sec baad mujhe resume karna"
    await asyncio.sleep(2)

    print("World")


# --------------------------------------------------
# 2️⃣ EVENT LOOP START – asyncio.run()
# --------------------------------------------------
"""
asyncio.run():
- Event loop create karta hai
- Coroutine ko run karta hai
- Kaam khatam hone par loop close karta hai

Rule:
-----
Top-level pe sirf asyncio.run() hota hai
"""

asyncio.run(hello())


print("*" * 30)


# --------------------------------------------------
# 3️⃣ MULTIPLE ASYNC TASKS
# --------------------------------------------------
"""
Ab hum multiple async tasks banayenge
Ye concurrent chalenge (parallel nahi)
"""

async def task1():
    await asyncio.sleep(2)
    print("Task 1 completed")

async def task2():
    await asyncio.sleep(2)
    print("Task 2 completed")


# --------------------------------------------------
# 4️⃣ asyncio.gather()
# --------------------------------------------------
"""
asyncio.gather():
- Multiple coroutines ko ek saath schedule karta hai
- Sab complete hone ka wait karta hai
- Concurrency achieve karta hai

Note:
-----
Ye threads create nahi karta
Sab ek hi thread mein hota hai
"""

async def main():
    await asyncio.gather(
        task1(),
        task2()
    )


asyncio.run(main())


# --------------------------------------------------
# 5️⃣ IMPORTANT ASYNC METHODS (REFERENCE)
# --------------------------------------------------

"""
🔹 asyncio.sleep(seconds)
- Non-blocking delay
- time.sleep() ka async version

🔹 asyncio.gather(coro1, coro2)
- Multiple coroutines ko saath run karta hai

🔹 asyncio.create_task(coro)
- Coroutine ko background task banata hai
- Fire-and-forget style

🔹 await
- Coroutine ke completion ka non-blocking wait

🔹 Event Loop
- Async system ka brain
- Decide karta hai kaunsa task kab chale

🔹 Coroutine
- async def se bana function
- await ke bina async incomplete hai
"""

# --------------------------------------------------
# 6️⃣ GOLDEN RULES (LIFE TIME MEMORY)
# --------------------------------------------------
"""
❌ async CPU heavy kaam ke liye nahi
✅ async I/O heavy kaam ke liye best

❌ time.sleep() async code mein mat use karo
✅ asyncio.sleep() use karo

❌ async bina await bekaar hai
✅ await hi async ko powerful banata hai

Mental Model:
-------------
Async = Smart waiting
Thread = Parallel worker
Process = Heavy isolation
"""
