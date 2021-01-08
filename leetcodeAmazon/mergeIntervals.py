class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) == 0 :
            return []
        intervals = sorted(intervals,key=lambda x: x[0])
        
        rez = []
        rez.append(intervals[0])
        for i in range(1,len(intervals)):
            if rez[-1][1] >= intervals[i][0]:
                rez[-1][1] = max(rez[-1][1],intervals[i][1]) 
            else:
                rez.append(intervals[i])
                
        return rez

#12 min