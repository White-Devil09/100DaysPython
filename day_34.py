ep1 = { 122 : 45, 123 : 89, 567: 69}
ep2 = { 222: 67, 566: 90}

# This will update ep1 with values of ep2 at the end
ep1.update(ep2)
print(ep1)
# This will clear the dictionary
ep2.clear()
print(ep2)
# This will delete key value pair
del ep1[122]
print(ep1)
# This will delete the entire dictionart
del ep2
# This will throw error as ep2 is deleted
# print(ep2)
