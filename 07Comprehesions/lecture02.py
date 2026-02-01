#set comprehension

fav_chai=["masala chai","green tea","masala chai","lemon tea","green tea","elaichi chai"]

unique_chai={chai for chai in fav_chai}
print(unique_chai) 

recipes={
    "masala chai":["ginger","cardom","clove"],
    "elaichi chai":["cardamom","milk"],
    "spicy chai":["ginger","black pepper","clove"],
}

unique_spices={spice for ingredients in recipes.values() for spice in ingredients}
print(unique_spices)