# In this program we gonna see about string operations.

# strings are immutable i.e., any operation will not change the string
name = ",.,,Bhanu,,.,,,,"

# This will print the length of the string
print(len(name))

# This will convert name into upper case
print(name.upper())

# This will convert name into lower case
print(name.lower())

# This will strip the string This will remove only trailing character and wont remove starting.
print(name.rstrip(","))

# This will replace the occurance of the particular character set in string
print(name.replace("Bhanu","Prasad"))

# This will split name in list
print(name.split("."))

heading = "thIs is PyThon coURse"

# Capatalize will convert first letter of string to cpaital and remailing all to lower
print(heading.capitalize())

# center will center the string with the specified space characters
print(heading.center(30))

# count function will give number of times the word is repeated
print(heading.count("is"))

# This will return true if string ends with provided characters or word.
print(name.endswith(",,,"))

# This will return true if string starts with provided characters or word.
print(name.startswith(",."))

# This will swap the cases i.e., lower cast to upper case and viceversa`
print(heading.swapcase())
