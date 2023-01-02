# Tuples are immutable
# We can't directly manuplate tuples but we can manupulate them by converting them into list

lang = ('Telugu','Hindi','English')
print(lang)
temp = list(lang)
temp.pop(1)
temp.append("Urdu")
lang = tuple(temp)
print(lang)

# combination or concatination of two tuples is also a tuple

state = ('Telangana','Andhra pradesh','Tamil nadu', 'Karnataka')

combined = state + lang
print(combined)

tup1 = (0,1,2,1,2,1,3,4,5,1)
cont = tup1.count(1)
print(cont) # This will print the number of occurance of 1 in tup1

print(tup1.index(2)) # this will print the first occurance index of 2
print(len(tup1)) # This prints the length of the tuple
