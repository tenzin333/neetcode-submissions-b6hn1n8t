class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows = len(matrix)
        cols = len(matrix[0])

        target_row = []

        for i in range(rows):
            if  matrix[i][0] <= target <= matrix[i][cols-1]:
                target_row = matrix[i]
                break

        left = 0
        right = len(target_row) - 1

        while left <= right:
            mid = left + (right-left+1) // 2

            if target_row[mid] == target:
                return True
            elif target_row[mid] > target:
                right = mid - 1
            else:
                left  =  mid + 1
        return False
