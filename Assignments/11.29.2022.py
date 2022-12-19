import os
clear = lambda: os.system('cls')

class Bills:
    def __init__(this, name, phone, house, electric, water, food):
        this.name = name
        this.phone = phone
        this.house = house
        this.electric = electric
        this.water = water
        this.food = food
    
    def total(this):
        return this.phone + this.house + this.electric + this.water, this.food

def saveToFile(name, total):
    filename = 'total.txt'
    f = open(filename, 'a')
    f.write(name + ": " + str(total) + "\n")
    f.close() 

def clearFile():
    filename = 'total.txt'
    f = open(filename, 'w')
    f.close()

clear()
clearFile() #using this to clear our our save file
f = open("test.csv", "r") # our csv we are opening
numberLines = len(f.readlines()) # Determine the number of lines in it
f.seek(0,0) # reset the file pointer
startingLine = 0 #set out starting point
runningTotal = 0
recordsProcessed = 0
while startingLine < numberLines:
    line = f.readline() # reads an entire line from the file
    line = line.strip() # Clean off the newline character \n
    print(line.split(','))
    #Split will split apart a string by whatever delimenter is provided
    pieces = line.split(',')
    cleanPieces = []
    for piece in pieces:
        cleanPieces.append(pieces.strip())
    # Turn this into an object 
    if str(cleanPieces[1]).isdigit():
        userBills = Bills(cleanPieces[0], int(cleanPieces[1]), 
        int(cleanPieces[2]), int(cleanPieces[3]), int(cleanPieces[4]), int(cleanPieces[5]))
        print(userBills.name, ": ", userBills.total())
        saveToFile(userBills.name, userBills.tota())
        runningTotal+= int(userBills.total())
        recordsProcessed += 1
    #else:
        #print("skipped: ", line)

    #print(userBills.electric)

'''
for piece in pieces: # looping throught the split apart pieces
    piece = piece.strip() # using strip to clean off empty spaces
    print(piece)  '''
startingLine += 1

print()
print("Records Processed: ", recordsProcessed)
print("Running Total: ", runningTotal)



'''
1. Read in a CSV file
2. Process each line of the CSV file
    a. Convert each line to an object
    b. Total the person's bills
    c. Write the person's name along with the total to a new fiile
3. Keep track of the running total
4. Display total users processed and total bills calculated
'''
#ways to evade column headers from popping the code
# Change the seek?



#Homework Using the current working code above!
# Add up each bill seperately (Like running total)
# Create a new script that will add 25 random rows to test.csv
# Name the new script (fileProcessing.py)
# csvGenerator.py 


