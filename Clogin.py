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


#configuracio perfil usuari

"""
from asyncio import base_futures
from cProfile import label
from dataclasses import field
from re import L, T
from tkinter import *
from turtle import bgcolor, left

menu_configuracio = Tk()
menu_configuracio.geometry("500x600")
menu_configuracio.resizable(0,0)
menu_configuracio.title("Configuració General")
menu_configuracio.config(bg="#8cb3ff")

imatge_menu_configuracio = PhotoImage(file="contactes.png")
imatge_menu_configuracio = imatge_menu_configuracio.subsample(3)

menu_imatge_configuracio = Label(menu_configuracio, image=imatge_menu_configuracio, bg="#8cb3ff")
menu_imatge_configuracio.place(x=0, y=50)

espai_titol_configuracio = Frame(menu_configuracio, width=500, height=55, relief="solid", borderwidth=2, bg="#4682B4",)
espai_titol_configuracio.place(x=0, y=0)

ajustes = PhotoImage(file="botoajustes.png")
ajustes = ajustes.subsample(23)

imatge_ajustes_menu_usuari = Label(espai_titol_configuracio, image=ajustes, bg="#4682b4")
imatge_ajustes_menu_usuari.place(x=70, y=12)

nom_titol_configuracio = Label(espai_titol_configuracio, text="CONFIGURACIÓ GENERAL", font=("THIN", 18, "bold"), bg="#4682b4", fg="white")
nom_titol_configuracio.place(x=100, y=7)

nom_usuari_configuracio = Label(menu_configuracio, text="Usuari", font=("THIN", 18, "bold"), bg="#8cb3ff")
nom_usuari_configuracio.place(x=200, y=80)

canviar_estat = Menubutton(menu_configuracio, text="Canviar estat", font=("THIN", 12, "bold"), bg="#606fff", cursor="hand2", fg="#ffee04", activebackground="#ffff98", activeforeground="#606fff")
canviar_estat.place(x=200, y=150)

estat_usuari = Label(menu_configuracio, bg="#8cb3ff", fg="white", font=("THIN", 14, "bold"), cursor="hand2")
estat_usuari.place(x=335, y=150)
def estats(valor):
    global estat_usuari
    estat_usuari.config(text=valor)

menu_estat = Menu(canviar_estat, tearoff=False, bg="#606fff", fg="white")

menu_estat.add_radiobutton(label="Desconnectat", font=("THIN", 12, "bold"), command= lambda:estats("Desconnectat"))
menu_estat.add_radiobutton(label="Connectat", font=("THIN", 12, "bold"),command= lambda:estats("Connectat"))
menu_estat.add_radiobutton(label="Treballant", font=("THIN", 12, "bold"), command= lambda:estats("Treballant"))
menu_estat.add_radiobutton(label="Estic en l'escola", font=("THIN", 12, "bold"), command= lambda:estats("Estic a l'escola"))
menu_estat.add_radiobutton(label="No molestis", font=("THIN", 12, "bold"), command= lambda:estats("No molestis"))
canviar_estat["menu"] = menu_estat

titol_canviar_tema = Label(menu_configuracio, text="Canviar tema", font=("THIN", 12, "bold"), bg="#8cb3ff")
titol_canviar_tema.place(x=45, y=250)

canviar_nom_usuari = Label(menu_configuracio, text="Canviar el teu nom", font=("THIN", 12, "bold"), bg="#8cb3ff")
canviar_nom_usuari.place(x=45, y=320)

entry_canviar_nom = Entry(menu_configuracio, width=20, borderwidth=1, relief="solid", font=("THIN", 14))
entry_canviar_nom.place(x=230, y=323)

boto_canviar_nom_usuari = Button(menu_configuracio, text=">>", font=("THIN", 10, "bold"), borderwidth=0, cursor="hand2", activebackground="#ffff98",fg="#ffee04", bg="#606fff", activeforeground="#606fff")
boto_canviar_nom_usuari.place(x=465, y=323)

canviar_contrasenya = Label(menu_configuracio, text="Canviar contrasenya", font=("THIN", 12, "bold"), bg="#8cb3ff")
canviar_contrasenya.place(x=45, y=390)

clau = PhotoImage(file="clau.png")
clau = clau.subsample(20)

imatge_clau = Label(menu_configuracio, image=clau, bg="#8cb3ff")
imatge_clau.place(x=2, y=390)

imatge_usuaris = PhotoImage(file="usuari.png")
imatge_usuaris = imatge_usuaris.subsample(22)

foto_usuaris = Label(menu_configuracio, image=imatge_usuaris, bg="#8cb3ff")
foto_usuaris.place(x=2, y=316)

entry_canviar_contrasenya = Entry(menu_configuracio, width=20, borderwidth=1, relief="solid", font=("THIN", 14))
entry_canviar_contrasenya.place(x=230, y=392)
entry_canviar_contrasenya.config(show="*")

boto_canviar_contrasenya = Button(menu_configuracio, text=">>", font=("THIN", 10, "bold"), borderwidth=0, cursor="hand2", activebackground="#ffff98",fg="#ffee04", bg="#606fff", activeforeground="#606fff")
boto_canviar_contrasenya.place(x=465, y=393)

llista_usuaris_bloquejats = Button(menu_configuracio, text= " Usuaris Bloquejats", font=("THIN", 16, "bold"), borderwidth=0, cursor="hand2", activebackground="#ffff98",fg="#ffee04", bg="#606fff", activeforeground="#606fff", bitmap="error", compound="left")
llista_usuaris_bloquejats.place(x=150, y=500)

linia_separar_ajustes = Frame(menu_configuracio, width=500, height=2, relief="solid", bg="black")
linia_separar_ajustes.place(x=0, y=220)

camera = PhotoImage(file="camera.png")
camera = camera.subsample(45)

imatge_camera = Label(menu_configuracio, image=camera, bg="#8cb3ff")
imatge_camera.place(x=2, y=245)

boto_clar_tema = Button(menu_configuracio, borderwidth=1, cursor="hand2", relief="solid", width=3, height=1)
boto_clar_tema.place(x=230, y=250)

boto_blau_tema = Button(menu_configuracio, borderwidth=1, cursor="hand2", relief="solid", width=3, height=1, bg="blue")
boto_blau_tema.place(x=258, y=250)

boto_verd_tema = Button(menu_configuracio, borderwidth=1, cursor="hand2", relief="solid", width=3, height=1, bg="green")
boto_verd_tema.place(x=287, y=250)

boto_fosc_tema = Button(menu_configuracio, borderwidth=1, cursor="hand2", relief="solid", width=3, height=1, bg="black")
boto_fosc_tema.place(x=316, y=250)

boto_vermell_tema = Button(menu_configuracio, borderwidth=1, cursor="hand2", relief="solid", width=3, height=1, bg="red")
boto_vermell_tema.place(x=345, y=250)

boto_groc_tema = Button(menu_configuracio, borderwidth=1, cursor="hand2", relief="solid", width=3, height=1, bg="yellow")
boto_groc_tema.place(x=374, y=250)

boto_lila_tema = Button(menu_configuracio, borderwidth=1, cursor="hand2", relief="solid", width=3, height=1, bg="purple")
boto_lila_tema.place(x=403, y=250)

boto_taronja_tema = Button(menu_configuracio, borderwidth=1, cursor="hand2", relief="solid", width=3, height=1, bg="orange")
boto_taronja_tema.place(x=432, y=250)

menu_configuracio.mainloop()"""