from tkinter import *
import tkinter as tk
from tkinter import messagebox
import random

score = {'computer':0, 'Player':0}
choises = ['Πέτρα', 'Ψαλίδι', 'Χαρτί']



t = "-"
top = Tk()
top.geometry("610x500")
top.title("Πέτρα,Ψαλίδι,Χαρτί")

photo1 = PhotoImage(file = r"foto\petra1.png") 
photo2 = PhotoImage(file = r"foto\psalidi1.png") 
photo3 = PhotoImage(file = r"foto\xarti1.png") 
 

def CH_1():
    choise = 0
    img1 = Label(top, image = photo1).place(x = 0,y = 250)
    show_result(choise)
    
     
def CH_2():
    choise = 1
    img2 = Label(top, image = photo2).place(x = 0,y = 250)
    show_result(choise)
   
def CH_3():
    choise = 2
    img3 = Label(top, image = photo3).place(x = 0,y = 250)
    show_result(choise)
    

def show_result(choise):
    global t
    computer_choise = random.randrange(3)
    
    if computer_choise == 0:
        img4 = Label(top, image = photo1).place(x = 400,y = 250)
    if computer_choise == 1:
        img5 = Label(top, image = photo2).place(x = 400,y = 250)
    if computer_choise == 2:
        img6 = Label(top, image = photo3).place(x = 400,y = 250)

    if choise == computer_choise :
        print('>>>> Ισσοπαλία <<<<')
        t = "Ισσοπαλία"
        apot.set(t)
        return
    if choise - computer_choise == -1 or choise - computer_choise == 2 :
        print('>>>> Κερδίσατε <<<<')
        t = "Κερδίσατε"
        apot.set(t)
        score['Player'] += 1
        scoru.set(score['Player'])
        return
    
    print('>>>>   Χάσατε   <<<<')
    t = "Χάσατε"
    apot.set(t)
    score['computer'] += 1
    scorc.set(score['computer'])

  


B1 = Button(top, text = "Πέτρα", command = CH_1, image = photo1, compound = TOP).place(x = 0,y = 0)
B2 = Button(top, text = "Ψαλίδι", command = CH_2, image = photo2, compound = TOP).place(x = 200,y = 0)
B3 = Button(top, text = "Χαρτί", command = CH_3, image = photo3, compound = TOP).place(x = 400,y = 0)


apot = StringVar()
apot.set("")
apotLb1 = Label(top, textvariable = apot, font =('Verdana', 25)).place(relx=0.5, rely=0.7, anchor=CENTER)


scorc = StringVar()
scorc.set(score['computer'])
cLb1 = Label(top, textvariable = scorc, font =('Verdana', 25)).place(x = 500,y = 400)


scoru = StringVar()
scoru.set(score['Player'])
uLb1 = Label(top, textvariable = scoru, font =('Verdana', 25)).place(x = 100,y = 400)

uLb2 = Label(top, text = 'Player', font =('Verdana', 25)).place(x = 50,y = 170)
cLb2 = Label(top, text = 'computer', font =('Verdana', 25)).place(x = 440,y = 170)

top.mainloop()
