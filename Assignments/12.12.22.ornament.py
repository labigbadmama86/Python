#Bead Project Estimator

class OrnamentEstimator:
    Bicone3mm = 0
    FirePolished3mm = 0
    FirePolished4mm = 0
    Bugle6mm = 0
    SeedBead11o = 0
    BeadingNeedle12 = 0
    FireLine = 0
    Ornament = 0
    Navette3HL = 0
    SeedBead15o = 0
    KiteBeads2HL = 0
    Labor = 0

    def GetOrnamentCost(this,quantity,type):
        if type == "Diamond":
            this.Bicone3mm = 90
            this.FirePolished3mm = 20
            this.FirePolished4mm = 20
            this.Bugle6mm = 4
            this.SeedBead11o = 8
            this.BeadingNeedle12 = 2
            this.FireLine = 10
            this.Ornament = 1
            this.Labor = 6

            ornamentCost = ((this.Bicone3mm * this.GetRate("Bicone3mm")) 
            + (this.FirePolished3mm * this.GetRate("FirePolished3mm"))
            + (this.FirePolished4mm * this.GetRate("FirePolished4mm"))
            + (this.Bugle6mm * this.GetRate("Bugle6mm"))
            + (this.SeedBead11o * this.GetRate("SeedBead11o"))
            + (this.BeadingNeedle12 * this.GetRate("BeadingNeedle12"))
            + (this.FireLine * this.GetRate("FireLine"))
            + (this.Ornament * this.GetRate("Ornament"))
            + (this.Labor * this.GetRate("Labor"))
            )
            #print(this.Labor * this.GetRate("Labor"))
            return ornamentCost * quantity
        

        if type == "Flower":
            this.Navette3HL = 56
            this.FirePolished4mm = 112
            this.SeedBead11o = 12
            this.SeedBead15o = 1
            this.KiteBeads2HL = 21
            this.Ornament = 1
            this.FireLine = 12
            this.BeadingNeedle12 = 2
            this.Labor = 8

            ornamentCost = ((this.Navette3HL * this.GetRate("Navette3HL")) 
            + (this.FirePolished4mm * this.GetRate("FirePolished4mm"))
            + (this.SeedBead11o * this.GetRate("SeedBead11o"))
            + (this.SeedBead15o * this.GetRate("SeedBead15o"))
            + (this.KiteBeads2HL * this.GetRate("KiteBeads2HL"))
            + (this.Ornament * this.GetRate("Ornament"))
            + (this.FireLine * this.GetRate("FireLine"))
            + (this.BeadingNeedle12 * this.GetRate("BeadingNeedle12"))
            + (this.Labor * this.GetRate("Labor"))
            )
            #print(this.Labor * this.GetRate("Labor"))
            return ornamentCost * quantity
        

    def GetRate(this, item):
        rates = {"Bicone3mm" : .07, "FirePolished3mm" : .19,
         "FirePolished4mm" : .04, "Bugle6mm" : .42,
         "SeedBead11o" : .43, "BeadingNeedle12" : .30, 
         "FireLine" : .23, "Ornament" : .42, "Labor" : 20,
         "Navette3HL" : .12, "SeedBead15o" : .26, "KiteBeads2HL" : .07}
        return rates[item]

estimator = OrnamentEstimator()
LeosOrnaments = estimator.GetOrnamentCost(1, "Diamond")
print("Diamond Ornament Cost $", LeosOrnaments)
LiviersOrnaments = estimator.GetOrnamentCost(1, "Flower")
print("Flower Ornament Cost $",LiviersOrnaments)