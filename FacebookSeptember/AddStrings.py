class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        length_one = len(num1) -1 
        length_two = len(num2) -1
        rez = ""
        transport = 0
        while(length_one != -1 and length_two != -1 ):
            rez = str( (int(num1[length_one]) + int(num2[length_two]) + transport )%10  ) + rez  
            transport = ( int(num1[length_one]) + int(num2[length_two]) + transport ) // 10
            length_one -= 1
            length_two -= 1
        
        
        while(length_one != -1 ):
            rez = str( (int(num1[length_one]) + transport )%10  ) + rez
            transport =  int(str((int(num1[length_one]))%10 + transport ))   // 10
            length_one -= 1
     

        while(length_two != -1 ):
            rez = str( (int(num2[length_two]) + transport  )%10   ) + rez
            transport =  int(str((int(num2[length_two]))%10 + transport ))   // 10
            length_two -= 1

         
        if transport != 0:
            rez = str(transport) + rez

        
        
        return rez

s = Solution()
print(s.addStrings("584","18"))