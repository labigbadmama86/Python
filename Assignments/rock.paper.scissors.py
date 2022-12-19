#1 File - Collect player names
#2 save players score
#3    best if 3/5/7 - win 1 point per round(Score is the sum of all won rounds / player)
#     gotcha: what to do with Ties
#4 Use Classes where possible
#5 Make sure output is clean
# Use loops
# Free to use more of the tools we have learned

#While loop if player wants to play another round
#Use Class to keep track of points, to keep track of players
#Print "Would you like to play another round"
#Adding the players points together
#Determine how the code knows "How the player won" (Figure out how they won)
#Make sure output is not full of unnecessary things

#Rock beats Scissors
#Scissors beats Paper
#Paper beats Rock




import os
clear = lambda: os.system('cls') #Clears the terminal

#Players
numberPlayers = 0

def askPlayerCount():
    print("How many players?")
    players = input()
    if players.isdigit():
        return  int(players)
    else:
        askPlayerCount()

names = []

def playerName():
    print("Enter Player Name")
    PlayerName = input()
    if (len(PlayerName) <= 0):
        print("No Manches! That's not a name. Please try again")
        playerName()
    else: 
        names.append(PlayerName)

def numberOfPlayers():
    #print(len(names))
    #print(numberPlayers)
    while len (names) < numberPlayers:
        playerName()
    print(names)


numberPlayers = askPlayerCount()
#playerName()
numberOfPlayers()








