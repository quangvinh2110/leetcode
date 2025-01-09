class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        from collections import Counter
        hashmap = Counter([' '.join(str(x) for x in row) for row in grid])
        grid_T = list(zip(*grid))
        count = 0
        for row in grid_T:
            count+=hashmap[','.join(str(x) for x in row)]
        return count