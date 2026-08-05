class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product = [1]
        suffix_product = [1]
        res = []
        for i in range(1, len(nums)):
            prefix_product.append(nums[i - 1] * prefix_product[i - 1])
            suffix_product.append(nums[-i] * suffix_product[i - 1])
        print(prefix_product)
        print(suffix_product)
        for i in range(len(nums)):
            res.append(prefix_product[i] * suffix_product[-i-1])
        return res