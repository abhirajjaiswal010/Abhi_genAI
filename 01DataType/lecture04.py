#tuple
# 🟢 Tuple Operations Example

# 1️⃣ Creating Tuples
t1 = (1, 2, 3)
t2 = ('a', 'b', 'c')
t3 = 4, 5, 6 ,"abhi"      # packing without parentheses
print("t1:", t1)
print("t2:", t2)
print("t3:", t3)

# 2️⃣ Indexing
print("\nIndexing:")
print("t1[0]:", t1[0])
print("t2[-1]:", t2[-1])

# 3️⃣ Slicing
print("\nSlicing:")
print("t1[1:3]:", t1[1:3])
print("t2[:2]:", t2[:2])
print("t3[::-1] (reverse):", t3[::-1])

# 4️⃣ Tuple Concatenation
t4 = t1 + t3
print("\nConcatenation (t1 + t3):", t4)

# 5️⃣ Tuple Repetition
t5 = t2 * 2
print("\nRepetition (t2*2):", t5)

# 6️⃣ Membership Testing
print("\nMembership:")
print("2 in t1:", 2 in t1)
print("'x' not in t2:", 'x' not in t2)

# 7️⃣ Tuple Unpacking
a, b, c = t1
print("\nUnpacking t1:", a, b, c)

# Extended unpacking
nums = (10, 20, 30, 40, 50)
x, *y, z = nums
print("Extended unpacking:", "x =", x, "y =", y, "z =", z)

# 8️⃣ Iteration
print("\nIteration over t2:")
for item in t2:
    print(item, end=" ")
print()

# 9️⃣ Tuple Methods (immutable - only count & index)
t6 = (1, 2, 2, 3)
print("\nTuple Methods:")
print("t6.count(2):", t6.count(2))
print("t6.index(3):", t6.index(3))

# 10️⃣ Immutability Test
print("\nImmutability Test:")
try:
    t1[0] = 100
except TypeError as e:
    print("Error:", e)


