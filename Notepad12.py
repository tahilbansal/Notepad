from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def open1():
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                      ("Text Documents", "*.txt")])
    root.title(os.path.basename(file) + " - Notepad")
    text.delete(1.0, END)
    f = open(file, "r")
    text.insert(1.0, f.read())
    f.close()

def save():
    file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt",
                             filetypes=[("All Files", "*.*"),
                                        ("Text Documents", "*.txt")])
    with open(file,"w") as f:
     f.write(text.get("1.0","end"))
     root.title(os.path.basename(file) + " - Notepad")
     print("File Saved")


def quitApp():
    root.destroy()

def cut():
    text.event_generate(("<>"))

def copy():
    text.event_generate(("<>"))

def paste():
    text.event_generate(("<>"))


root=Tk()
root.geometry("800x800")
root.title("Notepad")

mainmenu= Menu(root,tearoff=0)

m1=Menu(mainmenu,tearoff=0)
m1.add_command(label="open",command=open1)
m1.add_command(label="save",command = save)
m1.add_command(label="save As")
mainmenu.add_cascade(label="File",menu=m1)
root.config(menu=mainmenu)


EditMenu = Menu(mainmenu, tearoff=0)
#To give a feature of cut, copy and paste
EditMenu.add_command(label = "Cut", command=cut)
EditMenu.add_command(label = "Copy", command=copy)
EditMenu.add_command(label = "Paste", command=paste)

mainmenu.add_cascade(label="Edit", menu = EditMenu)

textvalue=StringVar()
text=Text(root)
text.pack(expand=TRUE,fill=BOTH)

root.mainloop()