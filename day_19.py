# In this program we will demostrate break and continue statement

for i in range(1,100):
    if( (i%10) == 0):
       continue 

    print(f'6 X {i} = {6*i}')

    if(i >= 15):
        break