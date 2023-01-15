# In this programm we will look at set operations

s1 = {1,2,3,4,5,6}
s2 = {2,4,6,8,9,0}

# This line will update s1
# s1.update(s2)
# s2.intersection_update(s2)

# This line will print the union of s1 and s2
print(s1.union(s2))
# This line will print the intersection of s1 and s2
print(s1.intersection(s2))
# This line will print the symmetric difference of s1 and s2
print(s1.symmetric_difference(s2))
# This line will print the difference of s1 and s2
print(s1.difference(s2))
# This line will print is s1 and s2 are disjoint or not
print(s1.isdisjoint(s2))
# This line will print is s1 and s2 are superset or not
print(s1.issuperset(s2))
# This line will print is s1 and s2 are subset or not
print(s1.issubset(s2))
# To remove the items in sets use remove() or discard() method
# remove() throws error if element is not present in set whereas discard() will not throw any error
# pop removes random element from the set
# del is used to delete entire set whereas clear is used to delete the elements of the set
# del s1 # This will delete s1
# s2.clear() # This will clear the elements of s2
