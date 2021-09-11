class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not len(intervals):
            return []
        intervals = sorted(intervals,key= lambda x: x[0])
        rez = []

        for i in range(0,len(intervals)):
            
            if not rez or rez[-1][1] < intervals[i][0]:
                rez.append(intervals[i])
            else:
                rez[-1][1] = max(intervals[i][1],rez[-1][1])
            
            
        return rez

s = Solution()
print(s.merge(intervals=[[1,4],[4,5]]))