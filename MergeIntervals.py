# class Solution(object):
#     def merge(self, intervals):
#         """
#         :type intervals: List[List[int]]
#         :rtype: List[List[int]]
#         """
#         def are_two_intervals_intersectable(int1,int2):
#             if int2[0] <= int1[1] and int2[1] >= int1[1]:
#                 return True
            
#             if int1[0] <= int2[1] and int1[1] >= int2[1]:
#                 return True
            
#             return False

#         resultList = []
#         intervals = sorted(intervals, key =  lambda s: s[0])
#         for interval in intervals:
#             if not resultList:
#                 resultList.append(interval)
#             else:
#                 find_brother = False
#                 for i in range(0,len(resultList)):
#                     if are_two_intervals_intersectable(resultList[i],interval):
#                         find_brother =True
#                         resultList[i][0] = min(interval[0],resultList[i][0])
#                         resultList[i][1] = max(interval[1],resultList[i][1])
#                 if not find_brother:
#                     resultList.append(interval)

#         return resultList

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if intervals == []:
            return []
        elif len(intervals) ==1 :
            return intervals

        def are_two_intervals_intersectable(int1,int2):
            if int2[0] <= int1[1] and int2[1] >= int1[1]:
                return True
            
            if int1[0] <= int2[1] and int1[1] >= int2[1]:
                return True
            
            return False

        def get_sol(intervals):
            resultList = []
            intervals = sorted(intervals, key =  lambda s: (s[0], s[1]) )
            low_index = []
            upper_index = []
            for interval in intervals:
                low_index.append(interval[0])
                upper_index.append(interval[1])
            
            maxi = -1
            i = 0
            current_i = 0
            current_interval = []
            while i < len(intervals) - 1 :
                if len(resultList) > 0 and low_index[i] == resultList[-1][1] and low_index[i] == upper_index[i]:
                    i+=1
                else:
                    if maxi == low_index[i]:
                        current_interval=[resultList[-1][0]]
                        resultList.pop()
                    else:
                        current_interval = [low_index[i]]
                    
                    if upper_index[i] > maxi:
                        maxi = upper_index[i]
                    current_i = i
                    while i < len(intervals)-1 and  upper_index[current_i] >= low_index[i+1] :
                        if upper_index[i+1] > maxi:
                            maxi = upper_index[i+1]
                        i+=1

                    current_interval.append(maxi)

                    resultList.append(current_interval)

                    i+=1            

            if are_two_intervals_intersectable(intervals[-1],resultList[-1]):
                resultList[-1][0] = intervals[-1][0] if intervals[-1][0] <  resultList[-1][0] else resultList[-1][0] 
                resultList[-1][1] = max(intervals[-1][1],resultList[-1][1])
            else:
                resultList.append(intervals[-1])

            return resultList

        if len(intervals) > 5:
            return get_sol(intervals=get_sol(intervals=intervals))
        else:
            return get_sol(intervals=intervals)
s = Solution()
print(s.merge(intervals=[[1,4],[4,5]]))