#while
from random import randint


name = "Joe"
while (name != "munch") and (name != "Isa")
    print ("Your not my child!")

age = 14
if age < 21:
    cantsmoke = True
elif age < 65:
    cantsmoke = False
else:
    cantsmoke = True
    

messages = {1 : "Not Today", 2: "Try again later", 3: "Definitely Not!", 4: "There's a chance", 5: "Yes"}

print("What's yout question?")
question = input()
randomNumber = randint(1,5)
#print(randomNumber)
print(messages[randomNumber])


def getNumber(numbers):
    numbersToReturn = []
    i = 0 
    while i <= numbers:
        numbersToReturn.append(randint(1,65))
        i = i + 1    # i = i + 1
    return numbersToReturn

def playPowerball():
    print



# Boolean Values True of False "Used on the Login Function"
evenNumberList = ["0", "2", "4", "6", "8"]
myNumber = 226

def modIsEven(num):
modValue = num % 2
if modValue > 0: 
    return False
return True

def isEven(num):
    mynum = str(num)
    print(myNumber[-1])
    if lastDigit in evenNumberList:
        return True
    return False

isEven(myNumber)
