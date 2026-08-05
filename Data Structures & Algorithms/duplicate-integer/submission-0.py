class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = {}
        for num in nums:
            if num in map:
                map[num] += 1
            else:
                map[num] = 1
        num_set = set(nums)
        for num in num_set:
            if map[num] > 1:
                return True
        return False
