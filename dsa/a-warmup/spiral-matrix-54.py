# https://leetcode.com/problems/spiral-matrix/
def spiralOrder(matrix: list[list[int]]) -> list[int]:
    res = []
    row, col = len(matrix), len(matrix[0])
    rMin = cMin = 0
    rMax, cMax = row - 1, col - 1

    while rMin <= rMax and cMin <= cMax:
        # -> movement (left to right), col value will change, row value will be constant = rMin = 0
        for colIndex in range(cMin, cMax + 1):
            res.append(matrix[rMin][colIndex])

        # increment rMin for next bottom for loop movement so that last top right corner element does not repeat
        rMin += 1

        #  movement (top to bottom), col will be cMax and constant while rows will change from top to bottom
        for rowIndex in range(rMin, rMax + 1):
            res.append(matrix[rowIndex][cMax])

        # decrement cMax for next bottom for loop movement so that last bottom right corner element does not repeat
        cMax -= 1

        #  movement (right to left), row will be rMax and constant while column will change from right to left
        for colIndex in range(cMax, cMin - 1, -1):
            res.append(matrix[rMax][colIndex])

        # decrement rMax for next bottom for loop movement so that last bottom left corner element does not repeat
        rMax -= 1

        # movement (bottom to top), rows will change for bottom to top movement while column will remain constant as cMin
        for rowIndex in range(rMax, rMin - 1, -1):
            res.append(matrix[rowIndex][cMin])

        # decrement rMax for next bottom for loop movement so that last bottom left corner element does not repeat
        cMin += 1

    return res


# T.C -> O(m * n), for traversing a 2D matrix
inputMatrix = [
    [1, 4, 5, 6, 7],
    [6, 2, 7, 4, 1],
    [2, 7, 9, 8, 4],
    [9, 2, 5, 7, 2],
    [5, 4, 1, 2, 3]
]

print(spiralOrder(inputMatrix))
