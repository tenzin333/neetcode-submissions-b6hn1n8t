class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        wordSet = set(wordDict)
        memo = {}

        def dfs(i):
            if i == len(s):
                return True
            
            if i in memo:
                return memo[i]

            for word in wordSet:
                if s.startswith(word, i):
                    if dfs(i + len(word)):
                        memo[i] = True   # ✅ fix here
                        return True
            
            memo[i] = False
            return False

        return dfs(0)