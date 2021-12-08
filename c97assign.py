# guessing game

import random
guess=(random.randint(1,9))
number=int(input('enter your number:'))
chance=4

while (chance>=0):
    
    if chance>0:
        if guess==number:
            print("Congratulations!you won")
            break
        elif guess>number:
            print('your number is too small')
            number=int(input('enter your number:'))
            chance=chance-1
        else:
            print('your number is too big')
            number=int(input('enter your number:'))
            chance=chance-1
    elif chance==0 and guess!= number:
        print('you lose the number was',guess)
        break