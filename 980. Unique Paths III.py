# Your runtime beats 98.50 % of python3 submissions.
# Your memory usage beats 94.24 % of python3 submissions.

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        # Backtracking approach
        self.unique = 0
        def move(grid: List[List[int]],i:int,j:int):
            if grid[i][j] == 0:
                grid[i][j] = 1
                
            if grid[i][j] == 2:
                for row in grid:
                    if 0 in row:
                        return
                self.unique += 1
                return
            
            # Not finished so continue
            # Pick all new directions that are avaliable
            
            # Right
            if j + 1 < len(grid[0]) and abs(grid[i][j+1]) != 1:
                move(grid,i,j+1)
            # Down
            if i + 1 < len(grid) and abs(grid[i+1][j]) != 1:
                move(grid,i+1,j)
            # Left
            if j - 1 >= 0 and abs(grid[i][j-1]) != 1:
                move(grid,i,j-1)
            # Up
            if i - 1 >= 0 and abs(grid[i-1][j]) != 1 :
                move(grid,i-1,j)
            grid[i][j] = 0
        
        #Get starting index
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == 1:
                    move(grid, i,j)
                    return self.unique
        return self.unique
