class Solution(object):
    
    def binary_search(self, start_id, nums, target):
        # print("start_id", start_id)
        # print("nums: ", nums)
        if len(nums)==0:
            return -1
        if len(nums)==1:
            if nums[0]==target:
                return start_id
            else:
                return -1
            
        median_id = len(nums)//2
        median = nums[median_id]
        if target > median:
            return self.binary_search(start_id+median_id+1, nums[median_id+1:], target)
        elif target < median:
            return self.binary_search(start_id, nums[:median_id], target)
        else:
            return start_id + median_id
        
        
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.binary_search(0, nums, target)
        