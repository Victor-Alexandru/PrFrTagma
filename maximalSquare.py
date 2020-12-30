class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        def expand_right(r,c):
            if c+1 < len(matrix[0])-1:
                return 0
            if matrix[r][c] == 0:
                return 0 
            else:
                 return 1 + expand_right(r,c+1)
        
        def expand_down(r,c):
            if r+1 < len(matrix)-1:
                return 0
            if matrix[r][c] == 0:
                return 0 
            else:
                return 1 + expand_right(r+1,c)
        
        def expand_diagonal(r,c):
            if r+1 < len(matrix)-1 and c+1 < len(matrix[0])-1:
                return 0
            if matrix[r][c] == 0:
                return 0 
            else:
                return 1 + expand_diagonal(r+1,c+1)
        

        def expand_square(r,c):
            down = expand_down(r,c)
            right = expand_right(r,c)



        max_length = 0
        if len(matrix) == 0:
           return 0


        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[i])):
                if matrix[i][j] == 1:
                    max_length = max(max_length,1)
                    expand_square(i,j) 




# We initialize another matrix (dp) with the same dimensions as the original one initialized with all 0’s.

# dp(i,j) represents the side length of the maximum square whose bottom right corner is the cell with index (i,j) in the original matrix.

# Starting from index (0,0), for every 1 found in the original matrix, we update the value of the current element as

# dp(i, j) = \min \big( \text{dp}(i-1, j), \text{dp}(i-1, j-1), \text{dp}(i, j-1) \big) + 1.dp(i,j)=min(dp(i−1,j),dp(i−1,j−1),dp(i,j−1))+1.

s = Solution()
print(s.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))