import serial
import math
import ast
import Accelerometer
import TimeOut
import time

class initial:
    def __init__(self, weight, workout):
        self.weight = weight
        self.workout = workout
        self.ser = serial.Serial('/dev/ttyACM0', 115200)
        self.startBoolean = False;
        self.sameCount = 0;
        self.valPrev = 0;
        self.timer = TimeOut.timer(self.workout, self.weight)
        
        self.ser.readline()
        self.ser.readline()
        isInitialized = False
        while(isInitialized == False):
            try:
                valArray = self.ser.readline()
                initialStrings = ast.literal_eval(valArray)
                self.x = float(initialStrings[0])
                self.y = float(initialStrings[1])
                self.z = float(initialStrings[2])
                if (initialStrings.__contains__(None)):
                    isInitialized = False
                else:
                    isInitialized = True
            except Exception:
                isInitialized = False
                pass
        self.timeIn()
        
    def readValues(self):
        try:
            dic = self.ser.readline()
            valStrings = ast.literal_eval(dic)
            vals = [float(valStrings[0]), float(valStrings[1]), float(valStrings[2])]
            if (valStrings.__contains__(None)):
                self.readValues()
            else:
                return vals
        except Exception:
            self.readValues()

    def timeIn(self):
        while (self.sameCount < 50):
            time.sleep(0.04);
            print(self.sameCount)
            vals = self.readValues();
            try:
                valAvg = ((vals[0]+vals[1]+vals[2])/3)
            except Exception:
                self.readValues()
            if (valAvg <= (abs(self.valPrev + 30))):
                self.sameCount += 1
            self.valPrev = valAvg
        self.timer.start()
        self.sameCount=0
        self.timeOut()
        
    def timeOut(self):
        while (self.sameCount < 50):
            time.sleep(0.04);
            vals = self.readValues();
            try:
                valAvg = ((vals[0]+vals[1]+vals[2])/3)
            except Exception:
                self.readValues()
            if (valAvg <= (abs(self.valPrev + 30))):
                self.sameCount += 1
            valPrev = valAvg
        self.timer.stop()
#NOTER :: WHAT TO DO NEXT?
