class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        m_idx = [x for x in range(m)]
        n_idx = [x for x in range(n)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    m_idx[i] = -1
                    n_idx[j] = -1

        for i in range(m):
            for j in range(n):
                if m_idx[i] == -1 or n_idx[j] == -1:
                    matrix[i][j] = 0