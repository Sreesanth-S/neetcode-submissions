class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        non_dup = set(nums)
        longest = 0
        for i in non_dup:
            if i in non_dup:
                length = 1
                while (i+length) in non_dup:
                    length += 1
                longest = max(length, longest)
        return longest