class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # non zero index
        nzi=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[nzi],nums[i]=nums[i],nums[nzi]
                nzi=nzi+1