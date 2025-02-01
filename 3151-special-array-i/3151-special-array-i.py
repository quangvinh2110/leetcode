class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        if nums[0]%2==0:
            remainder = 1
        else:
            remainder = 0

        for num in nums[1:]:
            if num%2!=remainder:
                return False
            remainder=1-remainder
        return True