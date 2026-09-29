class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)
        while start < end:
            midpoint = (start + end) // 2
            if nums[midpoint] == target:
                return midpoint
            if nums[midpoint] > target:
                end = midpoint
            elif nums[midpoint] < target:
                start = midpoint + 1
        return -1