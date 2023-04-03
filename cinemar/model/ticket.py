from datetime import datetime

class Ticket():
    def __init__(self, id=None, dni_comprador=0, pelicula='', cant_butacas=0, fecha='', horario='', precio=0):
        self.id = id
        self.dni_comprador = dni_comprador
        self.pelicula = pelicula
        self.cant_butacas = cant_butacas
        self.fecha = fecha
        self.horario = horario
        self.precio = precio
    
    def cargar_ticket(self, bdd):
        """Método que inserta un registro nuevo en la tabla de tickets."""
        bdd.insert('tickets',
                    'comprador, pelicula, cant_butacas, fecha, horario, precio', 
                    f'"{self.dni_comprador}", "{self.pelicula}", {self.cant_butacas}, "{self.fecha}", "{self.horario}", {self.precio}')
    
    def tickets_todos(self, bdd):
        lista = []
        tickets =  bdd.select_all('tickets', 'id_ticket, comprador, pelicula, cant_butacas, fecha, horario, precio')
        for i in range(len(tickets)):
            lista.append(tickets[i]) 
        return lista
    
    def tickets_comprador(self, bdd, dni):
        """Método que retorna una lista de tickets del comprador con el dni 'dni' pasado por parámetro."""
        lista = []
        tickets = bdd.select_all(f'tickets WHERE comprador="{dni}"', 'id_ticket, comprador, pelicula, cant_butacas, fecha, horario, precio')
        for i in range(len(tickets)):
            lista.append(tickets[i])
        return lista
    
    def tickets_comprador_vigentes(self, bdd, dni):
        """Método que retorna una lista de tickets vigentes hasta la fecha actual
        del comprador con el dni 'dni' pasado por parámetro."""
        lista = []
        tickets = bdd.select_all(f'tickets WHERE comprador="{dni}"', 'id_ticket, comprador, pelicula, cant_butacas, fecha, horario, precio')
        fecha_actual = datetime.now()
        fecha_actual = fecha_actual.strftime('%Y-%d-%m %H:%M:%S')
        for i in range(len(tickets)):
            fecha_reserva = tickets[i][4] + ' ' + tickets[i][5]
            if  fecha_reserva > fecha_actual:
                lista.append(tickets[i])
        return lista

    def eliminar_ticket(self, bdd, id):
        bdd.delete('tickets', f'id_ticket={id}')

    def __str__(self):
        ticket = f'ID Ticket: {self.id}\nComprador: {self.dni_comprador}\nCantidad de Butacas: {self.cant_butacas}'
        ticket += f'Fecha: {self.fecha}\nHorario: {self.horario}\nPrecio: ${self.precio}'
        return ticket