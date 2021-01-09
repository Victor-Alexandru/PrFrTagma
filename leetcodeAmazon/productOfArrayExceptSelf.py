class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        left_part = []
        right_part = []
        temp = 1

        for number in nums:
            left_part.append(temp)
            temp = temp*number

        temp = 1
        
        for i in range(len(nums)-1,-1,-1):
            right_part.append(temp)
            temp = temp*nums[i]

        rez =[]

        for i in range(len(left_part)):
            rez.append(left_part[i]*right_part[len(right_part)-i-1])
        
        return rez