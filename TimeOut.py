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

# this will stop the timer


        