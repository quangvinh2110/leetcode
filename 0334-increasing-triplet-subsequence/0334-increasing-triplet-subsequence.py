class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float(inf)
        second = float(inf)
        for a in nums:
            if a <= first:
                first = a
            elif a <= second:
                second = a
            else:
                return True
        return False
            