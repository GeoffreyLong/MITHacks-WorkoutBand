import time
import math

class simpleFunctions:
    def __init__(self, data, weight, workout):
        self.workout = workout
'''        
        self.maxMag = 0
        self.lastMag = 0
        self.lastTime = int(round(time.time() * 1000))
        self.magV = 0
        self.avgPower = 0
        self.avgPowerDataPoints = 2
        self.weight = weight
        self.workout = workout
        
    def maxAcceleration(self):
        mag = self.accMagnitude()
        if (mag > self.maxMag):
            self.maxMag = mag
            
    def getMaxAcc(self):
        return self.maxMag        

#This is very naive and very wrong but I am putting it here anyways     
       
    def velocityMagnitude(self):
        mag = self.accMagnitude()
        deltaT = (self.lastTime - (int(round(time.time() * 1000))))
        magV = ((mag + self.lastMag)/2) * deltaT
        self.magV += magV
        
    def getMagV(self):
        return self.magV
'''
        
    def avgPower(self):
        power = self.velocityMagnitude() * self.weight * self.accMagnitude()
        self.avgPower = (self.avgPower - power) / (self.avgPowerDataPoints - 1)

    def getAvgPower(self):
        return self.avgPower
