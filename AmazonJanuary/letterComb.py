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

        if len(digits) == 1:
            for i in comb[digits[0]]:
                rez.append(i)
        if len(digits) == 2:
            for i in comb[digits[0]]:
                pString = i 
                for j in comb[digits[1]]:
                    pString += j
                    rez.append(pString)
                    pString =pString[:-1]
                pString=""
        elif len(digits) == 3:
            for i in comb[digits[0]]:
                pString = i 
                for j in comb[digits[1]]:
                    pString += j
                    for k in comb[digits[2]]:
                        pString += k
                        rez.append(pString)
                        pString =pString[:-1]
                    pString =pString[:-1]
                pString=""
        elif len(digits) == 4:
            for i in comb[digits[0]]:
                pString = i 
                for j in comb[digits[1]]:
                    pString += j
                    for k in comb[digits[2]]:
                        pString += k
                        for l in comb[digits[3]]:
                            pString += l
                            rez.append(pString)
                            pString = pString[:-1]
                        pString =pString[:-1]
                    pString =pString[:-1]
                pString=""
        

        return rez 

s = Solution()
print(s.letterCombinations("5678"))