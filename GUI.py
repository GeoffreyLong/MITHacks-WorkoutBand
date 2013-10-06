from Tkinter import *
import tkFont
import InitializeAccel


class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white") 
        self.parent = parent
        self.initUI()
    
    def initUI(self):
        self.parent.title("Weight Bands")

def initializeNext(): 
    workout = optionVar.get()
    weight = text.get()
    InitializeAccel.initial(workout, weight)

def main():
    root.geometry("300x300+300+40")
    
    titleFont = tkFont.Font(family="Helvetica",size=14,weight="bold")
    title = Label(root, text="WORKOUT SELECTION", font=titleFont)
    title.place(x=45, y=20)
    
    liftLabel = Label(root, text="Enter the workout : ")
    liftLabel.place(x=5, y=55)
    
    optionList = ("bench", "curls", "delt raises")
    optionVar.set(optionList[0])
    option = OptionMenu(root, optionVar, *optionList)
    option.place(x=190, y=50)
    
    weightLabel = Label(root, text="Enter the mass of weights (Kg) : ")
    weightLabel.place(x=5, y=100)
    
    text.place(x=210, y=100)  
    
    lineBreak = Label(root, text="_____________________________________________")
    lineBreak.place(x=12, y=160)
    
    note = Label(root, text="please rest the odometer in")
    note.place(x=55, y=180)
    noteContOne = Label(root, text="the starting position for at least one second")
    noteContOne.place(x=10, y=200)
    noteContTwo = Label(root, text="to initiate the accelerometer")
    noteContTwo.place(x=55, y=220)
    
    b = Button(root, text="Start the workout", command=initializeNext, background="#6AA5F2", 
               activebackground="#6AD5F2", border=3)
    b.place(x=75, y=250)
    
    root.mainloop()  
    
root = Tk()
text = Entry(root, width=8)
optionVar = StringVar(root)
if __name__ == '__main__':
    main() 
