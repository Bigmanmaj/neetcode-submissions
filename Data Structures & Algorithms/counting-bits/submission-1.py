class Solution:
    def countBits(self, n: int) -> List[int]:
        results = []
        for i in range(n + 1):
            count = 0
            for j in range(i):
                count += (i >> j) & 1
            results.append(count)
        return results
        