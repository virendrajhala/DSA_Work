def rotate(matrix: list[list[int]]) -> None:
    n = len(matrix)

    for i in range(n - 1):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # T.C -> O(n^2), S.C -> O(1)
    #         +
    # T.C -> O(n * n/2)
    for row in matrix:
        low, high = 0, len(row) - 1
        while low < high:
            row[low], row[high] = row[high], row[low]
            low, high = low + 1, high - 1


cube = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotate(cube)
print(cube)
