from tkinter import *

root = Tk()

def leftClick(event):
    print("LEFT")
    
def middleClick(event):
    print("MIDDLE")

def rightClick(event):
    print("RIGHT")
    
def add(): 
    num1 = int(input("Please enter first number: "))
    num2 = int(input("Please enter second number: "))
    result = num1 + num2
    print(result)

def one():
    print("ONE")

def click():
    print("Value is: "+ variable.get())
    method = variable.get()
    print(method)
    result=method
    
    test = eval(result)
    test()
    
    
    

    
frame = Frame(root, width=300, height = 250)
frame.bind("<Button-1>", leftClick)
frame.bind("<Button-2>", middleClick)
frame.bind("<Button-3>", rightClick)

frame2 = Button(root, text="ADD", command = add)

variable = StringVar(root)
variable.set("add")

frame3 = OptionMenu(root, variable, "one", "two", "three")

frame4 = Button(root, text="Output selected option", command = click)


frame.pack()
frame2.pack()
frame3.pack()
frame4.pack()


root.mainloop()

