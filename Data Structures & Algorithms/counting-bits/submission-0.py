class Solution:
    def countBits(self, n: int) -> List[int]:
        results = []
        for i in range(n + 1):
            count = 0
            b = bin(i)
            print(b)
            for j in range(len(b) - 2):
                count += (b[j + 2] == '1')
            results.append(count)
        return results
        