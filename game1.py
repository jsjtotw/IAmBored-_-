import random
import time
usererrorloop = True
aichoice = random.randint (1,3)
lives = 3
score = 0
while lives > 0:
    while usererrorloop == True:
        try:
            userchoice = int(input('Choose: 1 for Scissors, 2 for Paper, 3 for Stone'))
            if userchoice == not 1 or not 2 or not 3:
                print ('1,2 or 3')
            else:
                userchoice
        except ValueError:
            print ('Please input a number.')
        if userchoice == int:
            usererrorloop = False
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
    if score == 0:
        print ('You have no points currently.')
    elif score == 1:
            print ('You have '+str(score)+ 'point currently.')
    else:
            print ('You have '+str(score)+ 'points currently.')
    usererrorloop = True
print ('Game over!')
if score > 15:
    print ('Amazing! Not a lot of people reached the amount of points you have')
elif score > 5:
    print ('Not bad at all! You are above average!')
else:
    print ("It's ok! Try harder next time!")