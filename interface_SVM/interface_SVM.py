#!/usr/bin/env python
# coding: utf-8

# In[30]:


import tkinter.filedialog
import tkinter as tk
from tkinter import ttk
from tkinter import * 
import tkinter.font as font
from tkinter.filedialog import askopenfilename
import os
import webbrowser
from tkinter.messagebox import showinfo

def onSave():
    print(filedialog.asksaveasfilename(initialdir = "/",title = "Save as",filetypes = (("Python files","*.py;*.pyw"),("All files","*.*"))))
           
def onOpen():
    #print(filedialog.askopenfilename(initialdir = "/",title = "Open file",filetypes = (("Python files","*.py;*.pyw"),("All files","*.*")))) 
    rep = filedialog.askopenfilenames(
    	parent=fp,
    	initialdir='/',
    	initialfile='tmp',
    	filetypes=[
    		("Python", ["*.py","*.ipynb"]),
      		("Pdf", "*.pdf"),
    		("Text", "*.txt"),
    		("All files", "*")])
    print(rep)
    try:
	    os.startfile(rep[0])
    except IndexError:
        print("No file selected")


def openbtn1():    
    webbrowser.open_new(r"SVM_doc2.pdf")
def openbtn2():    
    webbrowser.open_new(r"SVM_doc1.pdf")

        

fp =Tk()


fz1 = font.Font(size=40,family='Times New Roman',weight="bold")
fz2 = font.Font(size=15,family='Times New Roman',weight="bold")

p = PanedWindow(fp, orient=HORIZONTAL)

F1 = Frame(fp, bg='gold', bd=5,relief = RAISED)
Label(F1,text='',borderwidth = 5,font=("Courier", 20,"bold")).pack(side=LEFT)
Label(F1,text="Faculté des Sciences Economiques et de Gestion de Sfax (FSEGS)",fg="red",borderwidth = 5,font=("Courier", 20,"bold")).pack(side=TOP)
F1.pack(side=TOP)
F1.pack(fill=tk.BOTH, expand=False)



F2 = Frame(fp, bg='gold', bd=5,relief = RAISED)
Label(F2,text='Supprt Vector Machine (SVM)',borderwidth = 5,font=("Courier", 20,"bold")).pack(side=TOP)
#F2.pack(side=TOP)
#F2.pack(fill=tk.BOTH, expand=True)
F2.pack(padx=100)


Frame3 = Frame(fp,borderwidth=1,relief=GROOVE)
Label(Frame3).pack(fill=tk.BOTH)
Frame3.pack(side=LEFT)
Frame3.pack(fill=tk.BOTH, expand=True)

Frame4 = Frame(fp,borderwidth=2,relief=GROOVE)
Label(Frame4,text="",font=("Courier", 20,"bold")).pack(fill=tk.BOTH)
Frame4.pack(side=RIGHT)
Frame4.pack(fill=tk.BOTH, expand=True)

tkinter.Label (Frame4, text = "Projet : Support Vector Machine (SVM)",bg="light yellow",fg='DodgerBlue2',font=("Courier", 20,"bold")).pack(pady=20, side= TOP, anchor="w")
#l1.pack (side=TOP) # positionne l à l'intérieur de Frame4

tkinter.Label (Frame4, text = "Présenté par : Tahar ALIMI",bg="light yellow",fg='DodgerBlue2',font=("Courier", 20,"bold")).pack(pady=20, side= TOP, anchor="w")
#l3.pack (side=TOP) # positionne l à l'intérieur de Frame4

tkinter.Label (Frame4, text = "Classe : Master de Recherche SINT (M1)",bg="light yellow",fg='DodgerBlue2',font=("Courier", 18,"bold")).pack(pady=20, side= TOP, anchor="w")
#l2.pack (side=TOP) # positionne l à l'intérieur de Frame4

tkinter.Label (Frame4, text = "Proposé par : Prof. Yassine Ben Ayed",bg="light yellow",fg='DodgerBlue2',font=("Courier", 18,"bold")).pack(pady=20, side= TOP, anchor="w")
#l4.pack (side=TOP) # positionne l à l'intérieur de Frame4

tkinter.Label (Frame4, text = "Année Académique : 2020/2021",bg="light yellow",fg='DodgerBlue2',font=("Courier", 10,"bold")).pack(pady=20, side= BOTTOM, anchor="c")

btn1=Button(Frame3,text="SVM Analysis 1 : Training dataset \n&&\n sklearn module ",width=20,borderwidth = 5,font=("Courier", 15,"bold"),fg='tomato',bg="lightblue1",command = openbtn1).pack(side=TOP,fill=tk.BOTH)
#Algo1.pack()

btn2=Button(Frame3,text="SVM Analysis 2 : Different Algorithms",borderwidth = 3,font=("Courier", 15,"bold"),fg='tomato',bg="lightblue1",command = openbtn2).pack(side=TOP,fill=tk.BOTH)


fp.title('Support Vector Machine') # Ajout d'un titre
fp.resizable(True, True) # autoriser le redimensionnement vertical et horizontal
fp.geometry("1072x800+80+50")#dimensionner et positionner la fnêtre

menubar = Menu(fp)
menufile = Menu(menubar,tearoff=0)
menufile.add_command(label="Open ",command=onOpen)
menufile.add_separator()

menufile.add_command(label="Save",command=onSave)
menufile.add_separator()


menufile.add_command(label="Save as")
menufile.add_separator()


menufile.add_command(label="Quit", command=fp.destroy) 
menufile.add_separator()

menubar.add_cascade(label="File", menu=menufile)

menuedition = Menu(menubar,tearoff=0)

def alert():
    showinfo("alerte", "Thank You!")


menuedition.add_command(label="Cut")
menuedition.add_separator()

menuedition.add_command(label="Copy")
menuedition.add_separator()

menuedition.add_command(label="Past")
menuedition.add_separator()

menuedition.add_cascade(label="Edit")
menuedition.add_separator()

menubar.add_cascade(label="Edit", menu=menuedition)

menuhelp = Menu(menubar, tearoff=0)
menuhelp.add_command(label="About !", command=alert)
menubar.add_cascade(label="Help", menu=menuhelp)


fp.config(menu=menubar)

p.pack()
fp.mainloop()


# In[ ]:





# In[ ]:




