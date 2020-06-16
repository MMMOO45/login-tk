from tkinter import *
from tkinter.messagebox import *

import sqlite3

from home import *

def root():
    global ventana_login
    global username_en
    global password_en
    ventana_login = Tk()
    ventana_login.title("Login LoopGeeks")
    ventana_login.geometry("350x320+500+250")

    img = PhotoImage(file="/Users/hever/Downloads/login-v2/img/userlogin.png")
    img = img.subsample(3,3)
    Label(ventana_login, image=img).pack()

    Label(ventana_login, text="Usuario", font="Ubuntu 15").pack()
    username_en = Entry(ventana_login, font="Ubuntu 12", justify="center")
    username_en.pack()

    Label(ventana_login, text="Contraseña", font="Ubuntu 15").pack()
    password_en = Entry(ventana_login, show="*", font="Ubuntu 12", justify="center")
    password_en.pack()

    entrar = Button(text="Login", font="Ubuntu 14", command=login)
    entrar.config(activebackground="dark blue")
    entrar.pack()

    ventana_login.mainloop()

def login():
    # Conexión a la base de datos
    db = sqlite3.connect('/Users/hever/Downloads/login-v2/login.db')
    c = db.cursor()

    usuario = username_en.get()
    contr = password_en.get()

    c.execute('SELECT * FROM usuarios WHERE usuario = ? AND pass = ?', (usuario,contr))

    if c.fetchall():
        showinfo(title="Login exitoso", message="Sesion iniciada correctamente")
        home()
    else:
        showerror(title="Ups, algo ha salido mal", message="Usuario o contraseña incorrectos")
        opcion = askretrycancel(message="¿Desea reintentar?", title="Reintentar")
        print(opcion)
        if opcion == True:
            showinfo(title="Nuevo intento", message="Introdue tus datos correctamente")
        else:
            ventana_login.destroy()

    c.close()

if __name__ == "__main__":
    root()
    