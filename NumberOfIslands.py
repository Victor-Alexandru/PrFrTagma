class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def vistGrid(sr,sc):
            if sc + 1 < len(grid[0]) and grid[sr][sc+1] == '1':
                grid[sr][sc+1] = 2   
                vistGrid(sr,sc+1)

            if sc - 1 >=  0 and grid[sr][sc-1] == '1':
                grid[sr][sc-1] = 2       
                vistGrid(sr,sc-1)

            if sr - 1  >=  0 and grid[sr-1][sc] == '1':
                grid[sr-1][sc] = 2       
                vistGrid(sr-1,sc)

            if sr + 1  < len(grid) and grid[sr+1][sc] == '1':
                grid[sr+1][sc] = 2       
                vistGrid(sr+1,sc)
        contor = 0
        for i in range(0,len(grid)):
            for j in range(0,len(grid[i])):
                if int(grid[i][j]) == 1:
                    contor += 1
                    vistGrid(i,j)
        return contor

        

s = Solution()
print(s.numIslands(grid=[  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]]))