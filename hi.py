import random
import time
def user():
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
def offense():
    user_atk = random.radint (1,6) * team_atk
atk = "atk_who = int(input('Choose who to attack. 1. for Joshua, 2 for K_pop, 3 for creator, and 4 for 1C team'))"
atk_loop = True
offense_who = """while atk_loop == True:
    if atk_who  == 1:
        def defense():
            defense = random.radint (1,6) * j_team_atk
            atk_loop = False
    elif atk_who == 2:
        def defense():
            defense = random.radint (1,6) * k_team_atk
            atk_loop = False
    elif atk_who == 3:
        def defense():
            defense = random.radint (1,6) * c_team_atk
            atk_loop = False
    elif atk_who == 4:
        def defense():
            defense = random.radint (1,6) * c1c_team_atk
            atk_loop = False
    elif ValueError:
        print('Please type a number instead')
    else:
        print('Please type a valid choice')"""
quit = False
while quit == False:
    user()
    offense()
    exec (atk)
    time.sleep (5)
    exec (offense_who)
    if user_atk > defense:
        user_team = user_team + 1
        if atk_who  == 1:
            joshua_team = joshua_team - 1
        elif atk_who == 2:
            kpop_team = kpop_team - 1
        elif atk_who == 3:
            creator_team = creator_team - 1
        elif atk_who == 4:
            class1c_team = class1c_team - 1
    else:
        user_team = user_team - 1
        if atk_who  == 1:
            joshua_team = joshua_team + 1
        elif atk_who == 2:
            kpop_team = kpop_team + 1
        elif atk_who == 3:
            creator_team = creator_team + 1
        elif atk_who == 4:
            class1c_team = class1c_team + 1
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
    if joshua_team == 0 and kpop_team == 0 and creator_team == 0 and class1c_team == 0:
        print ('Amazing! You win!')
        break