import os
import pygal #http://pygal.org/download/
import threading
import time
import threading
import Accelerometer

class timer:
    def __init__(self, workout, weight):
        self.workout = workout
        self.weight = weight
        
        self.accel = Accelerometer.arduino(self.workout, self.weight, True)
        
    def start(self):
        self.accel.start()

    def stop(self):
        self.accel.stop()
'''       
    def makeGraph (avgPowers):                                                   # First import pygal
    bar_chart = pygal.Bar()                                            # Makes a simple bar graph of powers eg: avgPowers = [5.2, 2.5, 7.9]
    bar_chart.add('Power (in J)', avgPowers)  
    bar_chart.x_labels = map(str, range(1, len(avgPowers)+1))
    bar_chart.render_to_file('Power_bar_chart.svg')
    os.system("start "+'Power_bar_chart.svg')
'''
# this will stop the timer


        
