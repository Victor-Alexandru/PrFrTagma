class Solution(object):
    def connectSticks(self, sticks):
        """
        :type sticks: List[int]
        :rtype: int
        """
        if len(sticks) == 1:
            return 0
        elif len(sticks) == 2:
            return sticks[1]+sticks[0]
        suml = 0
        prev_sum = 0
        while(len(sticks)!= 1):
            min_one = min(sticks)
            prev_sum += min_one
            sticks.remove(min_one)
            
            if len(sticks) == 1:
                suml += min_one + sticks[0] + prev_sum
                break

            min_two = min(sticks)
            prev_sum += min_two
            sticks.remove(min_two)

            print(min_one,min_two, sticks)
            suml = prev_sum + suml  

        return suml

s = Solution()
print(s.connectSticks(sticks=[1,8,3,5]))