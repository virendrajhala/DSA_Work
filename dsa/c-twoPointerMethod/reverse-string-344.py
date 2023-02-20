
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
def reverseString(s: list[str]):
    print(s)
    n = len(s)
    low = 0
    high = n - 1
    while low < high:
        # python internally handles swapping logic
        s[low], s[high] = s[high], s[low]
        # swap(nums, low, high)
        low += 1
        high -= 1
    print(s)


for lst in [
    ["h", "e", "l", "l", "o"],
    ["g", "l", "o", "b", "e"]
]:
    reverseString(lst)
