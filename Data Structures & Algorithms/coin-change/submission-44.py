class Solution:
    def __init__(self):
        self.memo = {}
        sys.setrecursionlimit(5000)
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        branches = []
        for c in coins:
            if c <= amount:
                if amount - c in self.memo.keys():
                    if self.memo[amount - c] == -1:
                        continue
                    branches.append(self.memo[amount - c] + 1)
                else:
                    res = self.coinChange(coins, amount - c)
                    if res != -1:
                        branches.append(res + 1)
                    self.memo[amount - c] = res
        if not branches:
            self.memo[amount] = -1
            return -1
        else:
            num_coins = min(branches)
            self.memo[amount] = num_coins
            return num_coins
        