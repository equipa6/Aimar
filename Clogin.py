from email.mime import image
from tkinter import *
import socket
import threading
from tkinter.font import BOLD
from turtle import width



def registredesessio():
    global inpconfirmaciocontrasenya
    global inpcontrasenya
    global ventana
    root.destroy()
    ventana = Tk()
    ventana.geometry("400x600")
    ventana.geometry("+475+50")
    ventana.resizable(0,0)
    ventana.title("Registra't")
    ventana.config(bg="#FFFFFF")

    logoclogin = PhotoImage(file="logo.png")
    zoom_logo = logoclogin.subsample(7)
    photo = Label(ventana, image=zoom_logo, bg="#FFFFFF")
    photo.place(x=125, y=0)

    nomusuari = Label(ventana, text="Nom d'usuari", font=("THIN", 16), bg="#FFFFFF")
    nomusuari.place(x=135, y=170)

    password = Label(ventana, text="Contrasenya", font=("THIN", 16), bg="#FFFFFF")
    password.place(x=135, y=260)

    inpnom = Entry(ventana, font=("Calibri", 18), width=28, borderwidth=1, relief="solid", bg="#ffee04")
    inpnom.place(x=28, y=205)

    inpcontrasenya = Entry(ventana, font=("Calibri", 18), width=28, borderwidth=1, relief="solid", bg="#ffee04")
    inpcontrasenya.place(x=28, y=295)
    inpcontrasenya.config(show="*")

    confirmaciopassword = Label(ventana, text="Repeteix la contrasenya", font=("THIN", 16), bg="#FFFFFF")
    confirmaciopassword.place(x=80, y=360)

    inpconfirmaciocontrasenya = Entry(ventana, font=("Calibri", 18), width=28, borderwidth=1, relief="solid", bg="#ffee04")
    inpconfirmaciocontrasenya.place(x=28, y=395)
    inpconfirmaciocontrasenya.config(show="*")

    botonsingup = Button(ventana, text="Registra't", fg="#ffee04", bg="#606fff", cursor="hand2", font=("Calibri", 15, "bold"), width=18, borderwidth=0, command=confirmacio_contrasenya)
    botonsingup.place(x=108, y=475)

    imatgeenrere = PhotoImage(file="enrere.png")
    imatgeenrere = imatgeenrere.subsample(10)

    enrere = Button(ventana, command=inicidesessio, image = imatgeenrere, borderwidth=0, bg="#FFFFFF", cursor="hand2")
    enrere.place(x=12, y=20)

    ventana.mainloop()

def inicidesessio():
    global root
    try:
        ventana.destroy()
    except:
        pass
    root = Tk()
    root.geometry("400x600")
    root.geometry("+475+50")
    root.resizable(0,0)
    root.title("Iniciar sessió")
    root.config(bg="#FFFFFF")
    

    logo_clogin = PhotoImage(file="logo.png")
    zoom = logo_clogin.subsample(7)
    foto = Label(root, image=zoom, bg="#FFFFFF")
    foto.place(x=125, y=0)

    nom_usuari = Label(root, text="Nom d'usuari", font=("THIN", 16), bg="#FFFFFF")
    nom_usuari.place(x=135, y=165)

    contrasenya = Label(root, text="Contrasenya", font=("THIN", 16), bg="#FFFFFF")
    contrasenya.place(x=135, y=265)

    inp_nom = Entry(root, font=("Calibri", 18), width=28, borderwidth=1, relief="solid", bg="#ffee04")
    inp_nom.place(x=28, y=200)

    inp_contrasenya = Entry(root, font=("Calibri", 18), width=28, borderwidth=1, relief="solid", bg="#ffee04")
    inp_contrasenya.place(x=28, y=300)
    inp_contrasenya.config(show="*")

    boton_singup = Button(root, text="Entra", fg="#ffee04", bg="#606fff", cursor="hand2", font=("Calibri", 15, "bold"), width=18, borderwidth=0)
    boton_singup.place(x=105, y=370)

    lab_register = Label(root, text="No tens compte?", font=("THIN", 14, "underline"), bg="#FFFFFF")
    lab_register.place(x=35, y=530)

    foto_register = PhotoImage(file="register.png")
    foto_register = foto_register.subsample(2)

    button_register = Button(root, text="Registra't", fg="#ffee04", bg="#606fff", cursor="hand2", font=("Calibri", 15, "bold"), width=16, borderwidth=0, command=registredesessio)
    button_register.place(x=195, y=525)
    
    root.mainloop()

def confirmacio_contrasenya():
    respostaconfirmacio = inpconfirmaciocontrasenya.get()
    respostacontrasenya = inpcontrasenya.get()

    if respostaconfirmacio != respostacontrasenya:
        error = Label(ventana, text="Les contrasenyes no coincideixen", font=("Calibri", 12, "bold"), fg="red", bg="#FFFFFF")
        error.place(x= 88, y= 430)  

inicidesessio()



