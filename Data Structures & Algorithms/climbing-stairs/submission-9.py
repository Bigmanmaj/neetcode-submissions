class Solution:
    def climbStairs(self, n: int) -> int:
        mem = [1, 2]
        if n == 2:
            return 2
        if n == 1:
            return 1
        else:
            for i in range(n - 2):
                res = mem[i] + mem[i+1]
                mem.append(res)
        print(mem)
        return mem[-1]