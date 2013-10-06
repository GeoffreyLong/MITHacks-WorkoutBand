'''
Since the cost of data manipulation may be high on the chip / phone
We decided to add this passive class to manipulate the data
Using in in the place of the Accelerometer for now.
It puts the elements to an array of arrays, later a class for intensive data manipulation will be added
'''
import serial
import math
import ast
import threading
import time

class arduino(threading.Thread):
    def __init__(self, initialX, initialY, initialZ):
        self.ser = serial.Serial('/dev/ttyACM0', 115200)
        self.ser.readline()
        
    def readValues(self):
        try:
            dic = self.ser.readline()
            valStrings = ast.literal_eval(dic)
            vals = [float(valStrings[0]), float(valStrings[1]), float(valStrings[2])]
            if (valStrings.__contains__(None)):
                self.readValues()
            else:
                print vals
                return vals
        except Exception:
            self.readValues()
            
