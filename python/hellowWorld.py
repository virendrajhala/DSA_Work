print("Hello World")
if 10 > 5:
    print("inside if")
    print("still inside if")

print("now, outside if")

if 67 < 89:
    pass
    print("inside if")

a = 44444444444444444444478877899999999999999999999999999999999994444444444444444444444444444444444444444488888888888888888888888888888888888888
b = 66666666666666666666666666666666666666622222222222222222222222222222222222222200000000000000000000000000000000001111111111111111111111111111
print(type(a * b))

a, b = "fret", "poll"
print(a, b, sep="lod", end=" stopit\n")

"""
There is no data type as Char in python, there are only Strings, (str)
String in python is an array of single character but as there is no char data type, so 
s = "python"
type(s[0]) -> str, so single element of string is also string
"""

s = "python"
print(type(s[0]))

s1 = s
print(s1)
s1 = s1 + "abc"
output = "s1 : {}, s2: {}"
print(output.format(s1, s))

# Slicing the string ***************
exampleString = "I love problem solving"
#  s[i:j] -> includes i index char and excludes j index char, -> [i,j)
print(exampleString[2:2])
print(exampleString[2:8])
print(exampleString[2:])
print(exampleString[:10])
# slice operation does not take into consideration the out of index thing, it will print upto the last character
# if value exceeds the length of the string
print(exampleString[4:78767878887])
print(exampleString[:])

# one way of Copying a string into other variable
anotherString = exampleString[:]
print("copied string:",anotherString)

# length of string
print(len(anotherString))

#  below line will give error, str does not support item assignment
# anotherString[0] = "e"
# print(anotherString)