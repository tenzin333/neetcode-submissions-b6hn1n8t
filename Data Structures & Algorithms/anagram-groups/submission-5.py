class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        seen = {}

        for word in strs:
            key = "".join(sorted(word))

            if key in seen:
                seen[key] = [*seen[key], word]
            else:
                seen[key] = [word]

        res = []
        for n  in seen.values():
            print(n)
            res.append(n)
        return res
