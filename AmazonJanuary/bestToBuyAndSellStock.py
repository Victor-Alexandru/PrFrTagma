class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_til_now =  9999
        profit = 0
        for number in prices:
            if number<min_til_now:
                min_til_now = number
            if number - min_til_now > profit:
                profit = number - min_til_now
        
        return profit

s = Solution()

print(s.maxProfit([7,1,5,3,6,4]))