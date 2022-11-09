# How do you call for a function to be used
'''print("a string")

def print2('no words '):
    print(words * 2)

print2("big words ")

list = []

answer = input()
while answer != "y":
    answer = input()'''



# keep grocery list from user
# make sure i have an empty list
# use a while loop to keep collecting groceries
# ask use if they are done to exit loop
# print full list when they are done
# save it to a file, send a text message, send an email...
# While their answer is yes:
    # ask for another item


def getGroceryItem ():
    print("What do you want to add to your list?")
    item = input()
    return item

groceryList ={}

answer = "initial"

while len(answer) > 0: 
    print("Type in a new item to add it to the list or press enter to quit")
    answer = getGroceryItem()
    if answer != '':
        groceryList.append(answer)


print(groceryList)


#Homework#
#Bonus items - keep the screen clean (Google)
# Requires proper login - if failed 3 times, exit app with a message like "Unable to login at this time"
# Receipt Calculator - Take in x amount of receipts, round the total.
# print receipts taken in: line by line, sort list by least expensive to most expensive $xx.xx
# when done, display the rounded the total $xxxx (No decimal place)









