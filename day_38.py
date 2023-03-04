# In this programm we will look at custom error

a = int(input("Enter any number between 1 and 9 : "))

if(a<1 or a>9):
    raise ValueError("Value should be between 1 and 9") 
