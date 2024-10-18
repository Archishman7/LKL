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
