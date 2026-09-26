class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        islands = 0
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()

        def dfs(r,c):
            if (r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r, c) not in visited):
                visited.add((r,c))

                dfs(r+1, c)
                dfs(r-1, c)
                dfs(r,c+1)
                dfs(r,c-1)


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    islands+=1
                    dfs(r,c)
        return islands
        
        