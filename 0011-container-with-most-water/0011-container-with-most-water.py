class Solution:
    def maxArea(self, height: List[int]) -> int:
        first = 0
        last = len(height)-1
        result = 0
        while first < last:
            if height[first] <= height[last]:
                tmp = height[first]*(last-first)
                first+=1
            else:
                tmp = height[last]*(last-first)
                last-=1
            if tmp > result:
                result = tmp
                
        return result
            