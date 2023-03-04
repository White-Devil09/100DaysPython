# In this programm we will look how to use else with for and while loops

for i in range(6):
    print(f"{i} ", end = '')
else:
    print(f"The value of i is now {i}")

# else will only be executed after sucessful termination of for loop
for j in range(6):
    if j ==4 :
        break
    print(f"{j} ", end = '')
else:
    print(f"The value of j is now {j}")

print()

# This wont execute else block as loop is breaked

# The same thing can be done with while loop
i = 3
while i < 8:
    print(f"{i} ", end = '')
    i += 1
else:
    print(f"The value of i is now {i}")


