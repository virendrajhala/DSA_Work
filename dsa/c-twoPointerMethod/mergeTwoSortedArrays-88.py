# T.C -> O(m+n), S.C -> O(m+n)
def mergeTwoSortedArrays88LeetCode(nums1: list[int], nums2: list[int]) -> list[int]:
    m = len(nums1)
    n = len(nums2)
    nums3 = []
    i, j = 0, 0
    while i < m or j < n:
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


# T.C -> O(m + n), S.C -> O(m + n)

def mergeTwoSortedArrays(nums1: list[int], nums2: list[int]) -> list[int]:
    m = len(nums1) - 1
    n = len(nums2) - 1
    nums3 = []
    i = j = 0
    while i < m or j < n:
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


for nums1, nums2 in [
    ([1], [0]),
    ([76, 65, 54, 90, 32, 45, 12], [10, 2, 3, 7, 1, 8])
]:
    print(mergeTwoSortedArrays(nums1, nums2))

# for nums1, nums2 in [
#     ([1], [0]),
#     ([76, 65, 54, 90, 32, 45, 12, 0, 0, 0, 0, 0, 0], [10, 2, 3, 7, 1, 8])
# ]:
#     mergeTwoSortedArrays88LeetCode(nums1, nums2)
