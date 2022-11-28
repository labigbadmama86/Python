from random import randint


def hairlength ():
    hairlength = {1 : "Long",2 : "Medium",3 : "Short"}
    #print ("What Hair Length would you like?")
    #length = input()
    random = randint(1,3)
    return hairlength[random]


def HairColor ():
    HairColor = {1 : "Blonde",2 : "Brown",3 : "Red"}
    #print ("What Hair Color would you like?")
    #color = input()
    random = randint(1,3)
    return HairColor[random]

def TypeOfHair ():
    TypeOfHair = {1 : "Straight",2 : "Wavy",3 : "Curly"}
    #print ("What Type of Hair do you have?")
    #typeofhair = (input)
    random = randint(1,3)
    return TypeOfHair[random]



length = hairlength()
color = HairColor()
type = TypeOfHair()

print (length)
print (color)
print (type)


