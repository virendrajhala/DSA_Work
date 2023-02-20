from collections import Counter


def areAnagrams(s: str, p: str) -> bool:
    return Counter(s) == Counter(p)


# T.C -> O((m-n+1)*(n+n+n+1)), S.C -> O((m-n+1)*n)
def stringAnagrams(s: str, p: str) -> list[int]:
    m, n = len(s), len(p)
    res = []
    if n > m:
        return res
    for i in range(m - n + 1):
        substring = s[i:i + n]
        if areAnagrams(substring, p):
            res.append(i)

    return res


for s, p in [
    ("abab", "ab"),
    ("cabferacberdfd", "abc"),
    ("gafdgfdgerg", "fgd")
]:
    print(stringAnagrams(s, p))
