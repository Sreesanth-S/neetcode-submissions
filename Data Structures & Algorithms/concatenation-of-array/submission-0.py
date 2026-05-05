class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums)
        while i < j:
            nums.append(nums[i])
            i += 1
        return nums