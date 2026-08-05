class Solution:
    width = -1
    height = -1
    def numIslands(self, grid: List[List[str]]) -> int:
        self.width = len(grid)
        self.height = len(grid[0])
        groups = 0
        for i in range(self.width):
            for j in range(self.height):
                if grid[i][j] == "1":
                    print(i)
                    print(str(j) + "\n")
                    groups += 1
                    self.depthFirstSearch(grid, i, j)
        return groups
    
    def depthFirstSearch(self, grid, i, j):
        # entire point of this function is to mark part of the same island as visted
        grid[i][j] = "0"
        print(str(grid) + "\n")
        #left
        if i - 1 >= 0 and grid[i-1][j] == "1":
            self.depthFirstSearch(grid, i-1, j)
        #right
        if i + 1 <= self.width - 1 and grid[i+1][j] == "1":
            self.depthFirstSearch(grid, i+1, j)
        #down
        if j + 1 <= self.height - 1 and grid[i][j+1] == "1":
            self.depthFirstSearch(grid, i, j+1)
        #up
        if j - 1 >= 0 and grid[i][j-1] == "1":
            self.depthFirstSearch(grid, i, j-1)
