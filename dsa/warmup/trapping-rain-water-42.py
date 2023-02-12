# https://leetcode.com/problems/trapping-rain-water/

# T.C -> O(n^2), S.C -> O(n^2) Brute force approach
def trap1(height: list[int]) -> int:
    widthOfBar = 1
    """ waterTrapped on each bar = (min(max height of bar on left, max height of bar on right) - bar height) * bar width 
        result = sum(water trapped on each bar)
    """
    result = 0
    for index in range(len(height)):
        maxOnLeft = max(height[:index + 1])
        maxOnRight = max(height[index:])
        waterTrappedOnCurrentBar = (min(maxOnLeft, maxOnRight) - height[index]) * widthOfBar
        result += waterTrappedOnCurrentBar

    return result


# Better approach, T.C -> O(n), S.C -> O(n), pre computation of leftMax and rightMax arrays
def trap(bars: list[int]) -> int:
    result = 0
    n = len(bars)
    leftMax = [0] * n
    leftMax[0] = bars[0]
    for i in range(1, n):
        leftMax[i] = max(leftMax[i - 1], bars[i])

    rightMax = [0] * n
    rightMax[-1] = bars[-1]
    for i in range(n - 2, -1, -1):
        rightMax[i] = max(rightMax[i + 1], bars[i])

    for i in range(1, n):
        trappedWaterOnCurrentBar = min(leftMax[i], rightMax[i]) - bars[i]
        result += trappedWaterOnCurrentBar

    return result


for height in [
    [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
]:
    print(trap1(height))

# 10^4, 10^5 -> O(n)
# 1000 -> O(n log n)
# 100 -> O(n^2)
