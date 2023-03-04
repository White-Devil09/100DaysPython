# In this programm we will look at try except and finally 

# finally will be executed even if function returned
def func():
    try:
        l = [1,2,3,4,5]
        i = int(input("Enter the index : "))
        print(l[i])
        return 1
    except:
        print("Some error occured")
        return 0
    finally:
        print("This will print irrespective of try or except")

x = func()
print(x)

# IF we dont use finally and make print statement out of try except then it wont get executed
