# below code takes Space complexity (S.C) -> O(n), T.C. -> O(n)
def reverseList(lst):
    n = len(lst)
    res = []
    for i in range(n - 1, -1, -1):
        res.append(lst[i])

    return res


print(reverseList([1, 2, 3, 4, 5, 6, 7, 8, 9]))

l = list((1, 2, 3))
print(l)
