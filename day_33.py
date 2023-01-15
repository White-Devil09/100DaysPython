# In this programm we will look about the dictionaries in python

dic = {
        "Bhanu" : "student",
        "Harry" : "instructor"
        }

# This will print the value of Harry
# This will throw error if Harry is not present in dictionary
print(dic["Harry"])
# This will not throw error even if Harry is not present in dictionary
print(dic.get("Harry"))
# This will print all keys 
print(dic.keys())
# This will print all values 
print(dic.values())
# This will print the key value pairs 
print(dic.items())
