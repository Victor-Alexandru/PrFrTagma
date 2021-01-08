class Solution(object):
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        def changing_after_n_days(cell,n):
            for i in range(n):
                for j in range(0,len(cell)):
                    print(j)

                    if (j == 0 and cell[j] == 1) or (j == len(cell)-1 and cell[j] == 1) or (cell[j]==0 and (j==0 or j == len(cell)-1)):
                        cell[j] = "*"
                        continue
                    
                    elif cell[j-1] in ['#',0] and cell[j+1] in [0] and cell[j]==0:
                        cell[j] = "#"
                        
                    
                    elif cell[j-1] in ['*',1] and cell[j+1] in [1]  and cell[j]==0:
                        cell[j] = "#"
                    
                    elif   cell[j] == 1:
                        cell[j] = "*"
                
                print(cell)
                for j in range(0,len(cell)):
                    if cell[j]=="#":
                        cell[j] = 1
                    if cell[j]=="*":
                        cell[j] = 0

                print(cell)
                
            return cell


        return changing_after_n_days(cells,N)

# 29 numai futem capu