def twoSumBruteForce(nums: list[int], target: int) -> list[int]:
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return list((i, j))


# T.C -> O(n), S.C -> O(n)
def twoSumUsingHashMap(nums: list[int], target: int) -> list[int]:
    valueToIndex = {}
    n = len(nums)
    for index in range(n):
        if (target - nums[index]) in valueToIndex:
            return list((valueToIndex[target - nums[index]], index))

        valueToIndex[nums[index]] = index


print(twoSumUsingHashMap([2, 7, 11, 15], 9))
