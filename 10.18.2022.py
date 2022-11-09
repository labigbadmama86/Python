users = {"Leo" : "Leonard Aguillon", "Bolis" : "Olivia Aguillon", "Bee" : "Livier Aguillon"}
tempname = "" # Using global string

def greetUser (username):
    fullname = users[username]
    #print(fullname)
    global tempname
    tempname = fullname
    return fullname
    print("Welcome, " + username)


# For some reason, we have the user name, ma7be they logged in?
name = greetUser("Leo")
print ("Welcome" + name + "!")


print(tempname)

# do function with optional parameter/argument
def optional (firstName, lastName = ""):
    print("Hello " + firstName + " " + lastName)
    return

print("John", "Doe")
optional("Mark")

# Take in data
'''print("Enter the password")
password = input()
print("Password: " + password)
'''

def checkUser (username):
    if username in users:
        return True
    else: 
        return False


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



#10.18.2022
'''#Homework "Login.py"
using the login above, add a while loop to make the 
system keep asking for a username until the user provides
a username from your list

if user gives right username, say something like "Login Successful
if user gices wrong username, say something like "Login Failed, 
Ask for the username again'''


