class Solution:
    def maxSubArray(self, nums):
        curr_sum = -21389595
        max_sum = -22222222222222
        for number in nums:
            curr_sum = max(curr_sum+number,number)
            max_sum = max(max_sum,curr_sum)

        return max_sum

# 6 minutes 