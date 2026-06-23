class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left = 0 
        right = 0

        visited = set()
        n = len(s)

        max_len = 0
        while right < n:
            while s[right] in visited:
                visited.remove(s[left])
                left += 1
            max_len = max(max_len, right - left + 1)
            visited.add(s[right])
            right += 1
        return max_len