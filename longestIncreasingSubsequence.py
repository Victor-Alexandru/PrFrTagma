# public class Solution {
#     public int lengthOfLIS(int[] nums) {
#         if (nums.length == 0) {
#             return 0;
#         }
#         int[] dp = new int[nums.length];
#         dp[0] = 1;
#         int maxans = 1;
#         for (int i = 1; i < dp.length; i++) {
#             int maxval = 0;
#             for (int j = 0; j < i; j++) {
#                 if (nums[i] > nums[j]) {
#                     maxval = Math.max(maxval, dp[j]);
#                 }
#             }
#             dp[i] = maxval + 1;
#             maxans = Math.max(maxans, dp[i]);
#         }
#         return maxans;
#     }
# }

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        dp = []
        
        for i in range(len(nums)):
            dp.append(0)

        for i in range(0,len(dp)):
            maxval= 0
            for j in range(0,i):
                if (nums[i]>nums[j]):
                    maxval = max(maxval,dp[j])
            dp[i] = maxval + 1


        return max(dp)


s = Solution()
print(s.lengthOfLIS([10,9,2,5,3,7,101,18]))