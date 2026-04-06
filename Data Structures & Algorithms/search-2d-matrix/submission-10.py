class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        row, col  = len(matrix) , len(matrix[0])
        left , right =0, (row*col)-1  # treating 2d as 1d array

        while left<=right:
            mid = left + (right-left)//2

            mid_num = matrix[mid // col][mid%col]  # back to 2d
            if mid_num == target:
                return True
            elif mid_num < target:
                left = mid+1
            else:
                right = mid-1

        return False
                