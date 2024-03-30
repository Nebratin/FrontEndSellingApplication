
from tkinter import *
from tkinter import ttk
RED = "#BF0D3E"
BLUE = "#0033A0"
GOLD = "#866D4B"
PINK = "#E8D6CB"
MAGNOLIA = "#F8F0FB"

app = Tk()
app.title("Bar Code Reader")
app.geometry("800x1000")
app.maxsize(800,1000)


# allframe= Frame(app, bg=GOLD, height=1000, width=800)
# allframe.pack()
topFrame = Frame(app, bg=GOLD, height=100)
rightFrame = Frame(app, bg=GOLD, height=800, width=580, bd=3)
leftFrame = Frame(app, bg=GOLD, height=800, width=200, bd=3)
# topFrame.grid_propagate(0)


rightLabel = LabelFrame(rightFrame,text="Bonul curent",width=577,height=794,font=('Helvetica 18 bold'))
rightLabel.grid(column=0, row=0, sticky=NSEW)
rightLabel.grid_propagate(0)

totalLabel = Label(topFrame, text="Total:  100 RON", font=('Helvetica 30 bold' ), bg=GOLD, fg='white')
totalLabel.grid(column=0, row=0, padx=10, pady=30)
achitaButton = Button(topFrame, text='Finalizeaza')
achitaButton.grid(column=1, row=0, padx=30)
restLabel = Label(topFrame, text="Rest:  100 RON", font=('Helvetica 30 bold' ), bg=GOLD, fg='white')
restLabel.grid(column=2, row=0, padx=30, pady=30)
restLabel.grid_forget()

# item1Label = Label(rightLabel, text="Salam de vara  1,345 kg x 23,45 RON = 45,67 RON", font=('Helvetica 16'))
# item1Label.grid(column=0, row=0, padx=5, pady=5, sticky=EW)
# item2Label = Label(rightLabel, text="Carne tocata  2,560 kg x 31,45 RON = 45,67 RON", font=('Helvetica 16'))
# item2Label.grid(column=0, row=1, padx=5, pady=5, sticky=EW)
# item3Label = Label(rightLabel, text="Carne tocata porc 2,560 kg x 31,45 RON = 45,67 RON", font=('Helvetica 16'))
# item3Label.grid(column=0, row=2, padx=5, pady=5, sticky=EW)

item1Label = Label(rightLabel, text="Salam de vara", font=('Helvetica 16'))
item1Label.grid(column=0, row=0, padx=5, pady=5, sticky=W, columnspan=3)
item2Label = Label(rightLabel, text="Carne Tocata", font=('Helvetica 16'))
item2Label.grid(column=0, row=1, padx=5, pady=5, sticky=W, columnspan=3)
item3Label = Label(rightLabel, text="Carne Tocata Porc", font=('Helvetica 16'))
item3Label.grid(column=0, row=2, padx=5, pady=5, sticky=W, columnspan=3)
item4Label = Label(rightLabel, text="1,375 kg x", font=('Helvetica 16'))
item4Label.grid(column=3, row=0, padx=5, pady=5, sticky=E, columnspan=1)
item5Label = Label(rightLabel, text="2,560 kg x", font=('Helvetica 16'))
item5Label.grid(column=3, row=1, padx=5, pady=5, sticky=E, columnspan=1)
item6Label = Label(rightLabel, text="3 BUC x", font=('Helvetica 16'))
item6Label.grid(column=3, row=2, padx=5, pady=5, sticky=E, columnspan=1)



topFrame.grid(column=0, row=0, columnspan=2,pady=5,sticky=EW)
leftFrame.grid(ipadx=5, column=0, row=1)
rightFrame.grid(ipadx=5, column=1, row=1, padx=5)





app.mainloop()