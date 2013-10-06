from Tkinter import *



class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white") 
        self.parent = parent
        self.initUI()
    
    def initUI(self):
        self.parent.title("Weight Bands")

def initializeNext(): 
    print optionVar.get()
    print text.get()

def main():
    root.geometry("300x300+300+40")
    optionList = ("bench", "curls", "delt raises")
    optionVar.set(optionList[0])
    option = OptionMenu(root, optionVar, *optionList)
    b = Button(root, text="Start the workout", command=initializeNext)
    option.pack()
    text.pack()    
    b.pack()
    root.mainloop()  
    
root = Tk()
text = Entry(root)
optionVar = StringVar(root)
if __name__ == '__main__':
    main() 
