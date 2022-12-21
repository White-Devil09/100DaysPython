# In this program we see if else elif 
age = int(input("Enter your age: "))

print(f'Your age is : {age}')

if(age>= 18 and age<=65):
    print("You can drive")
else:
    print("sorry you can't drive")

# In the following code we will look into if elif and else statement
money = int(input("Enter the amount you have : "))
while(money>0):
    if(money>=500):
        print("Let's go out and eat")
        money = money - 300
        print(f'amount left with you is {money}')
    elif(money<200):
        print("Go to nescafe canteen")
        money = money - 100
        if(money>0):
            print(f'amount left with you is {money}')
        else:
            print("You are left with balance of 0")
    else:
        print("Go to food court")
        money = money - 200
        print(f'amount left with you is {money}')
