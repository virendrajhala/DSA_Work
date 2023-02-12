from copy import deepcopy

l1 = [1, 2, [3, 4, 5], 6, 7]
l2 = l1.copy()
# above is shallow copy
print(id(l1))  # id will give physical address of the object
print(id(l2))

# below lines will give same input as both 2nd indexes
print(id(l1[2]))
print(id(l2[2]))

x = int(4)
y = x

y += 1
print(id(x))
print(id(y))

l3 = [1, 2, [3, 4, 2], 9, 8]
l4 = deepcopy(l3)

print(id(l3)[2])
print(id(l4[2]))

