import random
from tkinter import *
from random import choice

sweaty = ['Rainbow Six Siege', 'Apex Legends', 'Rocket League', 'CS:GO', ]
chill = ['Stardew Valley', 'Trials Rising', 'Game Of Life 2']
randgame = []

def Create_Choice():
    
 GameChoice = Tchoice.get()
 randgame.append(choice(GameChoice))
 
 gameselected.delete(0.0, END)
 gameselected.insert(END, randgame)
 

window = Tk()
window.geometry("800x500")
window.title("RNGameSelector")
Progname = Label(window, font=('Arial', 50, 'bold'), text="RNGame", fg="Black")
Progname.grid(row=1, column=3, padx=250, pady=0)
ChooseType = Label(window, font=('Arial', 25, 'bold'), text="Choose a type")
ChooseType.place(relx=.01, rely=.25)

Tchoice = StringVar()
sweatychoice = Radiobutton(window, font=(
    'corbel', 18, 'italic'), text="Sweaty", variable=Tchoice, value=sweaty)
sweatychoice.place(relx=.025, rely=.35)
chillchoice = Radiobutton(window, font=(
    'corbel', 18, 'italic'), text="Chill", variable=Tchoice, value=chill)
chillchoice.place(relx=.025, rely=.45)


button = Button(window, font=('Arial', 20, 'bold'),
                text='Random', command=Create_Choice)
button.place(relx=.4, rely=.6)


gameselected = Text(window, height=6, width=70)
gameselected.place(relx=.140, rely=.75)





window.mainloop()
