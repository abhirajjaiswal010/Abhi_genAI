# Empty list
l1 = []

# List with values
l2 = [10, 20, 30]

# Mixed types
l3 = [1, "Python", 3.14, True]

# Nested list
l4 = [1, [2, 3], [4, 5, 6]]

print(l1)
print(l2)
print(l3)
print(l4)
print("-------------------------------------------")
lst = [1, 2, 3]
 
lst[0] = 100
print(lst)  # [100, 2, 3]

# Append element
lst.append(4)
print(lst)  # [100, 2, 3, 4]

# Insert at index
lst.insert(1, 50)
print(lst)  # [100, 50, 2, 3, 4]

# Remove element
lst.remove(2)
print(lst)  # [100, 50, 3, 4]

# Pop element (by index)
p = lst.pop()
print(p, lst)  # 4 [100, 50, 3]
