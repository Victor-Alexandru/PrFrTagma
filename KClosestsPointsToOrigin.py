from math import sqrt

class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        def EuclDistance(point1,point2):
            return (point1[0]-point2[0])**2 + (point1[1]-point2[1])**2 

        my_map = {}
        for point in points:
            my_map[tuple(point)] = EuclDistance([0,0],point)

        results = []
        my_map = sorted(my_map.items(), key=lambda item: item[1])
        for key in my_map:
            if len(results) == K:
                break
            results.append(list(key[0]))
        return results


# class Solution(object):
#     def kClosest(self, points, K):
#         points.sort(key = lambda P: P[0]**2 + P[1]**2)
#         return points[:K]


s = Solution()
print(s.kClosest(points = [[3,3],[5,-1],[-2,4]] , K=2))