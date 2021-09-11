class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        numbers_stack = []
        operations_stack = []
        operations_stack.append("+")
        s = s.replace(" ","")
        for char in s:
            if char.isdigit() == True:
                numbers_stack.append(int(char))
                if len(operations_stack) and (operations_stack[-1] == "*" or operations_stack[-1] == "/"):
                    elem1 = numbers_stack.pop()
                    elem2 = numbers_stack.pop()
                    if operations_stack[-1] == "*":
                        numbers_stack.append(elem1*elem2)
                    else:
                        numbers_stack.append(elem2//elem1)
                    operations_stack.pop()
            else:
                operations_stack.append(char)
        result = 0
        while len(operations_stack):
            sign = operations_stack[-1]    
            sign_prod = -1 if sign == "-" else 1
            operations_stack.pop()
            elem1 = numbers_stack.pop()
            result += elem1*sign_prod
        return result

s = Solution()
print(s.calculate("3+5 / 2 "))