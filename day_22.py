# In this programm we will look about lists

lst = ["AI" ,21 , "Bhanu", True]
print(len(lst))

for item in lst:
    print(item)

print(lst[2])

# We can use in keyword to find a particular item is present in list or not
if 15 in lst:
    print("Yes")
else: 
    print("No")

print(lst)

# In the following line we will look about list comprehension

lst1 = [i for i in range(10)]
lst2 = [i*i for i in range(20) if (i%2 == 0)]

print(lst1)
print(lst2)
