#Cricket Team Management System Develop a Python application to maintain cricket player records. Requirements
#Create a Player class with:Player Name,Jersey Number,Runs
#Categorize players as:Excellent, Good, Average
#Create a Team class.
#Display all player details.

class Player:
    def __init__(self, name, jersey_number, runs):
        self.name = name
        self.jersey_number = jersey_number
        self.runs = runs

    def category(self):
        if self.runs >= 1000:
            return "Excellent"
        elif self.runs >= 500:
            return "Good"
        else:
            return "Average"

    def display(self):
        print("Player Name   :", self.name)
        print("Jersey Number:", self.jersey_number)
        print("Runs          :", self.runs)
        print("Category      :", self.get_category())
        print("-" * 30)


class Team:
    def __init__(self, team_name):
        self.team_name = team_name
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def display_players(self):
        print("\nTeam Name:", self.team_name)
        print("=" * 30)

        for player in self.players:
            player.display()


# Main Program
team = Team("India")

n = int(input("Enter number of players: "))

for i in range(n):
    print("\nEnter details of Player", i + 1)

    name = input("Enter Player Name: ")
    jersey = int(input("Enter Jersey Number: "))
    runs = int(input("Enter Runs: "))

    player = Player(name, jersey, runs)
    team.add_player(player)


# Display all players
print("\n--- ALL PLAYER DETAILS ---")
team.display_players()
