import serial
import math
import ast

class arduino:
def __init__(self):
	self.ser = serial.Serial('COM12', 115200)
#       self.ser = serial.Serial('/dev/ttyACM1', 115200)
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

def initialPosition(self, vals):
	if (abs(vals[0]-self.initial[0]) <= 40 and abs(vals[1]-self.initial[1]) <= 40 and abs(vals[2]-self.initial[2]) <= 40):
		ser.write('1')
		print 'TRUE! TRUE! TRUE!'

	else: 
		ser.write('0')
	print 'FALSE FALSE FALSE!'

	print ("x1: "+str(vals[0]))
	print ("y1: "+str(vals[1]))
	print ("z1: "+str(vals[2]))

if __name__ == '__main__':
	connection = arduino()
	while True:
		connection.magnitude(connection.readValues())
		connection.initialPosition(connection.readValues())

