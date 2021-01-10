class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        open_brackets = ["{","[","("]
        closed_brackets = {"}":"{","]":"[",")":"("}
        my_stack = [ ]
        for char in s:
            if char in open_brackets:
                my_stack.append(char)
            else:
                if len(my_stack)<=0:
                    return False
                
                elem = my_stack.pop()
                
                if elem != closed_brackets[char]:
                    return False
                    


        

        if len(my_stack) == 0:
            return True
        

        return False
#10min