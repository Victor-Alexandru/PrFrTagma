import heapq
class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        min_diference = 21478921
        def backtrackSolution(lista):
            nonlocal min_diference
            if len(lista) < 2:
                pass
            elif len(lista) == 2:
                min_diference = min(min_diference,abs(lista[0]-lista[1]))
            else:
                for i in range(0,len(lista)-1):
                    for j in range(i+1,len(lista)):
                        difference = abs(lista[i]-lista[j])
                        backtrackSolution(lista[0:i]+lista[i+1:j]+lista[j+1:len(lista)]+[difference])
        
        backtrackSolution(stones)
        return min_diference

s = Solution()
print(s.lastStoneWeightII([40,33,31,26,21]))