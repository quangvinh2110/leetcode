class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_0_ind = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[i], nums[non_0_ind] = nums[non_0_ind], nums[i]
                non_0_ind+=1
        return nums