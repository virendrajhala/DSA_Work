# python lists are  ordered, changeable, can have duplicate members
from collections import deque

myList = ["ehg", "eut", "ker", "dsa", "abc", "learn", "solve"]
# it changes list itself, returns None
print(myList.sort())
print(myList)
# returns None
print(myList.sort(reverse=True))
print(myList)
#  returns None
print(myList.append(100))
print(myList)
# reverses a list
print(myList.reverse())
print(myList)

myList.append(200)
print(myList)

# concatenation
list = [67, 34, 34]
y = myList + list
print(y)

for x in list:
    print(x, end=" ")

print()

# unpacking list
first, second, third = [4, 6, 7]
print(first, second, third)

for first, second in [[4, 6], [7, 2], [9, 5]]:
    print(first, second)

listExample = [1,2,3]

# removes element from last by default
print(listExample.pop())

# below operation takes O(n) as rest elements need to be shifted right
print(listExample.pop(0))

#  Dequeue is implemented in LinkedList
dequeueList = deque([1,2,34,3])

# very lesser data movement
# below code takes O(1) complexity as it moves head to second position
print(dequeueList.popleft())
# same for below
print(dequeueList.appendleft(10))