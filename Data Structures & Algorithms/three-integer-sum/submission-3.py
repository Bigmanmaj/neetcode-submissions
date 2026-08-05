class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        if not nums:
            return res
        nums.sort()
        for i in range(len(nums)):
            target = -nums[i]
            j = 0
            k = len(nums) - 1
            while j < k:
                if nums[j] + nums[k] < target:
                    j += 1
                elif nums[j] + nums[k] > target:
                    k -= 1
                else:
                    if (i != j and j != k and i != k):
                        triplet = [nums[i], nums[j], nums[k]]
                        triplet.sort()
                        if triplet not in res:
                            res.append(triplet)
                    j += 1
        return res 