class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies) - extraCandies
        return list(map(lambda c: c>=max_candies, candies))
        