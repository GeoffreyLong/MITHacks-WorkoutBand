import threading
import time
import threading
import Accelerometer

class timer:
    def __init__(self, workout, weight):
        self.workout = workout
        self.weight = weight
        self.accel = Accelerometer.arduino(self.workout, self.weight)
        self.stopped = threading.Event()
        
    def start(self):
        self.accel.start()
        
        thread = self.accel(self.stopped)
        thread.start()

    def stop(self):
        self.stopped.set()

# this will stop the timer


        
