class Solution:
    def isHappy(self, n: int) -> bool:
        nums = set()
        return self.findHappy(n, nums)

    def findHappy(self, n, nums):
        if n == 1:
            return True
        digit = 1
        digit_sum = 0
        while digit <= n:
            t = (n // digit) % 10
            digit_sum += t * t
            digit *= 10

        if digit_sum in nums:
            return False
        nums.add(digit_sum)
        return self.findHappy(digit_sum, nums)