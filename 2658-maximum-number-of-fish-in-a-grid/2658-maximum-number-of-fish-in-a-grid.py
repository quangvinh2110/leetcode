class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        # if max(map(max, grid))==0:
        #     return 0
        m = len(grid)
        n = len(grid[0])
        ind_set = set()
        clusters = []
        for i in range(m):
            for j in range(n):
                ind_set.add((i, j))
                n_fishs = 0
                if grid[i][j]==0:
                    continue
                bfs_queue = [(i,j)]
                while len(bfs_queue)>0:
                    i, j = bfs_queue.pop(0)
                    n_fishs+=grid[i][j]
                    if i<m-1 and grid[i+1][j]>0 and (i+1, j) not in ind_set:
                        ind_set.add((i+1, j))
                        bfs_queue.append((i+1, j))
                    if j<n-1 and grid[i][j+1]>0 and (i, j+1) not in ind_set:
                        ind_set.add((i, j+1))
                        bfs_queue.append((i, j+1))
                    if i>0 and grid[i-1][j]>0 and (i-1, j) not in ind_set:
                        ind_set.add((i-1, j))
                        bfs_queue.append((i-1, j))
                    if j>0 and grid[i][j-1]>0 and (i, j-1) not in ind_set:
                        ind_set.add((i, j-1))
                        bfs_queue.append((i, j-1))
                clusters.append(n_fishs)
        return max(clusters) if clusters else 0