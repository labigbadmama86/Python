#Reviewing the file processing, csv generator, Leo's CSV Generator

# the following items are the properties of the class
class House:
    Owner = 0
    SquareFootage = 0
    Bedrooms = 0
    Bathrooms = 0
    NumberStories = 0
    AttachedGarage ='y'
    Basement = 'n'

    # Class constructor - this is assigns the given variables to the 'properties' of our object
    def __init__(this, owner, sqFeet, bedrooms, bathrooms, stories, garage = 'y', basement = 'n'):
        this.Owner = owner
        this.SquareFootage = sqFeet
        this.Bedroom = bedrooms
        this.Bathrooms = bathrooms
        this.NumberStories = stories
        this.AttachedGarage = garage
        this.basement = basement
        # a function that the house class can do
        def UpdatHouse(this, owner, sqFeet, bedrooms, bathrooms, stories, garage, basement):
            # Save these values to the database
            print("saving to the database")

bolisHouse = House('Bolis Aguillon', 2650, 3, 2.5,2, 'y''n')

print("Bolis house is:", bolisHouse.SquareFootage, "sqft")

leosHouse = House('Livier Aguillon', 2381, 3, 2.5, 2) #Here we are creating Instances of the class
isasHouse = House('Isabel Aguillon', 327, 1,1,2, 'n', 'n')
donaldHouse = House('Donald Martin', 3700, 4, 4.5, 3, 'y', 'y')
munchHouse = House ('Munch Aguillon', 399, 4, 1, 'n', 'n')

houses = [bolisHouse, leosHouse, isasHouse, donaldHouse, munchHouse] # Adding them to a list

for house in houses: #Looping through our list of house objects
    if house.Bedrooms > 2:
        print(house.Owner, "Awesome House!")
    if house.SquareFootage < 400:
        print(house.Owner, 'has an awesome electric bill!')