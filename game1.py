import random
import time
usererrorloop = True
aichoice = random.randint (1,3)
lives = 3
score = 0
while lives > 0:
    while usererrorloop == True:
        userchoice = input('Choose: 1 for Scissors, 2 for Paper, 3 for Stone')
        try:
            userchoice = int(userchoice)
            if userchoice == int:
                usererrorloop = False
        except ValueError:
            print ('Please input a number.')
    if aichoice == 1:
        print ('The ai has chosen scissors')
    elif aichoice == 2:
        print ('The ai has chosen paper')
    else:
        print ('The ai has chosen stone')
    if userchoice == 1:
        if aichoice == 1:
            print ('You have drawn with the ai')
        if aichoice == 2:
            print ('You have won the ai')
            score = score + 1
        if aichoice == 3:
            print ('You have lost to the ai')
            lives = lives - 1
    elif userchoice == 2:
        if aichoice == 1:
            print ('You have lost to the ai')
            lives = lives - 1
        if aichoice == 2:
            print ('You have drawn with the ai')
        if aichoice == 3:
            print ('You have won the ai')
            score = score + 1
    elif userchoice == 3:
        if aichoice == 1:
            print ('You have won the ai')
            score = score + 1
        if aichoice == 2:
            print ('You have lost to the ai')
        if aichoice == 3:
            lives = lives - 1
            print ('You have drawn with the ai')
    print ('You have '+score+ ' amount of points currently.')
print ('Game over!')
if score > 15:
    print ('Amazing! Not a lot of people reached the amount of points you have')
elif score > 5:
    print ('Not bad at all! You are above average!')
else:
    print ("It's ok! Try harder next time!")