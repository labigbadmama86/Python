#Reviewing Homework from 12/05

#Homework
#create a class that helps you calculate something
#calculate at least 3 different things(example: yard cutting, weed eating, light)


class LandScapingEstimator:
    #Yard Cutting Properties
    YardArea = 100
    YardCuttingRate = 0 #Charge per sq ft
    YardLength = 0
    YardWidth = 0

#Weed Eating
    LinearFeet = 0
    WeedEatingRate = 0
    YardLength = 0 
    YardWidth = 0


#lighting
    LightCost = 0 # Light cost + rate/light
    QuantityLights = 0 

#Constructor
    def __init__(this, yardCuttingRate, weedEatingRate, lightingCost):
        this.YardCuttingRate = yardCuttingRate
        this.WeedEatingRate = weedEatingRate
        this.LightCost = lightingCost

# maybe**** Showed up charge + rate * area
    def YardCuttingCost(this, area = 0, length = 0, width = 0):
        if area > 0 :
            cost = area * this.YardCuttingRate
            return cost
        if area <= 0:
            calculatedArea = length * width
            cost = calculatedArea * this.YardCuttingRate
            return cost

    def GetWeedCuttingCost(this, length = 0, width = 0):
        calculatedPerimeter = (length * 2) + (width * 2)
        cost = calculatedPerimeter * this.WeedEatingRate
        return cost

    def GetLightingInstallationCost(this, lights):
        return lights * this.LightCost

leosEstimator = LandScapingEstimator(.02, 5, 45)
yardEstimate = leosEstimator.GetYardCuttingCost(0, 96, 40)
weedTrimmingEstimate = leosEstimator.GetWeedCuttingCost(0,96,40)
print(yardEstimate)



