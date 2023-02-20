from collections import Counter
from collections import defaultdict

list1 = [6, 7, 8, 1, 2, 3, 4, 5, 6, 7]
# valueToCount = Counter(list1)
# print(valueToCount)
#
# valueToFrequency = {}
# for value in list1:
#     if value in valueToFrequency:
#         valueToFrequency[value] = valueToFrequency[value] + 1
#     else:
#         valueToFrequency[value] = 1
#
# print(valueToFrequency)

# constructing a frequency map
defaultMap = defaultdict(int)
for val in list1:
    defaultMap[val] = defaultMap[val] + 1
print(defaultMap)


def bruteForce(s: str) -> int:
    n = len(s)
    for i in range(n - 1):
        isRepeated = False
        for j in range(i + 1, n):
            if s[i] == s[j]:
                isRepeated = True
                break

    if not isRepeated:
        return i
    else:
        return -1


print(bruteForce("aaaaabbbbbbb"))


# edge case "aabb" will be ignored by above code

# T.C -> O(n+n) ->[for making frequency map from counter]+ [for iterating over the string to check first unique character]
# S.C -> O(1)******** -> because no. of lower case alphabets are fixed to be 26 only, so there will be 26 keys always
#  only their count will keep on increasing
def firstNonRepeatingCharacterInString(s: str) -> int:
    n = len(s)
    charToFrequency = Counter(s)
    for index, char in enumerate(s):
        if charToFrequency[char] == 1:
            return index


print(firstNonRepeatingCharacterInString("leetcode"))
