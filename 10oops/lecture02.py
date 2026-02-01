# #?-------------------inheritance -------------------
# class Parent:
#     pass

# class Child(Parent):
#     pass


#? -------------------example-------------------
class animal:
    def eat(self):

        print("animal is eating")

class dog(animal):
    def eat(self):
        super().eat()
        print("dog is barking")

d=dog()
d.eat()
