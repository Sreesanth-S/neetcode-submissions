class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        actual_volume = 0
        while i < j:
            height = min(heights[i], heights[j])
            width = j-i
            volume = height * width
            if volume > actual_volume:
                actual_volume = volume
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return actual_volume