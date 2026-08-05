class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        start = []
        for n in num_set:
            if n - 1 not in num_set:
                start.append(n)
        count = [1] * len(start)
        start.sort()
        start.append(10^7)
        for i in range(len(start) - 1):
            for n in num_set:
                if n > start[i] and n < start[i + 1]:
                    count[i] += 1
        if count:
            return max(count)
        else:
            return 0
        