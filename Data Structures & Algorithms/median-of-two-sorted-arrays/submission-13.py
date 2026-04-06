class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A , B = nums1, nums2

        if len(A) > len(B):
            A, B = B, A
        
        total = len(A) + len(B)
        half = (total+1) // 2

        l , r= 0, len(A)
        while True:
            i = (l+r)//2
            j = half - i

            Aleft = A[i-1] if i > 0 else float("-infinity")
            Aright = A[i] if i < len(A) else float("infinity")

            Bleft = B[j-1] if j > 0 else float("-infinity")
            Bright = B[j] if j < len(B) else float("infinity")

            if Aleft<=Bright and Bleft<=Aright:
                if total % 2:
                    return max(Aleft,Bleft)
                else:
                    return (max(Aleft,Bleft) + min(Aright,Bright)) / 2
            elif Aleft > Bright:
                r = i- 1  # decreasing cut on num1 by 1 
            else :
                l = i+1 


        