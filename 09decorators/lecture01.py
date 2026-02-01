from functools import wraps
def myDecorator(func):
    @wraps(func)
    def wrapper():
        print("before function runs")
        func()
        print("after function runs")
    return wrapper

@myDecorator
def greet():
    print("hello from decorators class from other planet")

greet()
print(greet.__name__)