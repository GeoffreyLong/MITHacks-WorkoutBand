import serial
import math
import ast
import threading
import time

class arduino(threading.Thread):
    def __init__(self, weight, workout, isRunning):
        self.weight = weight
        self.workout = workout
        self.ser = serial.Serial('/dev/ttyACM0', 115200)
        self.isRunning = isRunning
        
        threading.Thread.__init__(self)
        self.event = threading.Event()
        
        self.ser.readline()
        self.ser.readline()
        isInitialized = False
        while(isInitialized == False):
            try:
                dic = self.ser.readline()
                initialStrings = ast.literal_eval(dic)
                self.initial = [float(initialStrings[0]), float(initialStrings[1]), float(initialStrings[2])]
                if (self.initial.__contains__(None)):
                    isInitialized = False
                else:
                    isInitialized = True
            except Exception:
                isInitialized = False
                pass
        
    def readValues(self):
        try:
            dic = self.ser.readline()
            valStrings = ast.literal_eval(dic)
            vals = [float(valStrings[0]), float(valStrings[1]), float(valStrings[2])]
            if (self.initial.__contains__(None)):
                self.readValues()
            else:
                return vals
        except Exception:
            self.readValues()
            
    def magnitude(self, vals):
        normX = vals[0] - self.initial[0]
        normY = vals[1] - self.initial[1]
        normZ = vals[2] - self.initial[2]
        mag = math.sqrt(math.pow(normX,2)+math.pow(normY,2)+math.pow(normZ,2))
#NOTER ::
        if ((normX+normY+normZ)<0):
            mag = -mag
        return mag
    
    def run(self):
        while (self.isRunning == True):
            threading.Event().wait(1)
            print self.readValues()
            
    def stop(self):
        self.isRunning = False
  
#    def maxPower(self, ):
    
#    def avgPower(self, ):
    
#        connection.magnitude(connection.readValues())



