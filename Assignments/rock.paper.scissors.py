#- 1 File - Collect player names
#2 - save players score
#3    best if 3/5/7 - win 1 point per round(Score is the sum of all won rounds / player)
#     gotcha: what to do with Ties
#4 Use Classes where possible
#5 - Make sure output is clean
#  - Use loops
# Free to use more of the tools we have learned

#While loop if player wants to play another round
#Use Class to keep track of points, to keep track of players
#Print "Would you like to play another round"
#Adding the players points together
#Determine how the code knows "How the player won" (Figure out how they won)
# - Make sure output is not full of unnecessary things
#Quit game
#start a new game

#Rock beats Scissors
#Scissors beats Paper
#Paper beats Rock




import os
from random import randint
clear = lambda: os.system('cls') #Clears the terminal

clear() # Clearing the screen when running.
#Players
numberPlayers = 2 #saving # of players(numberPlayers)

names = [] # Saving input (names)

def playerName():
    print("Enter Player Name")
    PlayerName = input()
    if (len(PlayerName) <= 0): # if nothing entered, it will print phrase
        print("No Manches! That's not a name. Please try again")
        playerName()
    else:
        names.append(PlayerName) #saving to the names dictionary

def numberOfPlayers():
    while len (names) < numberPlayers: #Will re run playerName fuction till all names are entered
        playerName()
    print(names)

numberOfPlayers() 

#Random RPS selection
rps = {1 : "Rock", 2 : "Paper", 3 : "Scissors"}

def randomGenerator():
    randomNumber = randint(1,3)
    print (rps[randomNumber])

def randomPlayerObjects(): 
    clear()
    for name in names: #generate # of objects depending on # of players
        print(name)
        randomGenerator() #Calls out randomGenerator function

randomPlayerObjects()











'''def Rock(a,b):
    if "Rock" is True:
        "Rock" > "Scissors"
        "Rock" < "Paper"
    else:
        return False

def Scissors():
    if "Scissors" is True:
        "Scissors" > "Paper"
        "Scissors" < "Rock"

def Paper():
    if "Paper" is True:
        "Paper" > "Rock"
        "Paper" < "Scissors"'''














