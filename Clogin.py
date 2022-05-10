from tkinter import *
import socket
import threading

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

    botonsingup = Button(ventana, text="Registra't", fg="#ffee04", bg="#606fff", cursor="hand2", font=("Calibri", 15, "bold"), width=18, borderwidth=0, command=confirmacio_contrasenya, activebackground="#ffff98", activeforeground="#606fff")
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

    boton_singup = Button(root, text="Entra", fg="#ffee04", bg="#606fff", cursor="hand2", font=("Calibri", 15, "bold"), width=18, borderwidth=0, activebackground="#ffff98", activeforeground="#606fff")
    boton_singup.place(x=105, y=370)

    lab_register = Label(root, text="No tens compte?", font=("THIN", 14, "underline"), bg="#FFFFFF")
    lab_register.place(x=35, y=530)

    button_register = Button(root, text="Registra't", fg="#ffee04", bg="#606fff", cursor="hand2", font=("Calibri", 15, "bold"), width=16, borderwidth=0, command=registredesessio, activebackground="#ffff98", activeforeground="#606fff")
    button_register.place(x=195, y=525)
    
    root.mainloop()

def confirmacio_contrasenya():
    respostaconfirmacio = inpconfirmaciocontrasenya.get()
    respostacontrasenya = inpcontrasenya.get()

    if respostaconfirmacio != respostacontrasenya:
        error = Label(ventana, text="Les contrasenyes no coincideixen", font=("Calibri", 12, "bold"), fg="red", bg="#FFFFFF")
        error.place(x= 88, y= 430)  

inicidesessio()

#Afegir usuaris


"""from tkinter import *
import socket
import threading
from turtle import bgcolor

ventana_afegir_usuaris = Tk()
ventana_afegir_usuaris.geometry("600x300")
ventana_afegir_usuaris.config(bg="#8cb3ff")
ventana_afegir_usuaris.title("Afegir usuaris")
ventana_afegir_usuaris.resizable(0,0)
ventana_afegir_usuaris.geometry("+375+125")

titol_usuaris = Label(ventana_afegir_usuaris, text="Afegir usuaris", font=("THIN", 18, "bold"), bg="#8cb3ff")
titol_usuaris.place(x=62, y=45)

introduir_nom_usuari = Label(ventana_afegir_usuaris, text="Introdueix el nom de l'usuari", font=("THIN", 16), bg="#8cb3ff")
introduir_nom_usuari.place(x=17, y= 100)


nom_afegir_usuari = Entry(ventana_afegir_usuaris, font=("Calibri", 16), borderwidth=1, relief="solid", bg="#ffee04")
nom_afegir_usuari.place(x=35, y=150)

boto_afegir_usuaris = Button(ventana_afegir_usuaris, text="Afegeix", fg="#ffee04",bg="#606fff", cursor="hand2",font=("Calibri", 13, "bold"),width=14, borderwidth=0)
boto_afegir_usuaris.place(x=78,y=210 )

imatge_usuari = PhotoImage(file="contactes.png")
tamany_imatge = imatge_usuari.subsample(2)
imatge_ventana = Label(ventana_afegir_usuaris, image=tamany_imatge, bg="#8cb3ff")
imatge_ventana.place(x=330, y=10)

ventana_afegir_usuaris.mainloop()"""