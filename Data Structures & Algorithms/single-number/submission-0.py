class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = {}
        for num in nums:
            if num not in seen:
                seen[num] = 1
            else:
                seen[num] += 1
        for k, v in seen.items():
            if v == 1:
                return k
