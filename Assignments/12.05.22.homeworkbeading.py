#Project Beadwork with Already calculated cost per material item
import os

clear = lambda: os.system('cls')

class Beads:  # Properties
    Fireline = 0
    Clasp = 0
    Pendant = 0
    CrystalA = 0
    CrystalB = 0
    Toho11 = 0
    Shipping = 0
    Time = 0
    #Class Constructor = Assigning the given variables to the 'properties of our object
    # (This defines the Class)
    def __init__(this, fireline, clasp, pendant, crystalA, crystalB, toho11, shipping, time):
        this.Fireline = fireline
        this.Clasp = clasp
        this.Pendant = pendant
        this.CrystalA = crystalA
        this.CrystalB = crystalB
        this.Toho11 = toho11
        this.Shipping = shipping
        this.Time = time

    def getProjectTotal(this):
        return this.Fireline + this.Clasp + this.Pendant + this.CrystalA + this.CrystalB + this.Toho11 + this.Shipping + this.Time


    
#Instances
RobertosProject = Beads(2,1,47,2,11,8,10,120)
print(RobertosProject.getProjectTotal())











#Did not work for the project
# Fireline = Beads ('Fireline 5 yards', 2)
# Clasp = Beads ('Clasp per', 1)
# Pendant = Beads ('Pendant per', 47)
# CrystalA = Beads ('Crystals 4mm', 2)
# CrystalB = Beads ('Crystals 3mm', 11)
# Toho11 = Beads ('Toho Seed Beads', 8)
# Shipping = Beads ('Shipping Cost', 10)
# Time = Beads ('Time Beading', 60)

#beadsTotal = (Fireline, Clasp, Pendant, CrystalA, CrystalB, Toho11, Shipping)

#for Beads in bead:
    #print("Total Project Cost is", )











#Adding the total maybe
#def total(this):
    #return this.fireline + this.clasp + this.pendant + this.crystalA + this.crystalB + this.toho11 + this.shipping + this.time


    



    



