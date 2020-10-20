class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        def check_if_has_one_to_right_and_left(index,lista):
            has_to_part = False
            
            # [0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1]
            if index == 0:
                return False
            if index == len(lista) - 1:
                return False

            i = index - 1
            j = index + 1 
            while(i >= 0 ):
                if lista[i] == 1:
                    has_to_part = True
                    break
                i = i - 1

            if not has_to_part:
                return False                
            
            has_to_part = False

            while(j <= len(lista)-1 ):
                if lista[j] == 1:
                    has_to_part = True
                    break
                j = j + 1 

            if not has_to_part:
                return False
            
            return True
        if len(height) == 0:
            return 0
        if len(height) == 1:
            return 0
        matrix = []
        matrix_height = max(height)
        matrix_len = len(height) 
        elem = []
        

        for i in range(0,matrix_height):
            elem = []
            for j in range(0,matrix_len):
                if height[j]!=0 and height[j] > i:
                    elem.append(1)
                else:
                    elem.append(0)
            
            matrix.append(elem)

        print(mat)
        count = 0
        has_one_left = False
        has_one_right = False
        for i in range(0,matrix_height):
            for j in range(0,matrix_len):
                if has_one_left and matrix[i][j] == 1:
                    has_one_right = True 
                if matrix[i][j] == 1 and not has_one_left:
                    has_one_left = True

                if matrix[i][j] != 1 and has_one_left and has_one_right:
                    matrix[i][j]=2
                    count +=1
        return count
        


s = Solution()
print(s.trap(height=[4,2,0,3,2,5]))