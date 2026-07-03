class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        if len(nums1) > len(nums2):
            nums1 , nums2 = nums2, nums1

        n1 = len(nums1)
        n2 = len(nums2)

        total = n1 + n2
        half = total // 2

        left = 0 
        right = n1

        while left <= right:
            i = left + (right - left + 1) // 2
            j = half - i

            aleft = nums1[i-1] if i > 0 else float('-inf')
            aright = nums1[i] if i < n1 else float('inf')

            bleft = nums2[j-1] if j > 0 else float('-inf')
            bright = nums2[j] if j < n2 else float('inf')

            if aleft <= bright and bleft <= aright:
                if total % 2 ==0:
                    return (max(aleft,bleft) + min(aright, bright)) / 2
                else:
                    return min(aright, bright)
            elif aleft > bright:
                right = i - 1
            else:
                left = i + 1
        return 0.0


