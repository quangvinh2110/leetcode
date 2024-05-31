class Node:
    def __init__(self, value, ind):
        self.value = value
        self.ind = ind

class Solution(object):

    def binary_search(self, start_id, sorted_list, target):
        if len(sorted_list)==0:
            return -1
        if len(sorted_list)==1:
            if target == sorted_list[0].value:
                return start_id
            else:
                return -1

        mid_id = len(sorted_list)//2
        median = sorted_list[mid_id].value
        if target == median:
            return start_id + mid_id
        elif target > median:
            return self.binary_search(start_id+mid_id+1, sorted_list[mid_id+1:], target)
        else:
            return self.binary_search(start_id, sorted_list[:mid_id], target)
        


    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums = [Node(num, i) for i, num in enumerate(nums)]
        nums.sort(key=lambda x: x.value)
        for i, num in enumerate(nums):
            j = self.binary_search(0, nums[:i] + nums[i+1:], target-nums[i].value)
            if j!=-1:
                if j>=i:
                    j=j+1
                return [nums[i].ind, nums[j].ind]