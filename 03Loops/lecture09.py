# using dictionaries instead of match case

users = [
    {"id": 1, "total": 100, "coupon": "P20"},
    {"id": 2, "total": 400, "coupon": "F21"},
    {"id": 3, "total": 600, "coupon": "E40"},
]

discounts = {
    "P20": (0.2, 0),
    "F21": (0.5, 0),
    "P50": (0, 10),
}
for user in users:
    percent, fixed = discounts.get(user["coupon"], (0, 0))
    discount = user["total"] * percent + fixed
    print(
        f"{user["id"]} paid {user["total"]} and got  discount for next visit of  rupees"
    )
