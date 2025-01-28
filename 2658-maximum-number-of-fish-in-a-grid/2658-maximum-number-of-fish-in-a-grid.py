class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        # if max(map(max, grid))==0:
        #     return 0
        m = len(grid)
        n = len(grid[0])
        ind_set = {(i, j) for i in range(m) for j in range(n)}
        clusters = []
        while len(ind_set)>0:
            i, j = ind_set.pop()
            n_fishs = 0
            if grid[i][j]==0:
                continue
            bfs_queue = [(i,j)]
            while len(bfs_queue)>0:
                i, j = bfs_queue.pop(0)
                n_fishs+=grid[i][j]
                if i<m-1 and grid[i+1][j]>0 and (i+1, j) in ind_set:
                    ind_set.remove((i+1, j))
                    bfs_queue.append((i+1, j))
                if j<n-1 and grid[i][j+1]>0 and (i, j+1) in ind_set:
                    ind_set.remove((i, j+1))
                    bfs_queue.append((i, j+1))
                if i>0 and grid[i-1][j]>0 and (i-1, j) in ind_set:
                    ind_set.remove((i-1, j))
                    bfs_queue.append((i-1, j))
                if j>0 and grid[i][j-1]>0 and (i, j-1) in ind_set:
                    ind_set.remove((i, j-1))
                    bfs_queue.append((i, j-1))
            clusters.append(n_fishs)
        return max(clusters) if clusters else 0