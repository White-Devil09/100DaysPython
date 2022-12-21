import time

timestamp = time.strftime('%I:%M:%S %P')
hour = int(time.strftime('%H')) 

if(hour<12):
    print("Good morning sir!")
    print(f'The time is {timestamp}')
elif(hour>=12 and hour<4):
    print("Good afternoon sir!")
    print(f'The time is {timestamp}')
elif(hour>=4 and hour<8):
    print("Good evening sir!")
    print(f'The time is {timestamp}')
else:
    print("Good night sir!")
    print(f'The time is {timestamp}')

