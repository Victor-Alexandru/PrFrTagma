class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        visited_nodes = []
        def dfs(r):
            for i in range(0,len(isConnected[r])):
                if i!=r and isConnected[r][i] == 1 and i not in visited_nodes:
                    visited_nodes.append(i)
                    dfs(i)
                
        components = 0         
        for i in range(0,len(isConnected)):
            if i not in visited_nodes:
                    visited_nodes.append(i)
                    components+=1
                    dfs(i)

                
        return components
s = Solution()
print(s.findCircleNum(isConnected=[[1,0,0],[0,1,0],[0,0,1]]))