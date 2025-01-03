class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        half_nums_sum = sum(nums) / 2
        # print(sum(nums))
        # print(half_nums_sum)
        left = 0
        count = 0
        for num in nums[:-1]:
            left+=num
            if left >= half_nums_sum:
                # print(left)
                count+=1
        return count