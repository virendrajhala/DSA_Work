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
            reversedString = reverse(sCopy, k)
            outputString += reversedString
        return outputString


testData = [
    # "ab",
    # "abc",
    # "abcde",
    # "abcdef",
    # "abcdefg",
    # "abcdefgh",
    # "abcdefghi",
    # "abcdefghij",
    # "abcdefghijk",
    "hyzqyljrnigxvdtneasepfahmtyhlohwxmkqcdfehybknvdmfrfvtbsovjbdhevlfxpdaovjgunjqlimjkfnqcqnajmebeddqsgl"
]
kValue = 39

for string in testData:
    print(reverseStr(string, kValue))

# st = "fdcqkmxwholhytmhafpesaentdvxginrjlyqzyhehybknvdmfrfvtbsovjbdhevlfxpdaovjgunjqlimjkfnqcqnajmebeddqsgl"  -> Leetcode output
# print(len(st))

# fdcqkmxwholhytmhafpesaentdvxginrjlyqzyhehybknvdmfrfvtbsovjbdhevlfxpdaovjgunjqllgsqddebemjanqcqnfkjmi -> my output
