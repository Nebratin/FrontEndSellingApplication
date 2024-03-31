import time
import tkinter as tk
from tkinter import *
from tkinter import ttk

RED = "#BF0D3E"
BLUE = "#0033A0"
GOLD = "#866D4B"
PINK = "#E8D6CB"
MAGNOLIA = "#F8F0FB"


class GUserInterface(tk.Tk):
    itemList = []

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Bar Code Reader")
        self.geometry("800x1000")
        self.maxsize(width=800, height=1000)
        photo = PhotoImage(file="ok.png")
        self.ok_photo = photo.subsample(3, 3)

        self.topFrame = Frame(self, bg=GOLD, height=100)
        self.rightFrame = Frame(self, bg=GOLD, height=800, width=680, bd=3)
        leftFrame = Frame(self, bg=GOLD, height=800, width=100, bd=3)
        # self.topFrame.grid_propagate(0)

        self.rightLabel = LabelFrame(self.rightFrame, text="Bonul curent", width=677, height=794,
                                     font=('Helvetica 18 bold'))
        self.rightLabel.grid(column=0, row=0, sticky=NSEW)
        self.rightLabel.grid_propagate(0)

        self.totalLabel = Label(self.topFrame, text="Total:   0 RON", font=('Helvetica 30 bold'), bg=GOLD, fg='white')
        self.totalLabel.grid(column=0, row=0, padx=10, pady=30)
        achitaButton = Button(self.topFrame, text='Finalizeaza', image=self.ok_photo, border=0)
        achitaButton.grid(column=1, row=0, padx=30)
        self.restLabel = Label(self.topFrame, text="Rest:    0 RON", font=('Helvetica 30 bold'), bg=GOLD, fg='white')
        self.restLabel.grid(column=2, row=0, padx=30, pady=30)
        self.restLabel.grid_forget()

        self.topFrame.grid(column=0, row=0, columnspan=2, pady=5, sticky=EW)
        leftFrame.grid(ipadx=5, column=0, row=1)
        self.rightFrame.grid(ipadx=5, column=1, row=1, padx=5)
        photo = PhotoImage(file="cancel.png")
        self.cancel_photo = photo.subsample(3,4)

    def read_items(self, path: str):
        with open(path, mode="r") as file:
            for line in file:
                produs = line.strip().split(",")
                self.itemList.append(produs)

    def print_items(self):
        self.erase_bon()
        for produs in self.itemList:
            index = self.itemList.index(produs)
            itemNameLabel = Label(self.rightLabel, text=produs[0], font='Helvetica 16')
            itemNameLabel.grid(column=0, row=index, padx=5, pady=5, sticky=W, columnspan=4)
            cantitateLabel = Label(self.rightLabel, text=f"{produs[2]} {produs[3]} x", font='Helvetica 16')
            cantitateLabel.grid(column=4, row=index, padx=5, pady=5, sticky=E, columnspan=1)
            pretLabel = Label(self.rightLabel, text=f"{produs[1]} RON =", font='Helvetica 16')
            pretLabel.grid(column=5, row=index, padx=5, pady=5, sticky=E, columnspan=1)
            total_string = f"{float(produs[1]) * float(produs[2]):.2f} RON"
            totalLabel = Label(self.rightLabel, text=total_string, font='Helvetica 16')
            totalLabel.grid(column=6, row=index, padx=5, pady=5, sticky=E, columnspan=1)
            delete_button = Button(self.rightLabel, image=self.cancel_photo, border=0,
                                   command=lambda index=index: self.delete_items(index))
            delete_button.image = self.cancel_photo
            delete_button.grid(column=7, row=index, padx=5, pady=5, sticky=E, columnspan=1)
        self.calculate_total()

    def delete_items(self, index):
        self.itemList.remove(self.itemList[index])
        self.print_items()
        self.calculate_total()

    def erase_bon(self):
        for widget in self.rightLabel.winfo_children():
            widget.destroy()

    def calculate_total(self):
        total = 0
        for produs in self.itemList:
            total += float(produs[1]) * float(produs[2])
        # total = round(total, 2)
        self.totalLabel.config(text=f"Total:  {total:.2f} RON")


app = GUserInterface()
app.read_items("items.txt")
app.print_items()
app.mainloop()
