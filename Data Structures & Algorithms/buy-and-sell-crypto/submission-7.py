class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            p = prices[i] - min(prices[:i])
            if p > profit:
                profit = p
        return profit

        