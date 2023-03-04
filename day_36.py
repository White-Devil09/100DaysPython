# In this programm we will look at exception handling

try:
    a = int(input("Enter the number : "))
    print(f"Multiplication table of {a} is :")

    for i in range(1,11):
        print(f"{a} X {i} = {a*i}")
except :
    print('invalid input')

# Even if error occur in the above try except error the programm will not terminate the below lines will run normally
print("end of python programm")
