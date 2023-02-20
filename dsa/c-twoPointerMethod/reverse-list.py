# using library function
def main(num1: list[int]):
    # S.C -> O(n), T.C. -> O(n), returns new list
    print(reverseList(num1))

    # T.C -> O(n), S.C. -> O(1)
    num1.reverse()
    print(num1)


main([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


# Brute force, T.C. -> O(n), S.C -> O(n), input not modified
def reverseList(nums: list[int]):
    print(nums)
    n = len(nums)
    output = [0] * n
    outputIndex = 0
    for index in range(n - 1, -1, -1):
        output[outputIndex] = nums[index]
        outputIndex += 1
    print(output)


# without using extra temp variable
def swap(nums, index1, index2):
    nums[index1] = nums[index1] + nums[index2]
    nums[index2] = nums[index1] - nums[index2]
    nums[index1] = nums[index1] - nums[index2]


# using extra temp variable
def swap1(nums, index1, index2):
    temp = nums[index1]
    nums[index1] = nums[index2]
    nums[index2] = temp


# in place modification, input can be changed, T.C -> O(n/2), S.C -> O(1), Constant space
def reverse(nums: list[int]):
    print(nums)
    n = len(nums)
    low = 0
    high = n - 1
    while low < high:
        # python internally handles swapping logic
        nums[low], nums[high] = nums[high], nums[low]
        # swap(nums, low, high)
        low += 1
        high -= 1
    print(nums)


for lst in [
    [1, 2, 3, 4, 5],
    [5, 4, 6, 1, 2, 9]
]:
    reverseList(lst)
    reverse(lst)
