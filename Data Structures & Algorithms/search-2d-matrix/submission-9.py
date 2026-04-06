class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for row in matrix:
            if  row[0] <= target and target <= row[len(row)-1]:
                left , right=0, len(row)-1
                while left<=right:
                    mid  = left + (right-left)//2
                    if row[mid] == target:
                        return True
                    elif row[mid] > target:
                        right  = mid-1
                    else :
                        left = mid+1
                return False
        return False
                