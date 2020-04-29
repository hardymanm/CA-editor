import sys
v=sys.version
from tkinter import messagebox

if "2.7" in v:
    from tkinter import *
elif "3.8" in v or "3.8" in v:
    from tkinter import *
root=Tk("Text Editor")

root.title('CA editor')

text=Text(root)

text.grid()


def hello():
    print ("hello!")

def about():
    messagebox.showinfo("About", "Welcome to CA editor alpha version 0.1 coded by MHB 2020")
                        
                        
  

menubar = Menu(root)

# create a pulldown menu, and add it to the menu bar
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=hello)
filemenu.add_command(label="Save", command=hello)
filemenu.add_separator()
#filemenu.add_command(label="Exit", command=root.quit)
filemenu.add_command(label="Exit", command=root.destroy)
menubar.add_cascade(label="File", menu=filemenu)

# create more pulldown menus
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Cut", command=hello)
editmenu.add_command(label="Copy", command=hello)
editmenu.add_command(label="Paste", command=hello)
menubar.add_cascade(label="Edit", menu=editmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=about)
menubar.add_cascade(label="Help", menu=helpmenu)

# display the menu
root.config(menu=menubar)

#default_font = tkFont.nametofont("TkDefaultFont")
#default_font.configure(size=48)

root.mainloop()
