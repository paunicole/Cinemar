import tkinter as tk
from tkinter import ttk
from model.ticket import Ticket

class ReservaHistoricoCliente(tk.Frame):
    def __init__(self, master=None, cuenta_usuario=None, base_datos=None):
        tk.Frame.__init__(self, master)
        self.master = master

        self.cuenta_usuario = cuenta_usuario
        self.bdd = base_datos
        self.ticket = Ticket()

        """WIDGETS"""
        #Titulo
        self.cabecera = ttk.Label(self)
        #Tabla
        self.tabla = ttk.Treeview(self)
        #Busqueda
        self.busqueda_label = ttk.Label(self)
        self.busqueda_input = ttk.Entry(self)
        self.button_buscar = ttk.Button(self)

        self.widgets_config()
        self.widgets_grid()
        self.filtrar_tickets()
    

    def widgets_config(self):
        self.cabecera.config(text='Historial de Reservas', foreground='#FFFFFF', font=('Segoe UI Black', 36), background='red', justify='center')
        
        self.tabla_config()
        
        self.busqueda_label.config(text='Buscar reserva por nombre de pelicula', foreground='#FFFFFF', font=('Segoe UI Black', 18), background='black')
        self.busqueda_input.config(width=40)
        self.button_buscar.config(text='Buscar', command=self.buscar_peli)

    def widgets_grid(self):
        self.cabecera.grid(row=0, column=0, columnspan=4, pady=20, ipady=10)

        self.tabla.grid(row=1, column=0, rowspan=4, columnspan=4, padx=20, pady=(0, 20))
 
        self.busqueda_label.grid(row=5, column=0, columnspan=4)
        self.busqueda_input.grid(row=6, column=0, columnspan=4, pady=20)
        self.button_buscar.grid(row=7, column=0, columnspan=4, ipadx=5, ipady=5)

    def tabla_config(self):
        self.tabla.config(columns=(1,2,3,4,5))

        self.tabla.column('#0', width=70, anchor='center')
        self.tabla.column('#1', width=180, anchor='center')
        self.tabla.column('#2', width=160, anchor='center')
        self.tabla.column('#3', width=90, anchor='center')
        self.tabla.column('#4', width=70, anchor='center')
        self.tabla.column('#5', width=70, anchor='center')

        self.tabla.heading('#0', text='ID', anchor='center')
        self.tabla.heading('#1', text='Pelicula', anchor='center')
        self.tabla.heading('#2', text='Butacas Reservadas', anchor='center')
        self.tabla.heading('#3', text='Fecha', anchor='center')
        self.tabla.heading('#4', text='Horario', anchor='center')
        self.tabla.heading('#5', text='Precio', anchor='center')

    def buscar_peli(self):
        peli = self.busqueda_input.get()
        if len(peli) == 0:
            self.filtrar_tickets()
        else:
            self.filtrar_tickets(peli)

    def filtrar_tickets(self, peli=None):
        self.tabla.delete(*self.tabla.get_children())
        reservas = self.ticket.tickets_comprador(self.bdd, self.cuenta_usuario.dni)
        if peli == None:
            for res in reservas:
                self.tabla.insert('', 'end', text=f'{res[0]}', values=(res[2], res[3], res[4], res[5], res[6]))
        else:
            for res in reservas:
                if res[2] == peli:
                    self.tabla.insert('', 'end', text=f'{res[0]}', values=(res[2], res[3], res[4], res[5], res[6]))



class ReservaHistoricoAdministrador(tk.Frame):
    def __init__(self, master = None, base_datos = None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.bdd = base_datos
        self.ticket = Ticket()

        """WIDGETS"""
        self.cabecera = ttk.Label(self)
        self.tabla = ttk.Treeview(self)
        self.busqueda_label = ttk.Label(self)
        self.busqueda_input = ttk.Entry(self)
        self.button_buscar = ttk.Button(self)
        
        self.widgets_config()
        self.widgets_grid()
        self.filtrar_tickets()


    def tabla_config(self):
        self.tabla.config(columns=(1,2,3,4,5,6))
        self.tabla.column('#0', width=70, anchor='center')
        self.tabla.column('#1', width=120, anchor='center')
        self.tabla.column('#2', width=180, anchor='center')
        self.tabla.column('#3', width=160, anchor='center')
        self.tabla.column('#4', width=90, anchor='center')
        self.tabla.column('#5', width=70, anchor='center')
        self.tabla.column('#6', width=70, anchor='center')

        self.tabla.heading('#0', text='ID Ticket', anchor='center')
        self.tabla.heading('#1', text='Comprador', anchor='center')
        self.tabla.heading('#2', text='Pelicula', anchor='center')
        self.tabla.heading('#3', text='Butacas Reservadas', anchor='center')
        self.tabla.heading('#4', text='Fecha', anchor='center')
        self.tabla.heading('#5', text='Horario', anchor='center')
        self.tabla.heading('#6', text='Precio', anchor='center')

    def widgets_config(self):
        self.cabecera.config(text='Historial Reservas', foreground='#FFFFFF', font=('Segoe UI Black', 36), background='#002B40')
        
        self.tabla_config()
        
        self.busqueda_label.config(text='Buscar reserva por DNI', foreground='#FFFFFF', font=('Segoe UI Black', 18), background='#056595')
        self.busqueda_input.config(width=15)
        self.button_buscar.config(text='Buscar', command=self.buscar_tickets)

    def filtrar_tickets(self):
        self.tabla.delete(*self.tabla.get_children())
        reservas = self.ticket.tickets_todos(self.bdd)

        for res in reservas:
            self.tabla.insert('', 'end', text=f'{res[0]}', values=(res[1], res[2], res[3], res[4], res[5], res[6]))
    
    def filtrar_tickets_compr(self, dni):
        self.tabla.delete(*self.tabla.get_children())
        reservas = self.ticket.tickets_comprador(self.bdd, dni)

        for res in reservas:
            self.tabla.insert('', 'end', text=f'{res[0]}', values=(res[1], res[2], res[3], res[4], res[5], res[6]))

    def widgets_grid(self):
        self.cabecera.grid(row=0, column=0, columnspan=8, pady=20, ipady=10)
        
        self.tabla.grid(row=1, column=0, rowspan=4, columnspan=8, pady=(0, 20))
        
        self.busqueda_label.grid(row=5, column=1, columnspan=4)
        self.busqueda_input.grid(row=5, column=5)
        self.button_buscar.grid(row=5, column=6)

    def buscar_tickets(self):
        dni = self.busqueda_input.get()
        if len(dni) == 0:
            self.filtrar_tickets()
        else:
            self.filtrar_tickets_compr(dni)
