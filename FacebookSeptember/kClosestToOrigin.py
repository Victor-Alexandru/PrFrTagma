from math import sqrt
from heapq import heappop, heappush, heapify
class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        rez = []

        def calculate_distance(lista):
            return  sqrt((lista[0])**2 + (lista[1])**2)

        # Creating empty heap
        heap = []
        heapify(heap)

        for i in  range(len(points)):
            point = points[i]
            print(point,calculate_distance(point))
            if len(heap) < K  :
                heappush(heap,(-1 * calculate_distance(point),point))  
        
            elif len(heap) >= K and heap[0][0] < -1 * calculate_distance(point) :
                heappop(heap)
                heappush(heap,(-1 * calculate_distance(point),point))


        return [x[1] for x in heap]
        

s = Solution()
print(s.kClosest(points = 
[[-95,76],[17,7],[-55,-58],[53,20],[-69,-8],[-57,87],[-2,-42],[-10,-87],[-36,-57],[97,-39],[97,49]], K = 5))