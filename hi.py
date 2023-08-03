import random

MOBILIZATION_POLICY = {
    "LOW": 0,
    "MEDIUM": 1,
    "HIGH": 2
}

class Province:
    def __init__(self, terrain_type):
        self.terrain_type = terrain_type
        self.owner = None
        self.victory_points = random.randint(1, 5)

class MilitaryFactory:
    def __init__(self):
        self.equipment_production = {}

class Dockyard:
    def __init__(self):
        self.ship_production = {}

class Team:
    def __init__(self, name, atk, team_atk):
        self.name = name
        self.atk = atk
        self.team_atk = team_atk
        self.civilian_factories = 10
        self.policy_mobilization = MOBILIZATION_POLICY["LOW"]
        self.provinces = []
        self.alliance = []

    def spy_on(self, other_team):
        print(f"{self.name}'s spies gathered intelligence on {other_team.name}!")
        if other_team.team_atk > self.team_atk:
            self.atk -= 5
            print(f"{self.name}'s morale decreased due to intelligence gathered!")

    def diplomacy_phase(self, teams):
        for team in teams:
            for other_team in teams:
                if team != other_team:
                    if len(team.provinces) >= 1 and len(other_team.provinces) >= 1:
                        alliance_chance = random.random()
                        if alliance_chance > 0.5:
                            print(f"{team.name} and {other_team.name} formed an alliance!")
                            team.alliance.append(other_team)
                            other_team.alliance.append(team)

    def espionage_phase(self, teams):
        for team in teams:
            for other_team in teams:
                if team != other_team:
                    if len(team.provinces) >= 1 and len(other_team.provinces) >= 1:
                        espionage_chance = random.random()
                        if espionage_chance > 0.7:
                            print(f"{team.name} sent spies to gather intelligence from {other_team.name}!")
                            team.spy_on(other_team)

def combat(attacker, defender, province):
    attacker_strength = attacker.team_atk
    defender_strength = defender.team_atk
    if attacker_strength > defender_strength:
        print(f"{attacker.name} won the battle against {defender.name} in {province.terrain_type}!")
        return True
    else:
        print(f"{defender.name} defended successfully against {attacker.name} in {province.terrain_type}!")
        return False

def production_phase(teams):
    for team in teams:
        for factory in team.military_factories:
            equipment_type = random.choice(["Tank", "Artillery", "Infantry"])
            production_quantity = random.randint(1, 10)
            if equipment_type in factory.equipment_production:
                factory.equipment_production[equipment_type] += production_quantity
            else:
                factory.equipment_production[equipment_type] = production_quantity

        for dockyard in team.dockyards:
            ship_type = random.choice(["Destroyer", "Cruiser", "Battleship"])
            production_quantity = random.randint(1, 5)
            if ship_type in dockyard.ship_production:
                dockyard.ship_production[ship_type] += production_quantity
            else:
                dockyard.ship_production[ship_type] = production_quantity

        if team.policy_mobilization == MOBILIZATION_POLICY["HIGH"]:
            team.civilian_factories -= 2
            team.military_factories.append(MilitaryFactory())

def player_interaction(team):
    print(f"It's {team.name}'s turn.")
    print("What do you want to do?")
    print("1. Train Divisions")
    print("2. Build Ships")
    print("3. Adjust Policies")
    choice = int(input("Enter the corresponding number: "))

    if choice == 1:
        divisions_trained = random.randint(1, 3)
        team.atk += divisions_trained
        print(f"{team.name} trained {divisions_trained} divisions. Their attack power is now {team.atk}.")
    elif choice == 2:
        ships_built = random.randint(1, 2)
        # Assuming the team has at least one dockyard
        team.dockyards[0].ship_production["Destroyer"] += ships_built
        print(f"{team.name} built {ships_built} Destroyers.")
    elif choice == 3:
        print("Choose a policy:")
        for policy_name, policy_value in MOBILIZATION_POLICY.items():
            print(f"{policy_value}. {policy_name}")
        policy_choice = int(input("Enter the corresponding number: "))
        if policy_choice in MOBILIZATION_POLICY.values():
            team.policy_mobilization = policy_choice
            print(f"{team.name}'s mobilization policy is now set to {policy_choice}.")
        else:
            print("Invalid policy choice. No changes were made.")

def check_victory(teams):
    for team in teams:
        if len(team.provinces) == 0:
            print(f"{team.name} wins the game!")
            return True
    return False

def main():
    team1 = Team("Joshua's Team", 29, 7)
    team2 = Team("K Pop's Team", 32, 6)
    team3 = Team("Creator's Team", 23, 10)
    team4 = Team("Class 1C Team", 37, 5)

    team1.provinces = [Province("Plains"), Province("Mountains")]
    team2.provinces = [Province("Forest")]
    team3.provinces = [Province("Desert")]
    team4.provinces = [Province("Island")]

    team1.military_factories = [MilitaryFactory()]
    team2.military_factories = [MilitaryFactory()]
    team3.military_factories = [MilitaryFactory()]
    team4.military_factories = [MilitaryFactory()]

    team1.dockyards = [Dockyard()]
    team2.dockyards = [Dockyard()]
    team3.dockyards = [Dockyard()]
    team4.dockyards = [Dockyard()]

    teams = [team1, team2, team3, team4]

    TEAM_ATTACK_FACTOR = 7
    user_team = TEAM_ATTACK_FACTOR
    atk_loop = True

    while not check_victory(teams) and user_team > 0:
        print(f"Your attack power: {user_team}")
        atk_who = int(input("Choose who to attack. 1 for Joshua, 2 for K Pop, 3 for Creator, and 4 for Class 1C Team: "))
        try:
            if atk_who in [1, 2, 3, 4]:
                defense = random.randint(1, 6) * teams[atk_who - 1].team_atk
                if user_team > defense:
                    user_team += 1
                    print('Welp, one attack in!')
                    teams[atk_who - 1].atk -= 1
                else:
                    user_team -= 1
                    print('Oopsie, you lost a player')
                    teams[atk_who - 1].atk += 1
            else:
                print('Please type a valid choice')
        except ValueError:
            print('Please type a valid choice')
        except IndexError:
            print('Team not found.')

if __name__ == "__main__":
    main()
