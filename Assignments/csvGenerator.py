from random import choice, randint
#randomNumber = randint(15,80)
#print(randomNumber)
def getRandomNumber(min, max):
    return str(randint(min, max))
def getRandomName():
    names = ['Julio', 
    'Mark', 
    'Robert', 
    'John', 
    'Oogie', 
    'Jack', 
    'Sally', 
    'Zero',
    'Roxy',
    'Drake',
    'Pebbles',
    'Joy',
    'Coops',
    'Isa',
    'Monchi',
    'Leonardo the wife hater',
    'Livier',
    'Pachita',
    'Marcelo',
    'Chepa',
    'Manuel',
    'Roberto',
    'Cristina',
    'Tony',
    'Bolis']
    return choice(names)
x = 0
f = open("test.csv", 'w')
while (x < 25):
  x = x + 1
  f.write(getRandomName() + "," + getRandomNumber(15,80) + ", " + getRandomNumber(750,2500) + ", " + getRandomNumber(80,500) +
  ", " + getRandomNumber(30,150) +", " + getRandomNumber(250, 600) + "\n")
  #print(x)
f.close()



'''name, phone, house, electric, water, food
julio, 70, 850, 180, 65, 400
mark, 35, 950, 200, 72, 500
robert, 135, 1550, 400, 102, 800
john, 25, 600, 500, 250, 900'''