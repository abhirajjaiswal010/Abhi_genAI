# chai="ginger chai"

# def prepare_chai(order):
#     print("preparing", order)

# prepare_chai(chai)
# print(chai)

# 

def make_chai(tea,milk,sugar):
    print(tea,milk,sugar)

make_chai("darjeeeling ","yes","low")
make_chai(tea="green",sugar="medium",milk="no")


def special_chai(*ingredients,**extras):
    print("ingredients" , ingredients)
    print("extras",extras)

special_chai("cinnamon","cardmom",sweetener="honey",foam="yes")

