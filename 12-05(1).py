trd = [[]]
rows = None
cols = None

class Solution:
    def maxG(self, grid, i, j):
        global trd
        global rows
        global cols
        # print(i, j)
        if trd[i][j]:
            return 0
        
        ans = grid[i][j]
        maxE = 0
        trd[i][j] = True

        if (i - 1 >= 0) and (not trd[i-1][j]):
            maxE = max(maxE, self.maxG(grid, i-1, j))
            
        if (i + 1 < rows) and (not trd[i+1][j]):
            maxE = max(maxE, self.maxG(grid, i+1, j))
            
        if (j + 1 < cols) and (not trd[i][j+1]):
            maxE = max(maxE, self.maxG(grid, i, j+1))
            
        if (j - 1 >= 0) and (not trd[i][j-1]):
            maxE = max(maxE, self.maxG(grid, i, j-1))
            
        # print(i, j, maxE, trd)
        ans += maxE
        trd[i][j] = False
        return ans
        
    
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        global rows
        rows = len(grid)
        
        global cols
        cols = len(grid[0])
        
        global trd
        trd = []
        trd = [[False]*cols for i in range(0, rows)]
        
        for i, row in enumerate(grid):
            for j, gold in enumerate(row):
                if gold == 0:
                    trd[i][j] = True        
        
        # print(trd)
        ans = 0
        for i, row in enumerate(grid):
            for j, gold in enumerate(row):
                ans = max(ans, self.maxG(grid, i, j))
                
        return ans
        
