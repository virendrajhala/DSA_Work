
from collections import defaultdict

a = {
    "class": "dsa",
    "topic": "dict",
    "purpose": "problem solving",
    "name": "virendra",
    "name" : "harshit",
    "students" : ["a","b","c"],
    # unhashable type list key not allowed below
    # [1,3,5,8] : 1,
    # below is also unhashable type
    # {"a":"c"} : 9,
    2 : 5
}
b = {}
c = dict()
# dict is unordered, changeable, no duplicate keys
print(a)
print(len(a))
print(type(a))
print(type(b),type(c))
# read -> value = dict[ley]
print(a["name"])
# error below as key 5 is not present
# print(a[5])
a["name"] = "viru"
print(a)

# differencr between a[key] and a.get(key)
#  a[key] will give key error while a.get(key) will return None if key not present

# print(a[5])
c = a.get(5)
d = a.get(5)
print(c,d)

keys = a.keys()
print(keys)

# .get()
# defaultdict()
# .get(key,defaultValue)
# Counters
myDict = {
    "name" : "viru",
    "number" : "6354728393",
    "id" : "100089"
}

# below line throws error, KeyError, as no key is present
# print(myDict["employeeCode"])

print(myDict.get("employeeCode"))
print(myDict.get("employeeCode","defaultEmployeeCodeValue"))
print(myDict.setdefault("employeeCode","DefaultEmpCode"))

# very important ************
default = defaultdict(str)
default["_id"] = "37665687866"
default["name"] = "Virendra"
default["number"] = "6789456778"
print(default)
print(default["unknownKey"])

string1 = "viru"
string2 = "Viru"

print(string1 == string2)



