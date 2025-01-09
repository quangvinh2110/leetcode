class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        from collections import Counter
        hashmap = Counter([' '.join(str(x) for x in row) for row in grid])
        count = 0
        for row in list(zip(*grid)):
            count+=hashmap[' '.join(str(x) for x in row)]
        return count