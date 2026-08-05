class Solution:
    def maxArea(self, heights: List[int]) -> int:
        water = 0
        i = 0
        j = len(heights) - 1
        while i < j:
            water = max(water, min(heights[i], heights[j]) * (j - i))
            if heights[j] > heights[i]:
                i += 1
            elif heights[i] >= heights[j]:
                j -= 1
        return water