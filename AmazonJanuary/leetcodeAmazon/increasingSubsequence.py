class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        sorted_nums = sorted(nums)

        max_length = 1
        max_var = 1
        for i in range(1,len(sorted_nums)):
            if nums[i-1]