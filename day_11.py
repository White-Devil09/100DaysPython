name = "Bhanu" # this is a string

name2 = 'prasad' # this is also a string

long_string = '''we can write
multi line string
with three quote'''

print(name)
print(name2)
print(long_string)

print(name[0]) # This will print first character of name
print(name[0:3]) # This will print first 3 characters of name
print(long_string[0::2]) # This will print whole long string with 2 character skip
print(long_string[-1]) # This will print last character of the long string

# By using for loop
for character in name:
    print(character)
