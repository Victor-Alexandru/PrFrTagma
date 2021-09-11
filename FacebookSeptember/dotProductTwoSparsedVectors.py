class SparseVector:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums    

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec):
        """
        :type vec: 'SparseVector'
        :rtype: int
        """
        sum = 0 
        for i in range(len(self.nums)):
            sum+= self.nums[i]*vec.nums[i]            
        
        return sum

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)