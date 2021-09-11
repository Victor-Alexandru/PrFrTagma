class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        nodes = {}
        visited = []
        for  i in range(numCourses):
            nodes[i] = []

        for edge in prerequisites:
            nodes[edge[1]].append(edge[0])

        def dfs(node_number):
            for neighbour in nodes[node_number]:
                if neighbour in visited:
                    return False
                visited.append(neighbour)
                dfs(neighbour)

            return

        print(nodes)

        for i in range(numCourses):
            visited = [i]
            if dfs(i) is False:
                return False 

        return True

s = Solution()
print(s.canFinish(numCourses=2,prerequisites=[[1,0],[0,1]]))