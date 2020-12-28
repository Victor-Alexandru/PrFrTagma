class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """


        def visit_nodes(r,c):
            #visit_down
            if r<len(grid)-1 and grid[r+1][c] == "1":
                grid[r+1][c] = "2"
                visit_nodes(r+1,c)
            #visit_right
            if c<len(grid[r])-1 and grid[r][c+1] == "1":
                grid[r][c+1] = "2"
                visit_nodes(r,c+1)


            #visit_left
            if r-1>=0 and grid[r-1][c] == "1":
                grid[r-1][c] = "2"
                visit_nodes(r-1,c)

            #visit_up
            if c-1>=0 and grid[r][c-1] == "1":
                grid[r][c-1] = "2"
                visit_nodes(r,c-1)


        nr_of_islands = 0 
        for i in range(0,len(grid)):
            for j in range (0, len(grid[i])):
                if grid[i][j] == "1":
                    nr_of_islands+=1
                    grid[i][j] = "2"
                    visit_nodes(i,j)


            
        return nr_of_islands

s = Solution()

# print(s.numIslands(
# [["1","1","1"],["0","1","0"],["1","1","1"]]))

#Explanation de la ei de pe site:
'''
DFS:

Complexity Analysis

Time complexity : O(M \times N)O(M×N) where MM is the number of rows and NN is the number of columns.

Space complexity : worst case O(M \times N)O(M×N) in case that the grid map is filled with lands where DFS goes by M \times NM×N deep.

BFS:

Complexity Analysis

Time complexity : O(M \times N)O(M×N) where MM is the number of rows and NN is the number of columns.

Space complexity : O(min(M, N))O(min(M,N)) because in worst case where the grid is filled with lands, the size of queue can grow up to min(M,NM,N).


DISJOINTS SETS ( uitate pe internet )
Complexity Analysis

Time complexity : O(M \times N)O(M×N) where MM is the number of rows and NN is the number of columns. Note that Union operation takes essentially constant time[1] when UnionFind is implemented with both path compression and union by rank.

Space complexity : O(M \times N)O(M×N) as required by UnionFind data structure.



'''