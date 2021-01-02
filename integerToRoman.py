class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        rez = ""
        roman_dict_rules = {
            900:"CM",
            500:"D",
            400:"CD",
            90:"XC",
            50:"L",
            40:"XL",
            9:"IX",
            8:"VIII",
            7:"VII",
            6:"VI",
            5:"V",
            4:"IV",
            3:"III",
            2:"II",
            1:"I",
            0:"",
        }
        ord = 1
        while num > 0 :
            uc = num % 10
            if ord == 1:
                rez += roman_dict_rules[uc]
            if ord  == 10:
                if uc == 4 or uc == 9 or uc == 5:
                    rez = roman_dict_rules[uc*ord] + rez
                elif uc < 4:
                    for i in range(uc):
                        rez ="X" + rez
                elif uc >5:
                    pString = "L" 
                    for i in range(uc-5):
                        pString = pString + "X"
                    rez = pString + rez
            if ord  == 100:
                if uc == 4 or uc == 9 or uc == 5:
                    rez = roman_dict_rules[uc*ord] + rez
                elif uc < 4:
                    for i in range(uc):
                        rez ="C"+ rez
                elif uc >5:
                    pString = "D"
                    for i in range(uc-5):
                        pString = pString + "C"
                    rez = pString + rez
            if ord  == 1000:
                for i in range(uc):
                    rez ="M" + rez


            ord = ord*10
            num = num //10


        return rez

s = Solution()
print(s.intToRoman(61))

#GREEDY
# class Solution(object):
#     digits = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), 
#           (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]

#     def intToRoman(self, num: int) -> str:
#         roman_digits = []
#         # Loop through each symbol.
#         for value, symbol in digits:
#             # We don't want to continue looping if we're done.
#             if num == 0: break
#             count, num = divmod(num, value)
#             # Append "count" copies of "symbol" to roman_digits.
#             roman_digits.append(symbol * count)
#         return "".join(roman_digits)