def reverse(s: str, k: int) -> str:
    return s[:k][::-1] + s[k:]


def reverseStr(s: str, k: int) -> str:
    n = len(s)
    if n < k:
        return reverse(s, len(s) - 1)
    elif k <= n < 2 * k:
        return reverse(s, k)
    else:
        outputString = ""
        for index in range(0, n, 2 * k):
            sCopy = s[index:index + 2 * k]
            sCopyLength = len(sCopy)
            if sCopyLength < k:
                outputString += reverse(sCopy, sCopyLength)
                break
        outputString += reverse(sCopy, k)
        return outputString


print(reverseStr("abcdefg", 2))
