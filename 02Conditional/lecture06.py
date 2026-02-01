# You're building a ticket info system for a railway app.
# Based on seat type, show its features.

# Task:
# · Input:"sleeper""AC""general""Luxury"
# . Match using match-case
# · Unknown -> show:"Invalid seat type"



seat_type=input("Enter the seat tye (sleeper/AC/general/luxury) : ").lower()


match seat_type:
    case "sleeper":
        print("sleeper - No AC, beds available")
    case "ac":
        print("AC coach ")
    case "general":
        print("general coach")
    case "luxury":
        print("luxury coach")
    case _:
        print("invalid seat type")