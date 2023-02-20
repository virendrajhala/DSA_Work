def rotateArray(arr, k):
    n = len(arr)
    k = k % n
    i, j = 0, n - k - 1
    reverseArray(arr, i, j)
    reverseArray(arr, n - k, n - 1)
    reverseArray(arr, i, n - 1)
    print(arr)


def reverseArray(arr, low, high):
    while low < high:
        arr[low], arr[high] = arr[high], arr[low]
        low += 1
        high -= 1


for tup in [
    ([100, -1, 0, -2, 7, 6, 9], 4),
    ([1], 3),
    ([3434, 675, 34, 25, 88, 66], 20),
    ([786, 34, 998], 1)
]:
    rotateArray(tup[0], tup[1])
