from functools import wraps

def requireAdmin(func):
    @wraps (func)
    def wrapper(user_role):
        if user_role != "admin":
            print("Access denied :admins only")
        else:
            return func(user_role)
    return wrapper

@requireAdmin
def accessTeaInvetory(role):
    print("access granted to tea inventory")

accessTeaInvetory("user")
accessTeaInvetory("admin")