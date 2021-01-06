class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        comb = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz",
        }


        rez = []
        if digits == "":
            return []

        def generate_solutions(s,computed=''):
            if len(s) == 0:
                rez.append(computed)
            else:
                for char in comb[s[0]]:
                    computed +=char
                    generate_solutions(s[1:],computed) 
                    computed = computed[0:len(computed)-1]

        generate_solutions(digits)
        return rez 


s = Solution()
print(s.letterCombinations(digits="23"))

#12min