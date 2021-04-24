from tkinter import *
import tkinter.messagebox as tsmg
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
import time as tm
root =Tk()
root.geometry("1080x1080")
root.title("notepad")
root.wm_iconbitmap("Notepad++.ico")
def openfile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()
def savefile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
        if file =="":
            file = None

        else:
            #Save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()

def exit():
    choice=tsmg.askokcancel("exit","Are you sure you want to exit")
    if choice== True:
        quit()
    else:
        pass
def timedate():
    currenttime=tm.strftime('%I:%M:%S:%p')
    print(currenttime)
    choice=tsmg.askquestion("time ",f"{currenttime} ")
    print(choice)
def cut():
    TextArea.event_generate(("<<Cut>>"))
def copy():
    TextArea.event_generate(("<<Copy>>"))
def paste():
    TextArea.event_generate(("<<Paste>>"))
def about():
     tsmg.showinfo("information","This notepad is created by Jitendta lodhi ")
scrollbar =Scrollbar(root)
scrollbar.pack(fill=BOTH,side = RIGHT)
TextArea =Text(root,font="lucida 20 bold",yscrollcommand=scrollbar.set)
file= None
# here expand = true and fill = both fill the text widget on full screen
TextArea.pack(expand=True,fill=BOTH)
scrollbar.config(command=TextArea.yview)
mymenu=Menu(root)
m1=Menu(mymenu,tearoff=0)
m1.add_command(label="save",command=savefile)
m1.add_command(label="open",command=openfile)
m1.add_separator()
m1.add_command(label="Exit",command=exit)
root.config(menu=mymenu)
mymenu.add_cascade(label="File",menu=m1)
m2=Menu(mymenu,tearoff=0)
m2.add_command(label="Date/Time",command=timedate)
m2.add_separator()
m2.add_command(label="cut",command=cut)
m2.add_command(label="copy",command=copy)
m2.add_command(label="paste",command=paste)
root.config(menu=mymenu)
mymenu.add_cascade(label="Edit",menu=m2)
mymenu.add_command(label="About",command = about)
root.mainloop()