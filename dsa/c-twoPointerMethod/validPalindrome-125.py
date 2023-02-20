def isValidPalindrome(s: str) -> bool:
    # s = s.lower()      -> T.C -> O(n)
    low, high = 0, len(s) - 1
    while low < high:
        if s[low] != s[high]:
            return False
        low += 1
        high -= 1

    return True


def isValidPalindromeOptimal(s: str) -> bool:
    low, high = 0, len(s) - 1
    while low < high:
        # logic to ignore alphanumeric characters
        if not s[low].isalnum():
            low += 1
            continue
        if not s[high].isalnum():
            high -= 1
            continue
        # below line will compare the characters
        if s[low].lower() != s[high].lower():
            return False
        # else increment/decrement the two
        low, high = low + 1, high - 1

    return True


for string in [
    "madam",
    ".,.,,."
]:
    print(string, isValidPalindromeOptimal(string))
