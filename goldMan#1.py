fiboNumbers = []
memo = {}
def fiborecursion(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    elif  number not in memo.keys():
        memo[number] = fiborecursion(number-1) + fiborecursion(number-2)    
    return memo[number]

def iterativeFibo(n):
    a = 0
    b = 1
    c = None 
    for i in range(n-1):
        c = a+b
        a = b 
        b = c

    return c
        
