class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_set = set(nums)
        count = {}
        result = [0 for i in range(k)]
        k_count = [0 for i in range(k)]
        for n in num_set:
            count[n] = 0
        for num in nums:
            count[num] += 1
        for key, value in count.items():
            m = min(k_count)
            if value > m:
                i = k_count.index(m)
                k_count[i] = value
                result[i] = key
        return result