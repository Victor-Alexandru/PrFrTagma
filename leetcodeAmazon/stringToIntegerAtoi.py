class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        min_int = -2147483648
        max_int = 2147483647

        i = 0 
        while  i!=len(s) and s[i] == " " :
            i+=1
        sign = 1
        if  i!=len(s) and (s[i] == "+" or s[i] == "-") :
            if s[i] == "-":sign=-1
            i+=1

        current_number = 0

        while i!= len(s) and s[i].isdigit():
            current_number = current_number*10 + int(s[i])
            i+=1

        current_number = current_number * sign

        if current_number > max_int:
            current_number = max_int
        elif current_number <min_int:
            current_number = min_int

        return current_number

        
s = Solution()
print(s.myAtoi(s="4193 with words"))

#21 minutes