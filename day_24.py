# In this programm we will look about tuples (tuples are immutable datatype)

tup = (1,2,3)
print(type(tup),tup)

tup1 = (1) # it is mandatory to put a comma if you are creating a tuple of size 1
tup2 = (1,)
print(type(tup1),tup1)
print(type(tup2),tup2)

# tup[0] = 22 # This will throw error since tuples are immutable datatype 

for item in tup:
    print(item)

print(tup)
