def fun(a, b, c):
    print("In fun")
    print("No need to specify type for any argument, nor return type of function")
    return 10


print(fun(10, [1, 5, 2, 4], "arg1"))

# only one constructor --init() can be written, the last one would overwrite previously written --init()
class Student:
    # below is parameterized constructor
    # def __init__(self, id, name, number):
    #     self.id = id
    #     self.name = name
    #     self.number = number
    def __init__(self):
        self.id = 0
        self.name = "name"
        self.number = "77867"


# s1 = Student(id=867865, name="Virendra", number="7678787878888")
s2 = Student()
print(s2)


# print(id(s1))
# print(s1)

class TestPrivateCase:
    __privateVar = 9
    def __privateFun(self):
        print("Inside private fun of the class")


test = TestPrivateCase()

