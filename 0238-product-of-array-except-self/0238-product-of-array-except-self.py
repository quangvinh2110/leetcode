class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prods = [1]
        right_prods = [1]
        for num in nums[:-1]:
            left_prods.append(left_prods[-1]*num)
        for num in nums[len(nums)-1:0:-1]:
            right_prods.append(right_prods[-1]*num)
        result = []
        for l_prod, r_prod in zip(left_prods, right_prods[::-1]):
            result.append(l_prod*r_prod)
        return result