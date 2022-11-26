#TimeComplexity: O(m*n)
#SpaceComplexity: O(1)
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        m = len(grid) # length of grid
        n = len(grid[0]) # length of grid of 0

        for j in range(n-2,-1,-1):
            grid[m-1][j] += grid[m-1][j+1] # run until the loop and add the grid of m-1th value

        for i in range(m-2,-1,-1):
            grid[i][n-1] += grid[i+1][n-1] # run until the loop and add the grid of n-1th value

        for i in range (m-2,-1,-1):
            for j in range(n-2,-1,-1): # run until the grid reaches last cell then add the minimum between the grid[i+1][j] and grid[i][j+1]
                grid[i][j] += min(grid[i+1][j],grid[i][j+1])

        return grid[0][0] # return the grid starting value
