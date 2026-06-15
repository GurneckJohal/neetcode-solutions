class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == "1":
                    self.explore_island(x, y, grid)
                    count += 1

        return count
    
    def explore_island(self, x, y, grid):
        ROWS, COLS = len(grid), len(grid[0])
        if x < 0 or y < 0 or x == ROWS or y == COLS or grid[x][y] != "1":
            return
        
        grid[x][y] = "-1"

        self.explore_island(x - 1, y, grid)
        self.explore_island(x + 1, y, grid)
        self.explore_island(x, y - 1, grid)
        self.explore_island(x, y + 1, grid)

        return 
