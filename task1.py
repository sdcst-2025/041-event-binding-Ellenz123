import tkinter as tk
from tkinter import PhotoImage
import playsound as p


window = tk.Tk()
window.attributes('-topmost',True)
window.title("Birds Sound Board")
window.geometry("600x400")

def playsound(event):
    print(event)
    p.playsound("Tufted Titmouse.mp3")
photo1 = PhotoImage(file="Tufted-Titmouse1.png")
photo1=photo1.subsample(6,6)
label1 = tk.Label(window, image=photo1)
label1.place(x=0,y=20)
b1 =  tk.Button(window,text="Click to play")
b1.bind("<Button>",playsound)
b1.place(x=40,y=140)
label2 = tk.Label(window,text="Tufted Titmouse", width=20)
label2.place(x=10,y=0)

def playsound(event):
    print(event)
    p.playsound("Prothonotary Warbler.mp3")
photo2 = PhotoImage(file="Prothonotary-Warbler1.png")
photo2=photo2.subsample(7,9)
label2 = tk.Label(window, image=photo2)
label2.place(x=190,y=20)
label3 = tk.Label(window,text="Prothonotary Warbler", width=20)
label3.place(x=200,y=0)
b2 =  tk.Button(window,text="Click to play")
b2.bind("<Button>",playsound)
b2.place(x=220,y=140)

def playsound(event):
    print(event)
    p.playsound("Roseate Tern.mp3")
photo3 = PhotoImage(file="Roseate Tern.png")
photo3=photo3.subsample(3,3)
label3 = tk.Label(window, image=photo3)
label3.place(x=350,y=20)
label4 = tk.Label(window,text="Roseate Tern", width=20)
label4.place(x=360,y=0)
b3 =  tk.Button(window,text="Click to play")
b3.bind("<Button>",playsound)
b3.place(x=400,y=145)


window.mainloop()