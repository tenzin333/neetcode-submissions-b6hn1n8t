class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # freq = {}

        # for i in range(len(numbers)):
        #     diff = target - numbers[i]
        #     if numbers[i] in freq:
        #         return [freq[numbers[i]] + 1, i+1]
        #     freq[diff] = i
        # return []

        sorted(numbers)

        left = 0 
        right = len(numbers)-1

        while left < right:
            total = numbers[left] + numbers[right]

            if total == target:
                return [left+1, right+1]
            if total < target:
                left += 1
            else:
                right -= 1
        return []