from tkinter import *
class Fenster1:
    zeilen = 10
    spalten = 10
    
    def __init__(self):
        self.fenster = Tk()

        # Buttonleiste Links
        self.frmlinks = Frame(master=self.fenster, relief=RIDGE,bd=2)
        # Buttons
        self.btnmove = Button(master=self.frmlinks, text="move")
        self.btnmove.pack(side=TOP, fill=BOTH)
        self.btnleft = Button(master=self.frmlinks, text="left")
        self.btnleft.pack(side=TOP, fill=BOTH, expand=1)
        self.btnright = Button(master=self.frmlinks, text="right")
        self.btnright.pack(side=TOP, fill=BOTH, expand=1)
        self.btnleafup = Button(master=self.frmlinks, text="L-Up")
        self.btnleafup.pack(side=TOP, fill=BOTH, expand=1)
        self.btnleafdown = Button(master=self.frmlinks, text="L-Down")
        self.btnleafdown.pack(side=TOP, fill=BOTH, expand=1)
        self.btnpilz = Button(master=self.frmlinks, text="Pilz")
        self.btnpilz.pack(side=TOP, fill=BOTH, expand=1)
        self.btntree = Button(master=self.frmlinks, text="Baum")
        self.btntree.pack(side=TOP, fill=BOTH, expand=1)

        self.frmlinks.pack(side=LEFT, anchor=NW, expand=1)
        
        # Spielfeld

        # Unterseite
        self.frmbottom = Frame(master=self.fenster, relief=RIDGE,bd=2)
        # Buttons
        self.btnstart = Button(master=self.frmbottom, text="Start")
        self.btnstart.pack(side=LEFT, fill=Y)
        self.btnstopp = Button(master=self.frmbottom, text="Stop")
        self.btnstopp.pack(side=LEFT, fill=Y)
        self.btnv = Scale(master=self.frmbottom,
        from_= 0, to=100, 
        orient=HORIZONTAL)
        self.btnv.pack(side=LEFT, fill=Y)
        
        self.frmbottom.pack(side=BOTTOM, anchor=S, fill=X, expand=1)
        
        self.fenster.mainloop()
