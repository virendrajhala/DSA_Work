set1 = set()
print(type(set1))
set2 = {}
print(type(set2))

set3 = {34,65,23,34,34,34,76,21}
print(set3)

#  set union
set4 = {56,76,65}
print(set4 | set3)

# set intersection
print(set4 & set3)


# set can have only hashable values, unhashable values not allowed ********
# below will give error as list is unhashable
set1 = {[1,2],3,4}
print(set1)

#  tuples are hashable while lists are not hashable *************
set1 = {(3,4,5),"rtu"}
print(set1)