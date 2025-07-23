# make randomiser 

import random 


def roll():
    max_value = 6
    min_value = 0 
    roll = random.randint(min_value, max_value)
    return roll

value = roll() 
print(value)

#choose number of players 


while True:
    players = int(input("Enter a number of player between 1-4: "))
     
    if players < 1 or players > 4:
        print("Try again")
        
    else: 
        break 

print(players)

player_list = []

for i in range(players): 
    player = i + 1 
    player_list.append(player)

print(player_list)

#now use each player to roll the dice and take turns, then add up their scores and for players who roll 6 lose their points, first to 50 wins 
    

