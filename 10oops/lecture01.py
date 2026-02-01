# #? class and object in python

# * class in python
# A class is a blueprint to create objects.
# It groups data (variables) and behavior (methods/functions) together.

# ? -------------------syntax---------------------------
# class ClassName:
#     def __init__(self, parameters):
#         self.variable = parameters  # instance variable
#     def method_name(self):
#         print("This is a method")

# ? ---------------------------example---------------------------

# student class example (commented for reference)
# class student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def introduce(self):
#         print(f"my name is {self.name} and i am {self.age} years old")
# s1 = student("abhi", 21)
# s1.introduce()


# ? ------------------- class and object namespace -------------------

class chai:
    origin = "India"   # class attribute (shared by all objects)


# accessing class attribute via class
# print(chai.origin)

chai.is_hot = True     # adding attribute at class level

# print(chai.is_hot)


# ? -------------------creating object from class chai-------------------

masala = chai()        # object creation

# object accessing class attributes
# print(f"masala - {masala.origin}")
# print(f"masala - {masala.is_hot}")

masala.is_hot = False  # instance attribute shadows class attribute

# print("class : ", chai.is_hot)
# print(f"masala {masala.is_hot}")

masala.flavor = "ginger"  # object-specific attribute


# conclusion:
# every object has its own namespace
# object-level changes do not affect other objects or the class


# ? -------------------Attribute shadowing-------------------

class chai1:
    temperature = "hot"     # class attribute
    strength = "strong"     # class attribute


cutting = chai1()          # object creation

# print(cutting.temperature)

cutting.temperature = "mild"  # instance attribute shadows class attribute
cutting.cup = "small"         # new attribute only for this object

# print("after changing ", cutting.temperature)
# print("cup  size is ", cutting.cup)
# print("dirct look into the class", chai1.temperature)

del cutting.temperature   # removes instance attribute
del cutting.cup           # deletes object-only attribute

# print(cutting.temperature)  # class attribute visible again
# print(cutting.cup)          # error: attribute no longer exists


# ? -------------------self argument -------------------

class chaicup:
    size = 150  # class attribute (ml)

    def describe(self):
        # self refers to the calling object
        return f"A {self.size}ml chai cup"
    

cup = chaicup()
# print(cup.describe())   # uses class attribute size

cup2 = chaicup()
cup2.size = 300         # instance attribute shadows class attribute
# print(cup2.describe())

# runtime error example:
# methods automatically receive self
# passing extra argument causes TypeError
# print(cup2.describe(cup_two))



