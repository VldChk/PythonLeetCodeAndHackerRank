def rotate_bruteForce(matrix: list) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix)

    res = [x[:] for x in matrix]

    for i in range(n):
        for j in range(n):
            res[j][n - i - 1] = matrix[i][j]
    for i in range(n):
        for j in range(n):
            matrix[i][j] = res[i][j]


def rotate_smart(matrix: list) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix)

    for i in range(n//2 + n % 2):
        for j in range(n//2):
            tmp = matrix[n-1-j][i]
            matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
            matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
            matrix[j][n - 1 - i] = matrix[i][j]
            matrix[i][j] = tmp


matrix = [[1,1,1,1,1],[2,2,2,2,2],[3,3,3,3,3],[4,4,4,4,4],[5,5,5,5,5]]
rotate_smart(matrix)
print(matrix)