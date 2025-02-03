class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        increasing_subarr = [nums[0]]
        increasing_subarr_len = 1
        decreasing_subarr = [nums[0]]
        decreasing_subarr_len = 1
        for num in nums[1:]:
            if num>increasing_subarr[-1]:
                increasing_subarr.append(num)
            else:
                increasing_subarr_len = max(increasing_subarr_len, len(increasing_subarr))
                increasing_subarr = [num]
            
            if num<decreasing_subarr[-1]:
                decreasing_subarr.append(num)
            else:
                decreasing_subarr_len = max(decreasing_subarr_len, len(decreasing_subarr))
                decreasing_subarr = [num]
        return max(increasing_subarr_len, decreasing_subarr_len, len(decreasing_subarr), len(increasing_subarr))