class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        freq = {}

        for i in range(len(numbers)):
            diff = target - numbers[i]
            if numbers[i] in freq:
                return [freq[numbers[i]] + 1, i+1]
            freq[diff] = i
        return []