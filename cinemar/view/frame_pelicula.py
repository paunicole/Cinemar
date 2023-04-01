import tkinter as tk
from tkinter import ttk, messagebox
from model.pelicula import Pelicula
from view.form_reserva import FormularioReserva
from view.form_pelicula import FormularioPelicula
from view.form_detalle_pelicula import MasDetalles

class PeliculaCliente(tk.Frame):
    def __init__(self, ventana_padre=None, master=None, cuenta_usuario=None, base_datos=None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.ventana_padre = ventana_padre
        self.cuenta_usuario = cuenta_usuario
        self.bdd = base_datos
        self.pelicula = Pelicula()

        """WIDGETS"""
        #Titulo
        self.cabecera = ttk.Label(self)
        #Tabla
        self.tabla = ttk.Treeview(self)
        #Detalles
        self.label_info = ttk.Label(self)
        self.input_info =  ttk.Combobox(self)
        self.button_info = ttk.Button(self)
        #Reservar
        self.label_reservar = ttk.Label(self)
        self.input_reservar =  ttk.Combobox(self)
        #Aceptar
        self.button_aceptar = ttk.Button(self)

        self.widgets_config()
        self.widgets_grid()
        self.input_fill()


    def tabla_config(self):
        self.tabla.config(columns = (1,2,3,4))

        self.tabla.column('#0', width=70, anchor='center')
        self.tabla.column('#1', width=180, anchor='center')
        self.tabla.column('#2', width=70, anchor='center')
        self.tabla.column('#3', width=100, anchor='center')
        self.tabla.column('#4', width=70, anchor='center')

        self.tabla.heading('#0', text='ID Pelicula', anchor='center')
        self.tabla.heading('#1', text='Nombre', anchor='center')
        self.tabla.heading('#2', text='Duracion', anchor='center')
        self.tabla.heading('#3', text='Genero', anchor='center')
        self.tabla.heading('#4', text='Tipo')

    def widgets_config(self):
        #Titulo
        self.cabecera.config(text='Peliculas Disponibles', foreground='#FFFFFF', font=('Segoe UI Black', 36), background='red')
        #Tabla
        self.tabla_config()
        #Detalles
        self.label_info.config(text='Selecciona una pelicula\npara ver más detalles', foreground='#FFFFFF', font=('Segoe UI Black', 18), background='black', justify='center')
        self.input_info.config(width=5, state='readonly')
        self.button_info.config(text='Ver Más', command=self.Detalles)
        #Reservar
        self.label_reservar.config(text='Selecciona una pelicula\npara reservar', foreground='#FFFFFF', font=('Segoe UI Black', 18), background='black', justify='center')
        self.input_reservar.config(width=10, state='readonly')
        self.button_aceptar.config(text='Aceptar', command=self.Reservar)


    def input_fill(self):
        self.tabla.delete(*self.tabla.get_children())
        ids = []
        peliculas = self.pelicula.mostrar_peliculas(self.bdd)
        
        for peli in peliculas:
            self.tabla.insert('', 'end', text=f'{peli[0]}', values=(peli[1], peli[2], peli[3], peli[4]))
            ids.append(peli[0])
        
        self.input_info.config(values=ids)
        self.input_reservar.config(values=ids)

    def widgets_grid(self):
        #Titulo
        self.cabecera.grid(row=0, column=0, columnspan=8, pady=20, ipady=10)
        #Tabla
        self.tabla.grid(row=1, column=0, rowspan=5, columnspan=5, padx=20, pady=(0, 20))
        #Detalles
        self.label_info.grid(row=2, column=5, rowspan=2, columnspan=8)
        self.input_info.grid(row=4, column=5, columnspan=2, pady=20)
        self.button_info.grid(row=4, column=7, columnspan=1, ipadx=5, ipady=5)
        #Reservar
        self.label_reservar.grid(row=6, column=1, rowspan=2, columnspan=3)
        self.input_reservar.grid(row=7, column=4, columnspan=2)
        self.button_aceptar.grid(row=7, column=6, columnspan=1, ipadx=5, ipady=5)

    def Reservar(self):
        i = 0
        peli = self.input_reservar.get()
        if len(peli) > 0:
            peliculas = self.pelicula.mostrar_nombres(self.bdd)
            self.input_reservar.delete(0, 'end')
            self.ventana_padre.withdraw()
            while peliculas[i][0] != int(peli):
                i += 1
            ventana = FormularioReserva(self.ventana_padre, self.cuenta_usuario.dni, peliculas[i][1], self.bdd)
            ventana.mainloop()
        else:
            messagebox.showerror('Error', 'Debe seleccionar una pelicula!')
    
    def Detalles(self):
        peli = self.input_info.get()
        if len(peli) > 0:
            self.input_info.set('')
            ventana = MasDetalles(self.ventana_padre, peli, self.bdd)
            ventana.mainloop()
        else:
            messagebox.showerror('Error', 'Debe seleccionar una pelicula!')



class PeliculaAdministrador(tk.Frame):
    def __init__(self, ventana_padre = None, master = None, base_datos = None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.ventana_padre = ventana_padre
        self.bdd = base_datos
        self.pelicula = Pelicula()

        """WIDGETS"""
        #Titulo
        self.cabecera = ttk.Label(self)
        #Tabla
        self.tabla = ttk.Treeview(self)
        #Detalles
        self.label_info = ttk.Label(self)
        self.input_info =  ttk.Combobox(self)
        self.button_info = ttk.Button(self)
        #Añadir
        self.Add_label = ttk.Label(self)
        self.Add_bott = ttk.Button(self)
        #Eliminar
        self.Elim_label = ttk.Label(self)
        self.Elim_input = ttk.Combobox(self)
        self.Elim_bott = ttk.Button(self)

        self.widgets_config()
        self.widgets_grid()
        self.input_fill()


    
    def tabla_config(self):
        self.tabla.config(columns = (1, 2, 3, 4))
        self.tabla.column('#0', width=70, anchor = 'center')
        self.tabla.heading('#0', text='ID Pelicula', anchor = 'center')
        self.tabla.column('#1', width=180, anchor = 'center')
        self.tabla.heading('#1', text='Nombre', anchor = 'center')
        self.tabla.column('#2', width=70, anchor = 'center')
        self.tabla.heading('#2', text='Duracion', anchor = 'center')
        self.tabla.column('#3', width=100, anchor = 'center')
        self.tabla.heading('#3', text='Genero', anchor = 'center')
        self.tabla.column('#4', width=70, anchor = 'center')
        self.tabla.heading('#4', text='Tipo', anchor = 'center')

    def widgets_config(self):
        #Titulo
        self.cabecera.config(text = 'Peliculas Disponibles', foreground = '#FFFFFF', font = ('Segoe UI Black', 36), background = '#002B40', justify = 'center')
        #Tabla
        self.tabla_config()
        #Detalles
        self.label_info.config(text = 'Selecciona una pelicula\npara ver más detalles', foreground = '#FFFFFF', font = ('Segoe UI Black', 18), background = '#056595', justify = 'center')
        self.input_info.config(width = 5, state = 'readonly')
        self.button_info.config(text = 'Ver Más', command = self.Detalles)
        #Añadir
        self.Add_label.config(text = 'Agregar pelicula', foreground = '#FFFFFF', font = ('Segoe UI Black', 18), background = '#056595')
        self.Add_bott.config(text = 'Agregar', command = self.Agregar)
        #Eliminar
        self.Elim_label.config(text = 'Eliminar pelicula', foreground = '#FFFFFF', font = ('Segoe UI Black', 18), background = '#056595')
        self.Elim_input.config(width = 5, state = 'readonly')
        self.Elim_bott.config(text = 'Eliminar', command = self.Eliminar)


    def input_fill(self):
        self.tabla.delete(*self.tabla.get_children())
        peliculas = self.pelicula.mostrar_peliculas(self.bdd)
        ids = []
        
        for peli in peliculas:
            self.tabla.insert('', 'end', text = f'{peli[0]}', values = (peli[1], peli[2], peli[3], peli[4]))
            ids.append(peli[0])
        
        self.input_info.config(values = ids)
        self.Elim_input.config(values = ids)

    def widgets_grid(self):
        #Titulo
        self.cabecera.grid(row = 0, column = 0, columnspan = 8, pady = 20, ipady = 10)
        #Tabla
        self.tabla.grid(row = 1, column = 0, rowspan = 5, columnspan = 5, padx = 20, pady = (0, 20))
        #Detalles
        self.label_info.grid(row = 2, column = 5, rowspan = 2, columnspan = 3)
        self.input_info.grid(row = 4, column = 5, columnspan = 2)
        self.button_info.grid(row = 4, column = 7, columnspan = 1)
        #Añadir
        self.Add_label.grid(row = 6, column = 2)
        self.Add_bott.grid(row = 7, column = 2, columnspan = 1, pady = 10)
        #Eliminar
        self.Elim_label.grid(row = 6, column = 4, columnspan = 2)
        self.Elim_input.grid(row = 7, column = 4)
        self.Elim_bott.grid(row = 7, column = 5, columnspan = 1, pady = 10)

    def Detalles(self):
        peli = self.input_info.get()
        if len(peli) > 0:
            self.input_info.set('')
            ventana = MasDetalles(self.ventana_padre, peli, self.bdd)
            ventana.mainloop()
        else:
            messagebox.showerror('Error', 'Debe seleccionar una pelicula!')

    def Agregar(self):
        self.ventana_padre.withdraw()
        ventana = FormularioPelicula(self.ventana_padre, self.bdd)
        ventana.mainloop()

    def Eliminar(self):
        peli = self.Elim_input.get()
        if len(peli) > 0:
            self.pelicula.eliminar_pelicula(self.bdd, int(peli))
            self.input_fill()
            self.Elim_input.set('')
            messagebox.showinfo('Aviso', 'Pelicula eliminada exitosamente!')
        else:
            messagebox.showerror('Error', 'Debe seleccionar una pelicula!')