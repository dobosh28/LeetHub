class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        # Initialize the matrix with all zeros
        matrix = [[0] * n for _ in range(m)]
        
        # Apply the increments
        for r, c in indices:
            # Increment all cells in row r
            for j in range(n):
                matrix[r][j] += 1
            # Increment all cells in column c
            for i in range(m):
                matrix[i][c] += 1
        
        # Count the number of odd-valued cells
        odd_count = 0
        for row in matrix:
            for cell in row:
                if cell % 2 != 0:
                    odd_count += 1
        
        return odd_count

