class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = (len(nums) * (len(nums)+1)) /2
        for number in nums:
            sum = sum -  number
        
        return sum