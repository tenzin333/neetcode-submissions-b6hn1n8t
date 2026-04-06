class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}

        for word in strs:
            key = "".join(sorted(list(word)))

            hashMap[key] = [*(hashMap[key] if key in hashMap else []), word]
        res = []
        for value in hashMap.values():
            res.append(value)

        return res