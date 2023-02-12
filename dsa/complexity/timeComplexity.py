from datetime import datetime

# time complexity -> how the runtime scales with respect to the state of change of input
# the state of change of steps with respect to the input change

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 7]
# length of list -> n=10
for val in list:
    print(val, end=" ")


#  T.C above is -> length of list -> O(n)

def main(list):
    for val in [1, 2, 3, 4, 5]:
        print(val, end=" ")


# T.C -> constant -> O(1) of above main fun

# T.C of below main1 is O(n)
def main1(lst):
    start = datetime.now()
    for val in lst:
        print(val, end=" ")
    print()

    end = datetime.now()
    print("Execution time",(end - start).microseconds,"microseconds")

# applying input to main fun
for lst in [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [4543, 7568, 432, 24, 3434, 33, 53, 33],
    [64, 2, 4],
    [23],
    [57564, 545, 343]
]:
    main1(lst)

