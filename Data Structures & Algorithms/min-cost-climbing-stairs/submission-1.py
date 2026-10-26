class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.memo = [10000000 for c in cost]
        self.cost = cost
        self.dfs(-1)
        return min(self.memo[0], self.memo[1])
        
    def dfs(self, i):
        if i >= len(self.cost):
            return 0
        if self.memo[i] != 10000000:
            return self.memo[i]
        res = self.cost[i] + min(self.dfs(i+1), self.dfs(i+2))
        if self.memo[i] > res:
            self.memo[i] = res
        print(i)
        print(res)
        print(self.memo)
        print('\n')
        return res
        
