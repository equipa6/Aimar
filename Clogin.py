from tkinter import *
import socket
import threading

def registredesessio():
    global ventana
    root.destroy()
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

    inpnom = Entry(ventana, font=("Calibri", 18), width=28)
    inpnom.place(x=28, y=205)

    inpcontrasenya = Entry(ventana, font=("Calibri", 18), width=28)
    inpcontrasenya.place(x=28, y=295)
    inpcontrasenya.config(show="*")

    confirmaciopassword = Label(ventana, text="Repeteix la contrasenya", font=("Calibri", 18), bg="#ccdadd")
    confirmaciopassword.place(x=85, y=345)

    inpconfirmaciocontrasenya = Entry(ventana, font=("Calibri", 18), width=28)
    inpconfirmaciocontrasenya.place(x=28, y=395)
    inpconfirmaciocontrasenya.config(show="*")

    imagensingup = PhotoImage(file="register.png")
    imgagensingup = imagensingup.subsample(2)
    botonsingup = Button(ventana, image=imgagensingup, borderwidth=0, bg="#ccdadd", cursor="hand2")
    botonsingup.place(x=95, y=475)

    imatgeenrere = PhotoImage(file="enrere.png")
    imatgeenrere = imatgeenrere.subsample(10)

    enrere = Button(ventana, command=inicidesessio, image = imatgeenrere, borderwidth=0, bg="#ccdadd", cursor="hand2")
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
    root.resizable(0,0)
    root.title("Inicia sessió")
    root.config(bg="#ccdadd")

    logo_clogin = PhotoImage(file="logo.png")
    zoom = logo_clogin.subsample(7)
    foto = Label(root, image=zoom, bg="#ccdadd")
    foto.place(x=125, y=0)

    nom_usuari = Label(root, text="Nom d'usuari", font=("Calibri", 18), bg="#ccdadd")
    nom_usuari.place(x=128, y=150)

    contrasenya = Label(root, text="Contrasenya", font=("Calibri", 18), bg="#ccdadd")
    contrasenya.place(x=130, y=260)

    inp_nom = Entry(root, font=("Calibri", 18), width=28)
    inp_nom.place(x=28, y=200)

    inp_contrasenya = Entry(root, font=("Calibri", 18), width=28)
    inp_contrasenya.place(x=28, y=300)
    inp_contrasenya.config(show="*")

    imagen_singup = PhotoImage(file="singup.png")
    imgagen_singup = imagen_singup.subsample(5)
    boton_singup = Button(root, image=imgagen_singup, borderwidth=0, bg="#ccdadd", cursor="hand2")
    boton_singup.place(x=125, y=370)

    lab_register = Label(root, text="No tens compte", font=("Calibri", 14, "underline"), bg="#ccdadd")
    lab_register.place(x=50, y=530)

    foto_register = PhotoImage(file="register.png")
    foto_register = foto_register.subsample(2)
    button_register = Button(root, image=foto_register, bg="#ccdadd",borderwidth=0, command=registredesessio)
    button_register.place(x=175, y=510)

    root.mainloop()

inicidesessio()



