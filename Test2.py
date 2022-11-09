#accessing strings
mystring = "78247-4114"
print(mystring[-3])
print(mystring[0:4])
print(mystring[0:5])
mystring = "192.168.10.16"


mystring = "Cheese loves to melt on the floor"
print(mystring[-6:])
print(mystring[5:15])

# List
pets = ['cat', 'dog', 'fish', 'gerbil']
#pets = [17, 'fish', "dog", 1000.00]
print(pets)
print(pets[-1])
print(pets[-2])
print(pets[1:2])
print(pets[1:4])

#Tuple
#dogs = ('german shepherd', 'golden retriever', 'boxer', 'yorkie')
#dogs = [0] = "pit bull'" throws error, tuples cannot be updated
#print(dogs[0])


#Dictionary - set of key value pairs
webster = {}
webster[0] = "0 value"
webster[1] = '1'
webster['a'] = 'a'
print(webster)
print(webster[0])

webster2 = {'cat':'jerk','dog':'friend','mouse':'cat food'}
print(webster)
print(webster["a"])

# Loops for Loop, While Loop
#For Loop - do something while the condition is true
#while (True):
  #  print("hello")

pets = ['cat','dog','fish','gerbil']
for pet in pets:
  print(pet)

x = 0
i = 0
while (x < 10):
  x = x + 1
  i = x
  print(x * i)







