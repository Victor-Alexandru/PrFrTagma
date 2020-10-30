class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s :
            return 0
        

        def expand(let,index):
            i = index - 1
            j = index + 1
            isPalindrome = True
            word = let
            while ( i >= 0 and j < len(s) and isPalindrome):
                if s[i] == s[j]:
                    word = s[i]+word+s[j]
                else:
                    isPalindrome = False
                i -= 1
                j += 1

            return word
        def expand_right(let,index):
            i = index 
            j = index + 1
            isPalindrome = True
            word = ''
            while ( i >= 0 and j < len(s) and isPalindrome):
                if s[i] == s[j]:
                    word = s[i]+word+s[j]
                else:
                    isPalindrome = False
                i -= 1
                j += 1

            return word

        if len(s) == 1:
            return s
        if len(s)==2: 
            return s if s[0] == s[1] else s[0]
        
        def isPalindrome(s):
            return len(set(s)) == len(s)


        for i,let in enumerate(s):
            if i == len(s)-1:
                continue

            if i == 0:
                word_two = expand_right(let,i)
                if len(word_two) > len(longestPal):
                    longestPal = word_two
                continue

            word = expand(let,i)
            word_two = expand_right(let,i)


            if len(word) > len(longestPal):
                longestPal = word

            if len(word_two) > len(longestPal):
                longestPal = word_two


        return longestPal

        

s = Solution()
s.lengthOfLongestSubstring('bbbb')