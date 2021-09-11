class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """       
        max_int = 1534236469
        min_int =-2143847412

        if x >= max_int or x < min_int:
            return 0
        if x == 0:
            return 0

        sign = 1 if x > 0 else -1  
        x = x* sign
        ogl = 0 

        while x > 0 :
            uc = x %10
            ogl = ogl*10 +uc
            x = x // 10
        
        return ogl if sign == 1 else -ogl