# #?------------------- inheritance -------------------
# Inheritance allows a child class to reuse properties and methods of parent class

# class Parent:
#     pass

# class Child(Parent):
#     pass


# ? -------------------example-------------------

class animal:
    # parent class method
    def eat(self):
        print("animal is eating")


class dog(animal):
    # child class overriding parent method
    def eat(self):
        super().eat()              # calls parent (animal) eat()
        print("dog is barking")    # additional behavior


# object of child class
d = dog()
d.eat()

# print(dog.mro())   # shows Method Resolution Order


# ? -------------------way to access base class-------------------
# This section shows different ways to call parent constructor

class chai:
    # base class constructor
    def __init__(self, type_, strength):
        self.type = type_          # chai type
        self.strength = strength  # chai strength


#*NOT recommended:
# direct re-writing parent attributes (code duplication)
# class gingerChai(chai):
#     def __init__(self, type_, strength, spiceLvl):
#         self.type = type_
#         self.strength = strength
#         self.spiceLvl = spiceLvl


#* Works but less preferred:
# explicit parent class call
# class GingerChai(chai):
#     def __init__(self, type_, strength, spiceLvl):
#         chai.__init__(self, type_, strength)
#         self.spiceLvl = spiceLvl


#* BEST PRACTICE:
# using super() to call base class constructor
class gingerChai(chai):
    def __init__(self, type_, strength, spiceLvl):
        super().__init__(type_, strength)  # initializes parent attributes
        self.spiceLvl = spiceLvl           # child-specific attribute
