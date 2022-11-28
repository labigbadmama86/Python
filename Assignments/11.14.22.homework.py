
import os   #Clearing terminal
clear = lambda: os.system('cls')

clear()
print("Enter Filename")
filename = input()

# File check if file exists
def fileExists(filename):
    try:
        f = open(filename, "r")
        f.close()
        return True
    except:
        return False

if fileExists(filename) == True:
    print("File exists, what would you like to add")
    userText = input()
    f = open(filename, "a")
    f.write(userText + "\n")
    f.close()
else:
    print("Creating new file, Add some text:")
    userText = input()
    f = open(filename, "w")
    f.write(userText + "\n")
    f.close()

userText = "y"  #While Loop
while userText == "y":
    clear()
    print("Would you like to add another message? y/n")
    userText = input()
    if userText == "y":
        print("What would you like to add?")
        addtext = input()
        f = open(filename, "a")
        f.write(addtext + "\n")
        f.close()





clear()
print("File contents:",filename)
f = open(filename, 'r')
print(f.read())
f.close()

    
#File Open
#file = open("lessons.reference.tx")
#print(file.read())
#file.seek(0, 0)















