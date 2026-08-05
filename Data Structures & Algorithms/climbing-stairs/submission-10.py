class Solution:
    def climbStairs(self, n: int) -> int:
        mem = [1, 2]
        if n <= 2:
            return mem[n - 1]
        else:
            for i in range(n - 2):
                res = mem[i] + mem[i+1]
                mem.append(res)
        return mem[-1]