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
    root.geometry("500x500+300+40")
    
    titleFont = tkFont.Font(family="Helvetica",size=14,weight="bold")
    title = Label(root, text="HOW WOULD YOU LIKE YOUR GRAPH?", font=titleFont)
    title.place(x=70, y=20)

    subTitleFont = tkFont.Font(family="Helvetica",size=10,weight="bold")
    accVsTimeLabel = Label(root, text = "Graph of Acceleration Vs. Time", font=subTitleFont)
    accVsTimeLabel.place(x=10, y=60)
    
    radioChoice = IntVar()

    Radiobutton(root, text="X-axis", variable=radioChoice, value=1).place(x=10, y=80)
    Radiobutton(root, text="Y-axis", variable=radioChoice, value=2).place(x=100, y=80)
    Radiobutton(root, text="Z-axis", variable=radioChoice, value=3).place(x=190, y=80)
    Radiobutton(root, text="Magnitude", variable=radioChoice, value=4).place(x=280, y=80)
    
    accVsTimeButton = Button(root, text="Graph it!", command="", background="#C48385", border=2)
    accVsTimeButton.place(x=10, y=100)
    
    
    subTitleFont = tkFont.Font(family="Helvetica",size=10,weight="bold")
    powVsTimeLabel = Label(root, text = "Graph of Power Vs. Time", font=subTitleFont)
    powVsTimeLabel.place(x=10, y=140)
    
    radioChoiceTwo = IntVar()

    Radiobutton(root, text="X-axis", variable=radioChoiceTwo, value=1).place(x=10, y=160)
    Radiobutton(root, text="Y-axis", variable=radioChoiceTwo, value=2).place(x=100, y=160)
    Radiobutton(root, text="Z-axis", variable=radioChoiceTwo, value=3).place(x=190, y=160)
    Radiobutton(root, text="Magnitude", variable=radioChoiceTwo, value=4).place(x=280, y=160)
    
    powVsTimeButton = Button(root, text="Graph it!", command="", background="#C48385", border=2)
    powVsTimeButton.place(x=10, y=180)
    
    root.mainloop()  

    
root = Tk()
text = Entry(root, width=8)
optionVar = StringVar(root)
if __name__ == '__main__':
    main() 