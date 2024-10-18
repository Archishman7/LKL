k=1
def factorial(n):
    global k
    k=k*n
    print('done',k)
    if n==1:
        print(k)
        return k
    else :
        
        factorial(n-1)

m=factorial(6)
print(m)
#I request the assistance of fellow Github members. Please help me figure out the issue 
#The function works well when I request it to PRINT the value of the factorial.
#But for some reason the value of variable k is not RETURNED by the function.
#Please help me find out the cause and solution.
