class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) < k:
            return sum(nums)/len(nums)
        max_k_sum = sum(nums[:k])
        k_sum = max_k_sum
        for i in range(1, len(nums)-k+1):
            k_sum = k_sum - nums[i-1] + nums[i+k-1]
            if k_sum>max_k_sum:
                max_k_sum = k_sum
        return max_k_sum/k
        