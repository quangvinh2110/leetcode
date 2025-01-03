class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l=r=0    
        for r in range(len(nums)):
            if nums[r] == 0:
                k-=1
            if k<0:
                if nums[l] == 0:
                    k+=1
                l+=1
            # print("r:", r)
            # print("l:", l)
            # print("k:", k)
            # print("="*20)
        return r-l+1