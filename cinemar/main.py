from tkinter import messagebox
from view.gui_main import Main
from database import database as db

try:
    base_datos = db.DataBase('cinemar.db')

    a = Main(base_datos)
    a.mainloop()

    base_datos.close()
except:
    messagebox.showerror('Error en la aplicación', 'Algo salio mal :(')