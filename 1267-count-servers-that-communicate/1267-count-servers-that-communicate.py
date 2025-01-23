class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        empty_row_indexes = []
        empty_col_indexes = []
        n_connected_servers = 0
        for i, row in enumerate(grid):
            s = sum(row)
            if s==1:
                empty_row_indexes.append(i)
            n_connected_servers+=s

        for i, col in enumerate(list(zip(*grid))):
            s = sum(col)
            if s==1:
                empty_col_indexes.append(i)
        
        for i in empty_row_indexes:
            for j in empty_col_indexes:
                if grid[i][j]==1:
                    n_connected_servers-=1

        return n_connected_servers

