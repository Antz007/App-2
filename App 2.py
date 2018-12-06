import tkinter
import time

window = tkinter.Tk()
window.title("Question Generater")
window.geometry("300x330")
window.configure(bg="dimgrey")


def home():
    global btnhome
    btnhome.pack_forget()
    btnhistory.pack()
    btnhistory_fact1.pack_forget()
    btnmaths.pack()
    btnsports.pack()
    btngames.pack()
    btnmaths_fact1.pack_forget()
    btnmaths_fact_rid.pack_forget()
    lblmaths1_fact.pack_forget()
    btnleave.pack()


def maths():
    global btnhome
    btnmaths.pack()
    btnmaths_fact1.pack()
    btnleave.pack_forget()
    btngames.pack_forget()
    btnmaths_fact1.configure(text = "click here for a maths fact",command = maths_fact1)
    btnhome= tkinter.Button(window, text = "home", command = home)
    btnhome.pack()
    btnmaths.pack()
    btnmaths_fact1.pack()
    btnhistory.pack_forget()
    btnsports.pack_forget()


def maths_fact1():
    global btnhome
    lblmaths1_fact.configure(text = "blahahahahah ")


def maths_fact_rid():
    global btnhome
    btnmaths_fact_rid.configure(text = "Click here to make the fact go away")
    lblmaths1_fact.pack_forget()


def history():
    global btnhome
    btnhistory.pack()
    btnmaths.pack_forget()
    btngames.pack_forget()
    btnleave.pack_forget()
    btnhistory.configure(text = "history",command = history)
    btnhome = tkinter.Button(window, text = "home", command = home)
    btnhome.pack()
    btnsports.pack()
    btnmaths.pack_forget()
    btnsports.pack_forget()

    
def sports():
    global btnhome
    btnsports.pack()
    btnmaths_fact1.pack_forget()
    btngames.pack_forget()
    btnleave.pack_forget()
    btnsports.configure(text = "Sports",command = sports)
    btnhome= tkinter.Button(window, text = "home", command = home)
    btnhome.pack()
    btnsports.pack()
    btnmaths.pack_forget()
    btnhistory.pack_forget()


def games():
    global btnhome
    btngames.pack()
    btnmaths_fact1.pack_forget()
    btnleave.pack_forget()
    btngames.configure(text = "Games",command = games)
    btnhome= tkinter.Button(window, text = "home", command = home)
    btnhome.pack()
    btngames.pack()
    btnmaths.pack_forget()
    btnhistory.pack_forget()
    btnsports.pack_forget()

    
def leave():
    btnleave.configure(text = "Quit", command = leave)
    quit()


btnmaths = tkinter.Button(window, text = "maths", command = maths)
btnmaths_fact1 = tkinter.Button(window, text = "click here for a maths fact")
btnmaths_fact_rid = tkinter.Button(window, text = "Click here to get rid of the fact", command = maths_fact_rid)
lblmaths1_fact = tkinter.Label(window, text = "", bg = 'dimgrey')
btnhistory = tkinter.Button(window, text = "history", command = history)
btnhistory_fact1 = tkinter.Button(window, text = "click here for a history fact")
btnsports = tkinter.Button(window, text = "Sports", command = sports)
btngames = tkinter.Button(window, text = "Games", command = games)
btnleave = tkinter.Button(window, text = "Quit", command = leave)


btnmaths.pack()
btnhistory.pack()
btnsports.pack()
btngames.pack()
btnleave.pack()
lblmaths1_fact.pack()
btnmaths_fact_rid()


window.mainloop()
