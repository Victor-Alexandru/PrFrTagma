class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return s

        def expand_odd(start,end):
            maxi = 1
            while(start >= 0 and end < n ):
                if s[start] == s[end]:
                    maxi+=2
                else:
                    break
                start = start -1 
                end+=1

            if(maxi == 1):
                return s[start+1]

            return s[start+1:end]

        def expand_even(start,end):
            if  (start >= 0 and end < n ) and  (s[start] == s[end]):
                start = start -1 
                end+=1
            else:
                return ""

            maxi = 2

            while(start >= 0 and end < n ):
                if s[start] == s[end]:
                    maxi+=2
                else:
                    break
                start = start -1 
                end+=1



            return s[start+1:end]

        max_palindrom = ""
        for index in range(len(s)):
            palind = expand_odd(index-1,index+1)
            palind_tow = expand_even(index,index+1)


            if len(palind) > len(max_palindrom):
                max_palindrom = palind
            
            if len(palind_tow) > len(max_palindrom):
                max_palindrom = palind_tow

        return max_palindrom

s = Solution()
print(s.longestPalindrome("cbbaddcabaabaddcb"))