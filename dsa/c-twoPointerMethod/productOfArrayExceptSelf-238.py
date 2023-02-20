# with division approach, edge case -> when all or atleast one element is zero
def productExceptSelf(nums: list[int]) -> list[int]:
    product = 1
    for num in nums:
        product *= num

    for index in range(0, len(nums)):
        if nums[index] == 0:
            continue
        nums[index] = product // nums[index]

    return nums


# T.C -> O(n^2)
def productExceptSelfBruteForce(nums: list[int]) -> list[int]:
    n = len(nums)
    leftProduct = 1
    res = []
    for i in range(n):
        rightProduct = 1
        for j in range(i + 1, n):
            rightProduct *= nums[j]
    res.append(leftProduct * rightProduct)
    leftProduct *= nums[i]


# T.C -> O(n + n + n) -> O(n), S.C -> O(n + n) -> O(n), res array space not counted as specified in the question
def productExceptSelfOptimal(nums: list[int]) -> list[int]:
    n = len(nums)
    lefProduct = [1] * n
    rightProduct = [1] * n
    res = []
    # pre computation of left product for each element
    for index in range(1, n):
        lefProduct[index] = lefProduct[index - 1] * nums[index - 1]

    for index in range(n - 2, -1, -1):
        rightProduct[index] = rightProduct[index + 1] * nums[index + 1]

    for index in range(n):
        res.append(lefProduct[index] * rightProduct[index])

    return res


# T.C -> O(n + n + n) -> O(n), S.C -> O(n + n) -> O(n), res array space not counted as specified in the question
def productExceptSelfOptimal(nums: list[int]) -> list[int]:
    n = len(nums)
    lefProduct = [1] * n
    rightProduct = [1] * n
    res = []
    # pre computation of left product for each element
    for index in range(1, n):
        lefProduct[index] = lefProduct[index - 1] * nums[index - 1]

    for index in range(n - 2, -1, -1):
        rightProduct[index] = rightProduct[index + 1] * nums[index + 1]

    for index in range(n):
        res.append(lefProduct[index] * rightProduct[index])

    return res


for a in [
    [1, 2, 3, 4],
    [-1, 1, 0, -3, 3],
    [4, 5, 1, 8, 2]
]:
    print(productExceptSelfOptimal(a))
