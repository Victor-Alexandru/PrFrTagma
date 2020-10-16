class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        record = []

        for operand in ops:
            if operand == "+":
                record.append(record[-1]+record[-2])
            elif operand == "D":
                record.append(record[-1]*2)
            elif operand == "C":
                record.pop()
            else:
                record.append(int(operand))
                
        sum = 0
        for x in record:
            sum +=  x
        return sum

s=Solution()
print(s.calPoints( ["5","-2","4","C","D","9","+","+"]))