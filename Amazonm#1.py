def generalizedGCD(num, arr):
    # WRITE YOUR CODE HERE
    def computeGCD(x, y): 
        while(y): 
            x, y = y, x % y 
        
        return x 
    if not arr:
        return 0 
    if len(arr) == 1:
        return arr[0]
    
    if len(arr) == 2:
        return computeGCD(arr[0],arr[1])
    
    return_value = 1
    
    for i in range(0,num-1):
        return_value = computeGCD(arr[i],arr[i+1])
    
    return return_value

print(generalizedGCD(arr = [13,17,2],num=5))



