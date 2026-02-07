import asyncio
import aiohttp

# --------------------------------------------------
# ASYNC FUNCTION: FETCH URL
# --------------------------------------------------
"""
fetch_url():
- Ye ek coroutine hai (async def)
- Network I/O karta hai (HTTP request)
- aiohttp NON-BLOCKING library hai
"""

async def fetch_url(session, url):

    # async with:
    # ----------
    # Context manager ka async version
    # - Request open karta hai
    # - Response close karta hai automatically
    # - Event loop block nahi hota

    async with session.get(url) as response:

        # response.status = HTTP status code (200, 404, etc.)
        print(f"fetched {url} with status {response.status}")


# --------------------------------------------------
# MAIN COROUTINE
# --------------------------------------------------
async def main():

    # Same URL 3 times
    # httpbin.org/delay/2
    # -> Server 2 seconds delay karta hai response dene mein
    urls = ["https://httpbin.org/delay/2"] * 3

    # ClientSession:
    # --------------
    # - HTTP connection pooling
    # - Reuse connections
    # - async context manager
    async with aiohttp.ClientSession() as session:

        # Tasks list:
        # -----------
        # Yahan coroutines create ho rahi hain
        # Execute tab hoti hain jab await hota hai
        tasks = [fetch_url(session, url) for url in urls]

        # asyncio.gather():
        # -----------------
        # - Sab coroutines ko ek saath schedule karta hai
        # - Event loop smartly switch karta hai
        # - Sab complete hone ka wait karta hai
        await asyncio.gather(*tasks)


# --------------------------------------------------
# EVENT LOOP START
# --------------------------------------------------
asyncio.run(main())


# --------------------------------------------------
# EXPLANATION: await asyncio.gather(*tasks)
# --------------------------------------------------
"""
await asyncio.gather(*tasks):

WHAT IT DOES:
-------------
1. tasks → list of coroutines (async functions not yet executed)
2. *tasks → list ko unpack karke individual arguments banata hai
3. asyncio.gather():
   - Sab coroutines ko event loop mein schedule karta hai
   - Unhe CONCURRENTLY run karta hai (parallel nahi)
4. await:
   - Jab tak sab coroutines complete na ho jaaye
   - Tab tak current coroutine ko pause karta hai (NON-BLOCKING)

IMPORTANT:
----------
- Ye line EVENT LOOP ko block nahi karti
- Ye THREADS create nahi karti
- Ye tabhi effective hai jab andar ka code NON-BLOCKING ho

TIME BEHAVIOR:
--------------
- Sequential await → total time = sum of all tasks
- asyncio.gather → total time = max time of one task

MENTAL MODEL:
-------------
gather = "run together"
await  = "wait smartly"

INTERVIEW ONE-LINER:
-------------------
asyncio.gather runs multiple coroutines concurrently and waits
for all of them to finish without blocking the event loop.
"""
