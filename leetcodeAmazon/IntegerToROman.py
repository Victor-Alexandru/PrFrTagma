class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman_values = [ "M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        integer_values = [1000,900,500,400,100,90,50,40,10,9,5,4,1]

        result = ""
        
        l=0
        while l != len(integer_values):
            if num - integer_values[l] >= 0:
                num = num - integer_values[l]
                result += roman_values[l]
            else:
                l+=1

        return result
#O()