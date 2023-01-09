# In this programm me will look at the recurssion

def fibb(n):
    if(n==1 or n==2):
        return 1
    fib = fibb(n-1)+fibb(n-2)
    return fib

fib5 = fibb(5)
print(fib5)

# Fractorial of the number
def fact(n):
    if(n==0):
        return 1
    return n*fact(n-1)

print(fact(6))
