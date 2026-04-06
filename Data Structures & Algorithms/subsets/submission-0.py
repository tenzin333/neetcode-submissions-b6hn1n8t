class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        subsets = [[]]

        for num in nums:
            temp = []

            for subset in subsets:
                temp.append(subset + [num])
            subsets.extend(temp)
        return subsets