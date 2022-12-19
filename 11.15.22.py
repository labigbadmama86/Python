#Break pieces up into logical groups
#Objects = description of something


class PersonA:
    age = 41
    name = "Leonard"
    height = 68
    lastName = "Aguillon"

person = PersonA()
print(person.name,person.lastName)
# Constructor
class Person:
    def __init__(self, age, name, height, lastName):
        self.age = age
        self.name = name
        self.height = height
        self.lastName = lastName

person1 = Person(41, "Leonard", 68, "Aguillon")
if(person1.age> 21):
    print(person1.name, "is old enought to drink")
# Person(green) = 
person2 = Person (33, "Olivia", 60, "Aguillon")

class Bills:
#_init_ is our class constructor
# self can be named anything we want(Pizza)
#WHen data is passed to it, it assigns the given data to the associated properties of our class
    def __init__(self, rent, electric, water, gas, phone):
        self.rent = rent
        self.electric = electric
        self.water = water
        self.gas = gas
        self.phone = phone
#Here we are defining a function inside our class
    def total(self):
        return(self.rent + self.electric + self.water + self.gas + self.phone)
# Here we are calling a function fron another function from within the class
    def yearlyTotal(self):
        return self.total() * 12

leoBills = Bills(1350, 250, 100, 0, 115)
leosTotal = leoBills.total()
print(leosTotal)

class Pizza:
    def __init__(this, size, crust, toppings):
        this.Size = size
        this.Crust = crust
        this.Toppings = toppings

pizza = Pizza("Large", "Stuffed", ["Pepperoni", "jalapeno"])
print(pizza.Toppings)

#Files - Saving, reading, writing data
# file = nothing more than a collection of data all stored together. 
# #File extention can be names anything we want. 

# File Open & Reading
file = open("test.txt","r")
print(file.read())  #file needs to be in directory in order for a file to open(error when running because there is no file)
file.seek(0, 0) # will read the whole file


file = open("lessons.refere.ce.txt","r")
#print(file.read()

#Will open the file from the directory
print(file.read(4)) #will print the first 4 characters
#Read line looks for a line terminator or end of the line characters like'enter'
print(file.readline()) #will read the first line to the end of the first line
print(file.realine()) #since the first line was read, it will read the 2nd line to the end of the 2nd line
file.close() # Closes the file

# File writing
f = open("Notes.txt","w") # W is "write" mode and will overwrite the file contents
f.write("OMG I created a file")
f.close()

f = open("Notes.txt", "a") # a is append mode and will add data to a file
f.write("Hey, look another line") 
f.close()

f = open("Notes.txt", "a") # a is append mode and will add data to a file
f.write("Hey, look another line\n") # \n creates a new line below "OMG I created a file"
f.write("adding another one!\n") # if I comment out "OMG I created a file", this will show "Hey, look another line" and "adding another one!" (Append)
f.close()


# File check if file exists
def fileExists(filename):
    try:
        f = open(filename, "r") # "r" = read only
        f.close()
        return True
    except:
            return False

print("Enter Filename:")
filename = input()

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

f = open(filename, 'r')
f.read()
f.close()

import os   #Clearing terminal
clear = lambda: os.system('cls')  #clear function

clear() #clears the screen at that point...() call out the imported clear function


#Homework 
# allow user to pick the file name
# check if the file exists, add to it, if it doesnt, create it
# use a loop and write some numbers to the file
# Feel free to add extras

## starting point (# File check if file exists)








