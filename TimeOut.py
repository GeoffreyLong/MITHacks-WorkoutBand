import os
import pygal
import threading
import time
from . import Accelerometry
import threading

class timer:
    def __init__(self, workout, weight):
        self.workout = workout
        self.weight = weight
        self.accel = Accelerometry.arduino(self.workout, self.weight)
        self.stopped = threading.Event()
        
    def start(self):
        self.accel.start()
        
        thread = self.accel(self.stopped)
        thread.start()

    def stop(self):
        self.stopped.set()
        
    def makeGraph (avgPowers):                                          # takes as input a list of powers   
	bar_chart = pygal.Bar()                                            # create a bar graph object
	bar_chart.add('Power', avgPowers)  
	bar_chart.render_to_file('Power_bar_chart.svg')
	os.system("start "+'Power_bar_chart.svg')

# this will stop the timer


        
