from multiprocessing import Process  # multiprocessing se Process import kar rahe hain (parallel kaam ke liye)
import time  # time module execution ka time measure karne ke liye


def CrunchNumber():
    """
    Ye function CPU-bound task ko represent karta hai.
    Heavy calculation (counting) karke multiprocessing ka effect dikhata hai.
    """
    print("started the count process....")

    count = 0  # counter initialize
    for _ in range(100_000_000):  # heavy loop → CPU intensive kaam
        count += 1               # har iteration me count increase

    print("ended the count process....")


# Ye check Windows ke liye IMPORTANT hai
# Isse ensure hota hai ki new process sirf yahin se start ho
if __name__ == "__main__":

    start = time.time()  # program ka start time record

    # Do alag-alag processes create ho rahe hain
    # Dono same function ko run karenge
    p1 = Process(target=CrunchNumber)
    p2 = Process(target=CrunchNumber)

    # Dono processes start ho jaate hain (parallel execution)
    p1.start()
    p2.start()

    # Main program wait karega jab tak p1 aur p2 complete na ho jaaye
    p1.join()
    p2.join()

    end = time.time()  # end time record

    # Total execution time print hota hai
    print(f"total time with multiprocessing is {end - start:.2f} seconds")
