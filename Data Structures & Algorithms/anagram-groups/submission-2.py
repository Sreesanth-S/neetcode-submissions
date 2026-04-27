class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        i = 0
        res = {}
        for i in strs:
            count = [0]*26
            for c in i: 
                count[ord(c) - ord('a')] += 1
            key = tuple(count)
            if key not in res:
                res[key] = [i]
            else:
                res[key].append(i)
        return list(res.values())          