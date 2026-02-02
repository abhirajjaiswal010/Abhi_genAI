# ───────────────────────── try / except ─────────────────────────
# The try block contains code that may raise an exception.
# If an error occurs, Python immediately jumps to the matching
# except block instead of crashing the program.
#
# This allows graceful error handling and keeps the program running.
# ────────────────────────────────────────────────────────────────


# try: run code
# except: handle error
# else: run if no error
# finally: always run


chaiMenu = {"masala": 30, "ginger": 40}

try:
    chaiMenu["elaichi"]
except KeyError:
    print("the key that you are try to access does not exists")


def serveChai(flavor):
    try:
        print(f"preparing {flavor} chai...")
        if flavor == "unknown":
            raise ValueError("we dont know that flavor")
    except ValueError as e:
        print("error : ", e)
    else:
        print(f"{flavor} chai is served")
    finally:
        print("Next customer please")
        


serveChai("masala")
serveChai("unknown")
