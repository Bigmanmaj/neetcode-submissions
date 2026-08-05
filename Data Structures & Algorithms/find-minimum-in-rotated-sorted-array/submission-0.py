class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        while start != end:
            midpoint = (end - start) // 2 + start
            if nums[midpoint] > nums[end]:
                start = midpoint + 1
            else:
                end = midpoint
        return nums[start]