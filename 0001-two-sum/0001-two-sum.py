class Solution(object):


    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        nums = [(num, i) for i, num in enumerate(nums)]
        nums.sort(key=lambda x: x[0])
        
        first = 0
        last = len(nums)-1
        while first<last:
            if nums[first][0]+nums[last][0]>target:
                last-=1
            elif nums[first][0]+nums[last][0]<target:
                first+=1
            else:
                return [nums[first][1], nums[last][1]]
            