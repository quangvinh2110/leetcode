class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        sum_above = sum(grid[0][1:])
        sum_below = 0
        possible_results = [sum_above]
        for i in range(1, len(grid[0])):
            sum_above-=grid[0][i]
            sum_below+=grid[1][i-1]
            possible_results.append(max(sum_above, sum_below))
        return min(possible_results)