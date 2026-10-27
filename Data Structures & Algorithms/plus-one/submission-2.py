class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = [0 for n in digits]
        carry.append(0)
        digits[-1] += 1
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] + carry[i+1] > 9:
                digits[i] = carry[i+1] * 10 % 10
                carry[i] += 1
            else:
                digits[i] += carry[i+1]

        if carry[0] > 0:
            digits.insert(0, carry[0])
        return digits