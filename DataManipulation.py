import time
import math

class simpleFunctions:
    def __init__(self, data, weight, workout):
        self.data = data
        self.workout = workout
        self.weight = weight
        
#Noter :: Last error here on data[0]        
        initial = data[0]
        self.initX = initial[0]
        self.initY = initial[1]
        self.initZ = initial[2]
        
        self.maxMag = 0
        self.lastMag = 0
        
        self.lastTime = int(round(time.time() * 1000))
        self.magV = 0
        self.avgPower = 0
        self.avgPowerDataPoints = 2
    
    def iterateThroughData(self):
        for elm in self.data:
            magElm = self.accMagnitude(elm)
            self.maxAcceleration(magElm)
            self.velocityMagnitude(magElm)
            self.avgPower()
                   
            
    def accMagnitude(self, vals):
        normX = vals[0] - self.initX
        normY = vals[1] - self.initY
        normZ = vals[2] - self.initZ
        mag = math.sqrt(math.pow(normX,2)+math.pow(normY,2)+math.pow(normZ,2))
        #NOTER ::
        if ((normX+normY+normZ)<0):
            mag = -mag
        return mag
        
    def maxAcceleration(self, mag):
        if (mag > self.maxMag):
            self.maxMag = mag
            
    def getMaxAcc(self):
        return self.maxMag        

#This is very naive and very wrong but I am putting it here anyways     
       
    def velocityMagnitude(self, mag):
        deltaT = (self.lastTime - (int(round(time.time() * 1000))))
        magV = ((mag + self.lastMag)/2) * deltaT
        self.magV += magV
        
    def getMagV(self):
        return self.magV
        
    def avgPower(self, mag):
        power = self.velocityMagnitude(mag) * self.weight * mag
        self.avgPower = (self.avgPower - power) / (self.avgPowerDataPoints - 1)

    def getAvgPower(self):
        return self.avgPower
