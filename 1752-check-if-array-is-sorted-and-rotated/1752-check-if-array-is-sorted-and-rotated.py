class Solution:
    def check(self, nums: List[int]) -> bool:
        flag = 0

        for i in range(1, len(nums)):
            if nums[i]<nums[i-1]:
                flag+=1
                if flag==2:
                    return False
        if flag==0:
            return True
        elif flag==1 and nums[0]>nums[-1]:
            return True
        return False