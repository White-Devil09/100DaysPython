# In this programm we wilstl look about list methods (lists are mutable datatype)

lst = [20-i for i in range(20) if i%2==0]

print(lst)
lst.append(100) # This will append 100 at the end of the list
print(lst)
lst.reverse() # This will reverse the list
print(lst)
lst.sort() # This will sort the list 
print(lst)
lst.sort(reverse = True) # This will sort the list but in reverse order
print(lst)
c = lst.count(16) # This will count the number of occurances of "16"
print(c)

# lstcpy = lst # This will make lstcpy as reference of lst

lstcpy = lst.copy()
lstcpy[0] = 12
print(lstcpy)

lstcpy.insert(2,134) # This will insert 134 at index 2
print(lstcpy)

ne = [12,32,53]
we = ne + lstcpy # This will create a new list which concatinates ne and lstcpy
print(we)

print(ne)
ne.extend(we) # This will modify ne
print(ne)
