class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = {}
        for num in nums:
            if num - 1 not in nums:
                seq[num] = []
        keys = list(seq.keys())
        keys.sort()
        keys.append(9999999)
        for i in range(len(keys) - 1):
            for num in nums:
                if num >= keys[i] and num not in seq[keys[i]] and num < keys[i+1]:
                    seq[keys[i]].append(num)
        m = 0
        for v in seq.values():
            if len(v) > m:
                m = len(v)
        return m
