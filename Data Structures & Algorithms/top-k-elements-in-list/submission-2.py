class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        res = [[] for i in range(len(nums)+1)]
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        for key, value in d.items():
            res[value].append(key)
        res2 = []
        for i in range(len(res)-1, 0, -1):
            for j in res[i]:
                res2.append(j)
                if len(res2) == k:
                    return res2