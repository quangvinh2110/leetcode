class Solution(object):
    
    def twoSum(self, sorted_nums, target,results):
        first = 0
        last = len(sorted_nums)-1
        
        while first < last:
            if sorted_nums[first] + sorted_nums[last] > target:
                last = last - 1
            elif sorted_nums[first] + sorted_nums[last] < target:
                first = first + 1
            else:
                if -target < sorted_nums[first]:
                    results[(-target,sorted_nums[first],sorted_nums[last])] = 1
                    # results.append(str(-target)+" "+str(sorted_nums[first])+" "+str(sorted_nums[last]))
                elif -target > sorted_nums[last]:
                    results[(sorted_nums[first],sorted_nums[last],-target)] = 1
                    # results.append(str(sorted_nums[first])+" "+str(sorted_nums[last])+" "+str(-target))
                else:
                    results[(sorted_nums[first],-target,sorted_nums[last])] = 1
                    # results.append(str(sorted_nums[first])+" "+str(-target)+" "+str(sorted_nums[last]))
                first = first + 1
                last = last - 1
        
        return results
        
        
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        # results = set()
        is_visited = {}
        results = {}
        for i, num in enumerate(nums[:-2]):
            if num not in is_visited:
                self.twoSum(nums[i+1:], -num,results)
                is_visited[num] = 1
                
        final = [list(o) for o in results.keys()]
        # print(results.keys())
        # results = list(map(lambda x: [int(i) for i in x.split()], results))
        return final
            