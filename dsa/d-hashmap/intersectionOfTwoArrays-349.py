# T.C -> O(m*n), S.C -> O(1)
def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
    res = []
    for val1 in nums1:
        for val2 in nums2:
            if val1 == val2 and val1 not in res:
                res.append(val1)

    return res


def intersectionOptimal(nums1: list[int], nums2: list[int]) -> list[int]:
    nums1Copy = set(nums1)  # T.C -> O(m), S.C -> O(m)
    res = []
    for val in nums2:    # T.C -> O(n)
        if val in nums1Copy:   # T.C -> O(1)
            res.append(val)
            nums1Copy.remove(val)

    return res


print(intersectionOptimal([1, 5, 2, 7, 3, 5], [8, 2, 6, 1, 4, 5]))
