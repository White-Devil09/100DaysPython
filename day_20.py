# In this programm we will look about the fucntion

# The below function will return the sum of two numbers
def mysum(a,b):
    return a+b

# The below function will return maximum of two numbers
def mymax(c,d):
    if(c>d):
        return c
    else :
        return d

# Now we will look about pass functionality
# if we don't write pass inside demopass it will throw an error
def demopass():
    pass

c = mysum(4,5)
m = mymax(8,99)
demopass()
print(c)
print(m)
