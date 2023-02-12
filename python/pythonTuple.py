
# Tuple is ordered, unchangeable,duplicates allowed -> only for reading values
# some set of values u need in code, and dont want anyone to change it

tuple1 = ("abc","tub","icr","opo")
# print(tuple1.count())

# single element in tuple is considered to be of type int, str, float etc.
tuple2 = (6)
print(tuple2)
print(type(tuple2))

tuple3 = (5,)
print(tuple3)
print(type(tuple3))

# slicing same in tuple as list
# same membership operator

# to modify elements of tuple, convert it into list
list1 = list(tuple1)
list1.append("appended")
print(tuple1)
print(list1)
