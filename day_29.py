# In this python program we will see about docstring
# doc string must be defined next line of function def 
 
import this # This will print the stuff 

def square(n):
    '''Takes in a number n, and returns square of it'''
    return n**2

sqr = square(5)
print(sqr)
print(square.__doc__) # This line will print the docstring of the function
