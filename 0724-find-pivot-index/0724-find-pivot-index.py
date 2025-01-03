class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum=sum(nums)
        left_sums=0
        for i in range(len(nums)):
            if left_sums==total_sum-left_sums-nums[i]:
                return i
            left_sums+=nums[i]
        
        return -1