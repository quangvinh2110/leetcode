class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        from collections import Counter
        
        counter = Counter(nums)
        n_ops = 0
        if k%2==0:
            for num in counter.keys():
                if num>k/2:
                    pass
                elif num==k//2:
                    n_ops+=counter[num]//2
                else:
                    n_ops+=min(counter[num], counter[k-num])
        else:
            for num in counter.keys():
                if num>k/2:
                    pass
                else:
                    n_ops+=min(counter[num], counter[k-num])
                    
        return n_ops
        