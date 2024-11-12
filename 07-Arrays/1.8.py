computer_games = [
   "Minecraft", "Fortnite", "Cyberpunk 2077", "The Witcher 3",
   "League of Legends", "Valorant", "Grand Theft Auto V", 
   "Elden Ring", "Apex Legends", "Call of Duty: Warzone"
]
counter = 0
while counter < len(computer_games):
    print(f"{(counter+1)}.", computer_games[counter])
    counter += 1