# asyncio with multiprocessing (ProcessPoolExecutor) example
# Ye code dikhata hai kaise asyncio ke sath CPU-bound task
# ko multiple processes me run kar sakte hain

import asyncio
from concurrent.futures import ProcessPoolExecutor

def encrypt(data):
    """
    Ye normal (blocking) function hai.
    Isme hum data ko reverse karke ek fake encryption kar rahe hain.
    CPU-bound ka example samajhne ke liye.
    """
    return f"🔒 {data[::-1]}"

async def main():
    """
    Ye async main function hai.
    Iske andar hum event loop lete hain aur
    ProcessPoolExecutor ka use karke function ko
    alag process me run karte hain.
    """

    # Current running event loop ko get kar rahe hain
    loop = asyncio.get_running_loop()

    # ProcessPoolExecutor:
    # - CPU intensive tasks ke liye best hota hai
    # - Har task alag process me chalta hai
    with ProcessPoolExecutor() as pool:

        # run_in_executor:
        # - Blocking function (encrypt) ko async tarike se run karta hai
        # - Yaha encrypt function ek alag process me execute hoga
        result = await loop.run_in_executor(
            pool,              # process pool
            encrypt,           # function jo run karna hai
            "credit_card_1234" # function argument
        )

        # Jab process complete ho jata hai,
        # tab result yaha mil jata hai
        print(result)

if __name__ == "__main__":
    """
    Ye check zaroori hai jab hum multiprocessing use karte hain,
    warna Windows par infinite process spawn ho sakta hai.
    """

    # asyncio event loop start kar rahe hain
    asyncio.run(main())
