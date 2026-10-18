class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLUMNS = len(matrix), len(matrix[0])
        self.sum_matrix = [[0] * (COLUMNS + 1) for rows in range(ROWS + 1)]

        for row in range(ROWS):
            prefix = 0
            for column in range(COLUMNS):
                prefix += matrix[row][column]
                sum_above = self.sum_matrix[row][column + 1]
                self.sum_matrix[row + 1][column + 1] = prefix + sum_above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, c1, r2, c2 = row1+1, col1+1, row2+1, col2+1

        bottom_right = self.sum_matrix[r2][c2]
        sum_above = self.sum_matrix[r1 - 1][c2]
        left = self.sum_matrix[r2][c1 - 1]
        top_left = self.sum_matrix[r1 - 1][c1 - 1]

        return bottom_right - sum_above - left + top_left

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

# i hate re and matrix so much fr