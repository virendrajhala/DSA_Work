from collections import Counter


# T.C -> O(n logn [sorting] + n [comparing equality])
# S.C -> O(n), space taken for sorted strings
def validAnagram1(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)


def validAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    freq1 = Counter(s)  # T.C -> O(n) , S.C -> O(1) (because of only 26 alphabet characters)
    freq2 = Counter(t)  # T.C -> O(n) , S.C -> O(1)
    return freq1 == freq2  # equate to dictionaries, order does not matter, will be equal if all key-value pairs are equal in both


def validAnagram2(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    freq1 = Counter(s)  # T.C -> O(n) , S.C -> O(1) (because of only 26 alphabet characters)
    freq2 = Counter(t)  # T.C -> O(n) , S.C -> O(1)
    for key in freq1:
        if key not in freq2 and freq1[key] != freq2[key]:
            return False

    return True


for s, t in [
    ("anagram", "naagram"),
    ("rat", "car")
]:
    print(s, validAnagram2(s, t))
