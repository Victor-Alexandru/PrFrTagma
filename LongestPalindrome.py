# class Solution(object):
#     def longestPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         def isPalindrome(s):
#             return s == s[::-1]
        
#         if len(s) == 1:
#             return s
        
#         occurences = {}
#         for i,let in enumerate(s):
#             if let not in occurences.keys():
#                 occurences[let] = [i]
#             else:
#                 occurences[let].append(i)
#         longestPal = ''
#         print(occurences)
#         for key in occurences.keys():
#             if len(longestPal) == 0:
#                     longestPal = key
#             for i in range(0,len(occurences[key])-1):   
#                 for j in range(i,len(occurences[key])):            
#                    if isPalindrome(s[occurences[key][i]:occurences[key][j]+1]):
#                      if len(s[occurences[key][i]:occurences[key][j]+1]) > len(longestPal):
#                         longestPal = s[occurences[key][i]:occurences[key][j]+1]
        
#         return longestPal
                        

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longestPal = ''
        
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
            return s == s[::-1]

        if isPalindrome(s):
            return s

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
print(s.longestPalindrome(s='cbbd'))