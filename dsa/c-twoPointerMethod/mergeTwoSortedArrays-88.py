# T.C -> O(m+n), S.C -> O(m+n)
def mergeTwoSortedArrays88LeetCode(nums1: list[int], m: int, nums2: list[int], n: int) -> list[int]:
    nums3 = nums1[:m]
    i = j = k = 0
    while i < m and j < n:
        if nums3[i] < nums2[j]:
            nums1[k] = nums3[i]
            i += 1

        else:
            nums1[k] = nums2[j]
            j = j + 1

        k += 1

    while j < n:
        nums1[k] = nums2[j]
        k, j = k + 1, j + 1

    while i < m:
        nums1[k] = nums3[i]
        k, i = k + 1, i + 1


# T.C -> O(m + n), S.C -> O(m + n)

def mergeTwoSortedArrays(nums1: list[int], nums2: list[int]) -> list[int]:
    m = len(nums1)
    n = len(nums2)
    nums3 = []
    i = j = 0
    while i < m and j < n:
        if nums1[i] < nums2[j]:
            nums3.append(nums1[i])
            i += 1
        else:
            nums3.append(nums2[j])
            j += 1

    while i < m:
        nums3.append(nums1[i])
        i += 1
    while j < n:
        nums3.append(nums2[j])
        j += 1

    return nums3


# for nums1, nums2 in [
#     ([1], [0]),
#     ([12, 32, 45, 54, 65, 76, 90], [1, 2, 3, 7, 8, 10])
# ]:
#     print(mergeTwoSortedArrays(nums1, nums2))

for nums1, nums2 in [
    ([12, 32, 45, 54, 65, 76, 90, 0, 0, 0, 0, 0, 0], [1, 2, 3, 7, 8, 10])
]:
    mergeTwoSortedArrays88LeetCode(nums1, 7, nums2, 6)
    print(nums1)
