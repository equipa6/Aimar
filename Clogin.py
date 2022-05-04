import configparser
from tkinter import *
from tkinter import ttk
import socket
import threading

ventana = Tk()
ventana.geometry("400x600")
ventana.resizable(0,0)
ventana.title("Registra't")
ventana.config(bg="#ccdadd")

logoclogin = PhotoImage(file="logo.png")
zoom_logo = logoclogin.subsample(7)
photo = Label(ventana, image=zoom_logo, bg="#ccdadd")
photo.place(x=125, y=0)

nomusuari = Label(ventana, text="Nom d'usuari", font=("Calibri", 18), bg="#ccdadd")
nomusuari.place(x=128, y=155)

password = Label(ventana, text="Contrasenya", font=("Calibri", 18), bg="#ccdadd")
password.place(x=130, y=250)

inpnom = ttk.Entry(ventana, font=("Calibri", 18), width=28)
inpnom.place(x=28, y=205)

inpcontrasenya = ttk.Entry(ventana, font=("Calibri", 18), width=28)
inpcontrasenya.place(x=28, y=295)
inpcontrasenya.config(show="*")

confirmaciopassword = Label(ventana, text="Repeteix la contrasenya", font=("Calibri", 18), bg="#ccdadd")
confirmaciopassword.place(x=85, y=345)

inpconfirmaciocontrasenya = ttk.Entry(ventana, font=("Calibri", 18), width=28)
inpconfirmaciocontrasenya.place(x=28, y=395)
inpconfirmaciocontrasenya.config(show="*")

imagensingup = PhotoImage(file="register.png")
imgagensingup = imagensingup.subsample(2)
botonsingup = Button(ventana, image=imgagensingup, borderwidth=0, bg="#ccdadd", cursor="hand2")
botonsingup.place(x=95, y=475)




ventana.mainloop()