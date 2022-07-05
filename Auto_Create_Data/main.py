# Import necessary libraries
from tkinter import *
from tkinter import ttk
import os
from time import *
from AutoCreateDataWithExcel import *


# create Frame class
class MainApp(Frame):

    # Constructor
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.initUI()

    # initialize UI
    def initUI(self):

        # Main frame
        self.pack(fill=BOTH, expand=True)
        self.frm_main = ttk.Frame(self, borderwidth=1)
        self.frm_main.pack(fill=BOTH, expand=True)

        # label
        self.label = ttk.Label(self.frm_main, text="Number of Data:")
        self.label.pack(fill=X, expand=True)

        # entry
        self.entry = ttk.Entry(self.frm_main)
        self.entry.pack(fill=X, expand=True)

        # button
        self.num = StringVar()
        self.num.set("0")
        self.button = ttk.Button(self.frm_main, command=self.create_Button, text="Create")
        self.button.pack(fill=X, expand=True)
    
    # method
    def create_Button(self):
        self.num = self.entry.get()
        return auto_Create_Data(self.num)
        
# create Root class
class Root(Tk):

    # Constructor
    def __init__(self):
        super().__init__()
        self.title('Auto Create Data tool')
        self.resizable(False, False)
        self.geometry('300x200')

# Main function
def main():
    root = Root()
    app = MainApp(root)
    root.mainloop()

# run main 
if __name__ == "__main__":
    main()