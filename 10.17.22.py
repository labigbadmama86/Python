#Math Functions
from math import ceil, floor

absoluteValue = abs(-7) # distance from zero
print(absoluteValue) 

ceilValue = ceil(99.87) # cveil always goes UP
print(ceilValue)

floorvalue = floor(99.99) # floor always goes Down
print(floorvalue)

compareValue = cmp(1, 2)
print(compareValue)

def compareValue(a, b):
    return a == b

compareVal = compareValue ('One', 'One')
print(compareVal)

# other function
#  exp(exponent of), log(logarithm of), log10(logarithm of base 10)
# max(item, item2), min(item2), sqrt(square root), round(value, places)

People = {'Leo' : 41, 'Munch' : 15,'Isa' : 17, 'Zebra' : 1, 'Livier' : 36, "Donald" : 14, 'Olivia' :33}
numbers = {27 : "R", 35 : "2", 96: "W", 1 : "A", 13 : "C" }

#print(sorted (people.items(), jey=lambda item: item[1]))
# max () sorts by the "key" in the dictionary
print(max(People))
print(min(People))
print(max(numbers))
print(min(numbers))


#Define a Function
# Function can take in x amount of parameters
def printMe(str):
    print(str)
    return

def multiply (intA, intB):
    answer = intA * intB
    #print(answer)
    return answer
        
printMe("Leo Rules")

x = multiply(9, 10)
print(x * 10)

printMe(7)