import sys
v=sys.version
#display About box
from tkinter import messagebox




if "2.7" in v:
    from tkinter import *
elif "3.8" in v or "3.8" in v:
    from tkinter import *


#save file in editor
from tkinter import filedialog
    
root=Tk("Text Editor")

root.title('CA editor')

text=Text(root)

text.grid()


def hello():
    print ("hello!")

def about():
    messagebox.showinfo("About", "Welcome to CA editor alpha version 0.1 coded by MHB 2020")
                        
def saveas():
    global text
    t = text.get("1.0", "end-1c")
    savelocation=filedialog.asksaveasfilename()
    file1=open(savelocation, "w+")
    file1.write(t)
    file1.close()

def FontHelvetica():
   
   global text
   text.config(font="Helvetica")   
   messagebox.showinfo("Font","Helvetica selected")
       
       
       

def FontCourier():

    global text
    text.config(font="Courier")
    messagebox.showinfo("Font","Courier selected")
    





menubar = Menu(root)
font=Menubutton(root, text="Font") 

# create a pulldown menu, and add it to the menu bar
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=hello)
filemenu.add_command(label="Save", command=saveas)
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

#create fontmenu
fontmenu=Menu(menubar, tearoff=0)
font["menu"]=fontmenu
helvetica=IntVar()
courier=IntVar()
fontmenu.add_checkbutton(label="Courier", variable=courier,
command=FontCourier)
fontmenu.add_checkbutton(label="Helvetica", variable=helvetica, 
command=FontHelvetica)
menubar.add_cascade(label="Font", menu=fontmenu)


helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=about)
menubar.add_cascade(label="Help", menu=helpmenu)

# display the menu
root.config(menu=menubar)

#default_font = tkFont.nametofont("TkDefaultFont")
#default_font.configure(size=48)

root.mainloop()
