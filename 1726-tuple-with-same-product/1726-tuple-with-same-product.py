class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        hashmap = {}
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                prod = nums[i]*nums[j]
                if prod in hashmap:
                    hashmap[prod]+=1
                else:
                    hashmap[prod]=1
        result = 0
        for _, count in hashmap.items():
            result+=4*(count-1)*count
        return result
        