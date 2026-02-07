import asyncio
import time

# --------------------------------------------------
# ❌ MISTAKE EXAMPLE: BLOCKING CALL INSIDE ASYNC
# --------------------------------------------------

async def brew(name):
    print(f"brewing {name}.....")

    # ❌ MISTAKE:
    # time.sleep() BLOCKING function hai
    # Ye poore EVENT LOOP ko rok deta hai
    # Is waqt koi aur async task run nahi ho sakta
    #
    # Result:
    # - async def hone ke baad bhi
    # - function SYNC jaisa behave karta hai
    #
    # RULE BREAK:
    # "Async function ke andar blocking code allowed nahi"

    time.sleep(3)   # ❌ BLOCKS EVENT LOOP

    print(f"{name} is ready.....")


async def main():
    # asyncio.gather() multiple coroutines ko schedule karta hai
    # Lekin ye tabhi kaam karta hai
    # jab andar ke functions NON-BLOCKING ho
    await asyncio.gather(
        brew("MASALA chai"),
        brew("GREEN chai"),
    )


# Event loop start hota hai
asyncio.run(main())


# --------------------------------------------------
# 🧠 GOLDEN RULES (NEVER FORGET)
# --------------------------------------------------

"""
RULE 1️⃣:
-------
async def ke andar
BLOCKING function = ASYNC FAIL

RULE 2️⃣:
-------
time.sleep()  ❌  async code mein
asyncio.sleep() ✅ async code mein

RULE 3️⃣:
-------
async + blocking code
= sync behavior

RULE 4️⃣:
-------
asyncio.gather() parallel nahi banata
Ye sirf NON-BLOCKING coroutines ko coordinate karta hai

FINAL FORMULA:
--------------
async + await + non-blocking IO = real async
"""
