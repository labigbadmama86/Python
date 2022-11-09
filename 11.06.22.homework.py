#Login
users = {"Leo" : "Leonard Aguillon", "Isa" : "Isabel Aguillon", "Munch" : "Leonardo Aguillon"}
def checkUser (username):
    if username in users:
        return True
    else: 
        return False * 3
print("Unable to login at this time")

def getUser (username):
    fullname = users[username]
    return fullname
    
def login():
    print("Enter your user name:")
    username = input()
    return username
    
user = login()
validUser = checkUser(user)
if validUser == True:
    print("Hello " + getUser(user))
else:
    print("Login Failed.")

#Receipt

def receipts():
    print("Enter Receipt")
    item = input()
    return item

receiptsList = {}

answer = "initial"
while len(answer) > 0: 
    print("Type in a new receipt to add it to the list or press enter to quit")
    answer = getReceiptsList()
    if answer != '':
        receiptsList.append(answer)

for receipt in receiptsList:
    print(receiptsList)



