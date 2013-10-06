import serial
import time
import PassiveAccelerometer
import DataManipulation


class initial:
    def __init__(self, weight, workout):
        self.weight = weight
        self.workout = workout
        self.ser = serial.Serial('/dev/ttyACM0', 115200)
        self.sameCount = 2;
        self.valPrev = 0;
        self.ser.readline()
        self.data = []
        self.xAvg = 0
        self.yAvg = 0
        self.zAvg = 0
        
        self.timeIn()
        
    def timeIn(self):
        passive = PassiveAccelerometer.arduino(0.0,0.0,0.0)
        while (self.sameCount < 52):
            time.sleep(0.04);
            vals = passive.readValues();
            valAvg = 0
            try:
                valAvg = ((vals[0]+vals[1]+vals[2])/3)
                if (valAvg <= (abs(self.valPrev + 30))):
                    self.xAvg = (self.xAvg - vals[0]) / (self.sameCount - 1)
                    self.yAvg = (self.yAvg - vals[1]) / (self.sameCount - 1)
                    self.zAvg = (self.zAvg - vals[2]) / (self.sameCount - 1)
                    self.sameCount += 1
                self.valPrev = valAvg
            except Exception:
                passive.readValues()
        self.timeOut()
        self.sameCount=2
        #have it beep

#could get rid of the threading and make this the timeout
#Would be faster for passive        
    def timeOut(self):
        passive = PassiveAccelerometer.arduino(self.xAvg, self.yAvg, self.zAvg)
        while (self.sameCount < 50):
            time.sleep(0.080);
            vals = passive.readValues();
            
            self.data.append(vals)
            
            try:
                valAvg = ((vals[0]+vals[1]+vals[2])/3)
            except Exception:
                passive.readValues()
            
            if (valAvg <= (abs(self.valPrev + 300)) or valAvg >= (abs(self.valPrev - 300))):
                self.sameCount += 1
            valPrev = valAvg
        
        manip = DataManipulation.simpleFunctions(self.data, self.weight, self.workout)
#NOTER :: WHAT TO DO NEXT?
