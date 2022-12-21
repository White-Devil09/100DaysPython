# In this program we will look about function defalut arguments

def myavg(a=11,b=4):
    print(f"The average is : {(a+b)/2}")

# This line will print myavg func with the given arguments
myavg(12,44)

# This line will dont take any arguments but prints average with default values
myavg()

# The following function will take dynamic arguments and returns avg
def soavg(*numbers):
    print(type(numbers))
    s = 0
    for i in numbers:
        s += i
    print(f"The average of given numbers is : {s/len(numbers)}")

soavg(1,2,3,4)
