# program to reverse a number
# https://leetcode.com/problems/reverse-integer/
def reverseInteger(x: int) -> int:
    # to handle negative numbers, modulus operator behaves abnormally with negative numbers
    factor = -1 if x < 0 else 1
    integerRange = 2 ** 31
    x = abs(x)
    result = 0
    while x:  # T.C -> O(log n)( to base 10) loop will run no. of digit times
        lastDigit = x % 10
        x //= 10
        result = (10 * result) + lastDigit

    if result < -integerRange or result > integerRange:   # handle out of range case
        return 0
    return result * factor


for val in [12345566666643, 12342, -432, 0, 230]:
    print(reverseInteger(val))
