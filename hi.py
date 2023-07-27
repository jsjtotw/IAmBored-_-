import random
import time
user_team = 5
team_atk = 4
if user_team > 84:
    team_atk = 8
elif user_team >  64:
    team_atk = 7
elif user_team > 44:
    team_atk = 6
elif user_team > 24:
    team_atk = 5
joshua_team = 29
j_team_atk = 7
kpop_team = 32
k_team_atk = 6
creator_team = 23
c_team_atk = 10
class1c_team = 37
c1c_team_atk = 5
atk_loop = True
offense_who = """while atk_loop == True:
    atk_who = int(input('Choose who to attack. 1. for Joshua, 2 for K_pop, 3 for creator, and 4 for 1C team'))
    time.sleep(5)
    try:
        if atk_who  == 1:
            defense = random.randint (1,6) * j_team_atk
            atk_loop = False
        elif atk_who == 2:
            defense = random.randint (1,6) * k_team_atk
            atk_loop = False
        elif atk_who == 3:
            defense = random.randint (1,6) * c_team_atk
            atk_loop = False
        elif atk_who == 4:
            defense = random.randint (1,6) * c1c_team_atk
            atk_loop = False
        else:
            print('Please type a valid choice')
    except ValueError:
        print('Please type a valid choice')
    except NameError:
        print('Like I said, do not choose it again')"""
quit = False
while quit == False:
    user_atk = random.randint (1,6) * team_atk
    exec (offense_who)
    if user_atk > defense:
        user_team = user_team + 1
        print('Welp, one attack in!')
        if atk_who  == 1:
            joshua_team -= 1
        elif atk_who == 2:
            kpop_team -= 1
        elif atk_who == 3:
            creator_team -= 1
        elif atk_who == 4:
            class1c_team -= 1
    else:
        user_team = user_team - 1
        print('Oopsie, you lost a player')
        if atk_who  == 1:
            joshua_team += 1
        elif atk_who == 2:
            kpop_team += 1
        elif atk_who == 3:
            creator_team += 1
        elif atk_who == 4:
            class1c_team += 1
    if user_team == 0:
        print ('Game Over')
        break
    if joshua_team == 0 or kpop_team == 0 or creator_team == 0 or class1c_team == 0:
        print ('Nice! You defeated a team!')
        if joshua_team == 0:
            print("Joshua's team has died. Do not choose it again.")
            del joshua_team
            del j_team_atk
        elif kpop_team == 0:
            print("K pop's team has died. Do not choose it again.")
            del kpop_team
            del k_team_atk
        elif creator_team == 0:
            print("Insta-win!!! You destroyed the creator's team.")
            break
        elif class1c_team == 0:
            print("You killed the class! Do not choose it, though.")
            del class1c_team
            del c1c_team_atk
    try:
        if joshua_team == 0 and kpop_team == 0 and class1c_team == 0:
            print ('Amazing! You win!')
            break
    except NameError:
        #Idk what to put here someone put a pull request please.l