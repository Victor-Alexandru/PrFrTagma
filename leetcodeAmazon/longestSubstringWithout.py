class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1    

        def check_array(values):
            for value in values:
                if value !=1 and value!=0:
                    return False
            return True

        def length(values):
            count = 0
            for value in values:
                if value == 1:
                    count+=1
            return count


        ascii_table_frequency = []
        #ord(letter) will be the ascii code
        for i in range(256):
            ascii_table_frequency.append(0)

        
        l = 0 
        e = 0
        maxi = -1        
        while e != len(s):

            ascii_table_frequency[ord(s[e])]+=1
            if ascii_table_frequency[ord(s[e])] == 2:
                while ascii_table_frequency[ord(s[e])] ==2:
                    ascii_table_frequency[ord(s[l])] = ascii_table_frequency[ord(s[l])] - 1
                    l+=1 
            
            if check_array(ascii_table_frequency):
                a = length(ascii_table_frequency)
                maxi = max(a,maxi)

            e+=1

        return maxi

s = Solution()
print(s.lengthOfLongestSubstring(s="abcabcbb"))


    
#32