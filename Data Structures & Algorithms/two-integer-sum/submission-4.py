class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            map[difference] = i
        for i in range(len(nums)):
            if nums[i] in map.keys():
                if i != map[nums[i]]:
                    return [i, map[nums[i]]]