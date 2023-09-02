import random
import time
usererrorloop = True
lives = 3
score = 0
while lives > 0:
    while usererrorloop == True:
        aichoice = random.randint (1,3)
        try:
            userchoice = int(input('Choose: 1 for Scissors, 2 for Paper, 3 for Stone'))
            if userchoice == 1:
                usererrorloop = False 
            elif userchoice == 2:
                usererrorloop = False
            elif userchoice == 3:
                usererrorloop = False
            else:
                print ('Hey, I know you want to joke around, but please,1,2,or 3.')
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
            lives = lives - 1
        if aichoice == 3:
            print ('You have drawn with the ai')
    if score == 0:
        print ('You have no points currently.')
    elif score == 1:
            print ('You have '+str(score)+ ' point currently.')
    else:
            print ('You have '+str(score)+ ' points currently.')
    print ('You have '+str(lives)+' lives left.')
    usererrorloop = True
print ('Game over!')
if score > 15:
    print ('Amazing! Not a lot of people reached the amount of points you have')
elif score > 5:
    print ('Not bad at all! You are above average!')
else:
    print ("It's ok! Try harder next time!")