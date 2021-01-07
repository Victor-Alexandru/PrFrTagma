class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        char_count = {}
        merged_intervals = []

        for i in range(len(S)):
            if S[i] in char_count:
                char_count[S[i]][1] = i
            else:
                char_count[S[i]] = [i,i]

        for key in char_count.keys():
            merged_intervals.append(char_count[key])


        merged_intervals = sorted(merged_intervals,key=lambda x: x[0])

        result = []

        result.append(merged_intervals[0])
        for i in range(1,len(merged_intervals)):
            if merged_intervals[i][0] > result[-1][1] and merged_intervals[i][1] > result[-1][1]:
                result.append(merged_intervals[i])
            elif merged_intervals[i][1] > result[-1][1]:
                result[-1][1] = merged_intervals[i][1]


        for i in range(len(result)):
            result[i] = result[i][1] - result[i][0] +1 

        return result




s = Solution()
print(s.partitionLabels(S="ababcbacadefegdehijhklij"))

# 20 min O(n) time space O(1)