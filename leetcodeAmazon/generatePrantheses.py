class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        results = []

        def is_simetric(item):
            contor = 0
            for char in item:
                if contor%2 == 0 and char!="(":
                    return False 
                if contor%2 == 1 and char!=")":
                    return False
                contor+=1

            return True

        def combine(lista):
            combined_list = []
            for item in lista:
                combined_list.append(item+"()")
                if not is_simetric(item):
                    combined_list.append("()"+item)
                combined_list.append("("+item+")")
            return combined_list


        for i in range(n+2):
            results.append([])
        
        results[1].append("()")

        for i in range(2,n+1):
            results[i] = combine(results[i-1])
             


        return sorted(results[n],reverse=True)
s = Solution()
print(s.generateParenthesis(4))

#31