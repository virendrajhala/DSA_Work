# count of words = w
# length of each word = l
# T.C -> O(w*(l)) -> O(n)
def reverseString(string: list[str], low, high):
    while low < high:
        # swap the low and high characters
        string[low], string[high] = string[high], string[low]
        low += 1
        high -= 1


# def reverseWords(string: str) -> str:
#     words = string.split(" ")
#     for word in words:
#         reverseString(list(word))
#
#     return " ".join(words)

def reverseWordsWithoutSplit(s: str) -> str:
    n = len(s)
    s = list(s)
    start = 0
    for end in range(n):
        if end == n or s[end] == " ":  # end == n condition for last word
            reverseString(s, start, end - 1)
            start += 1
    # can also include reverseString(s,start,n-1) for last words
    return "".join(s)


for string in [
    "Let\'s have fun tonight"
]:
    print(reverseWordsWithoutSplit(string))
