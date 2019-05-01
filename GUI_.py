from Tkinter import *
# the main GUI
class MainGUI(Frame):
    # the constructor
    def __init__(self, parent):
        Frame.__init__(self, parent, bg ="black")
        parent.attributes("-fullscreen", True)

        self.setupGUI()

    def setupGUI(self):
        self.display = Label(self, text="", anchor=E, bg="white", height=1, font=("TexGyreAdventor", 45))
        # put it in the top row, spanning across all four columns;
        # and expand it on all four sides
        self.display.grid(row=0, column=0, columnspan=4, sticky=E+W+N+S)

        for row in range(6):
                Grid.rowconfigure(self, row, weight=1)
                
        # there are 4 columns (0 through 3)
        for col in range(5):
            Grid.columnconfigure(self, col, weight=1)

        # start
        img = PhotoImage(file="images/add.gif")
        button = Button(self, image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("+"))
        button.image = img
        button.grid(row=2, column=2, sticky=N+S+E+W)

        # sound
        img = PhotoImage(file="images/add.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("+"))
        button.image = img
        button.grid(row=3, column=2, sticky=N+S+E+W)

        # quit
        img = PhotoImage(file="images/add.gif")
        button = Button(self, bg="black", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("+"))
        button.image = img
        button.grid(row=5, column=2, sticky=N+S+E+W)

        
        # pack the GUI
        self.pack(fill=BOTH, expand=1)

        

    def start_game():
        pass

    # toggle on/off sound
    def sound():
        pass

    
##############################
# the main part of the program
##############################
# create the window
window = Tk()
# set the window title
window.title("GUI")
# generate the GUI
p = MainGUI(window)
# display the GUI and wait for user interaction
window.mainloop()
