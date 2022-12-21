# Making a calculator
a = int(input("Enter the first number: "))

print('+ - * / // % **')
c = input("Enter the operation to be performed : ")

b = int(input("Enter the second number: "))
match(c):
    case '+'  : ans = a+b
    case '-'  : ans = a-b
    case '*'  : ans = a*b
    case '/'  : ans = a/b
    case '//' : ans = a//b
    case '%'  : ans = a%b
    case '**' : ans = a**b

print(f'The result of the operation is {ans}')
