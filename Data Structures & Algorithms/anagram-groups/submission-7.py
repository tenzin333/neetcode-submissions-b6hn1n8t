class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        mapHash = {}

        for word in strs:
            key = ''.join(sorted(word))
            mapHash[key] = [*mapHash.get(key, []), word]
        
        res = []
        for val in mapHash.values():
            res.append(val)
        return res
        
   