class Solution:
    def rotate(self, matrix) -> None:
        n = len(matrix)
        for i in range(n):
            matrix[i] = matrix[i][::-1]
        for j in range(n):
            for i in range(0, n-j-1):
                k = matrix[i][j]
                matrix[i][j] = matrix[n-j-1][n-i-1]
                matrix[n-j-1][n-i-1] = k