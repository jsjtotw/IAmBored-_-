import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Define the screen size
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Create the game screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Team Battle Game")

# Font setup
font = pygame.font.Font(None, 36)

# Define game teams and attack values
user_team = 5
team_atk = 4
joshua_team = 29
j_team_atk = 7
kpop_team = 32
k_team_atk = 6
creator_team = 23
c_team_atk = 10
class1c_team = 37
c1c_team_atk = 5

def user():
    global user_team, team_atk
    if user_team > 84:
        team_atk = 8
    elif user_team > 64:
        team_atk = 7
    elif user_team > 44:
        team_atk = 6
    elif user_team > 24:
        team_atk = 5

def offense():
    global user_atk
    user_atk = random.randint(1, 6) * team_atk

def defense(atk_who):
    if atk_who == 1:
        return random.randint(1, 6) * j_team_atk
    elif atk_who == 2:
        return random.randint(1, 6) * k_team_atk
    elif atk_who == 3:
        return random.randint(1, 6) * c_team_atk
    elif atk_who == 4:
        return random.randint(1, 6) * c1c_team_atk

def display_teams():
    # Clear the screen
    screen.fill(WHITE)

    # Show game teams
    teams_text = f"Your Team: {user_team}\n\nJoshua's Team: {joshua_team}\nK pop's Team: {kpop_team}\nCreator's Team: {creator_team}\nClass Team: {class1c_team}"
    text_surface = font.render(teams_text, True, BLACK)
    screen.blit(text_surface, (30, 30))

    # Show attack instruction
    instruction_text = "Click on the team you want to attack."
    instruction_surface = font.render(instruction_text, True, BLACK)
    screen.blit(instruction_surface, (30, 400))

    # Update the display
    pygame.display.flip()

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get the position of the mouse click
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Check if the click is on any team box
            if 30 < mouse_x < 250 and 30 < mouse_y < 110:
                atk_who = 1
            elif 30 < mouse_x < 250 and 140 < mouse_y < 220:
                atk_who = 2
            elif 30 < mouse_x < 250 and 250 < mouse_y < 330:
                atk_who = 3
            elif 30 < mouse_x < 250 and 360 < mouse_y < 440:
                atk_who = 4
            else:
                continue

            # Execute offense and defense functions
            user()
            offense()
            defense_points = defense(atk_who)

            # Delay for a few seconds
            time.sleep(3)

            # Determine the outcome
            if user_atk > defense_points:
                user_team += 1
                if atk_who == 1:
                    joshua_team -= 1
                elif atk_who == 2:
                    kpop_team -= 1
                elif atk_who == 3:
                    creator_team -= 1
                elif atk_who == 4:
                    class1c_team -= 1
            else:
                user_team -= 1
                if atk_who == 1:
                    joshua_team += 1
                elif atk_who == 2:
                    kpop_team += 1
                elif atk_who == 3:
                    creator_team += 1
                elif atk_who == 4:
                    class1c_team += 1

            # Check if the game is over
            if user_team == 0:
                print('Game Over')
                pygame.quit()
                sys.exit()

            if joshua_team == 0 or kpop_team == 0 or creator_team == 0 or class1c_team == 0:
                print('Nice! You defeated a team!')
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
                    pygame.quit()
                    sys.exit()
                elif class1c_team == 0:
                    print("You killed the class! Do not choose it, though.")
                    del class1c_team
                    del c1c_team_atk

            if joshua_team == 0 and kpop_team == 0 and creator_team == 0 and class1c_team == 0:
                print('Amazing! You win!')
                pygame.quit()
                sys.exit()

            # Update the display
            display_teams()
    
    # Update the display
    display_teams()
