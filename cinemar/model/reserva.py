from datetime import datetime

class Reserva():
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
        bdd.insert('reserva',
                    'id_usuario, id_funcion, id_butaca, fecha_reserva, precio', 
                    f'"{self.dni_comprador}", "{self.pelicula}", {self.cant_butacas}, "{self.fecha}", "{self.horario}", {self.precio}')
    
    def tickets_todos(self, bdd):
        lista = []
        tickets =  bdd.select_all('reserva', 'id_reserva, fecha_reserva, precio, id_usuario, id_funcion, id_butaca')
        for i in range(len(tickets)):
            lista.append(tickets[i]) 
        return lista
    
    def obtener_reservas(self, bdd, id):
        """Método que retorna una lista de reservas del usuario 'id' pasado por parámetro."""
        lista = []
        reservas = bdd.select_all(f'reserva WHERE id_usuario="{id}"', 'id_reserva, fecha_reserva, precio, id_funcion, id_butaca, id_usuario')
        for res in reservas:
            lista.append(res)
        return lista
    
    def obtener_reservas_vigentes(self, bdd, id):
        """Método que retorna una lista de reservas vigentes hasta la fecha actual
        del usuario 'id' pasado por parámetro."""
        lista = []
        reservas = bdd.select_all(f'reserva WHERE id_usuario="{id}"', 'id_reserva, fecha_reserva, precio, id_funcion, id_butaca, id_usuario')
        fecha_actual = datetime.now()
        fecha_actual = fecha_actual.strftime('%Y-%d-%m')
        for res in reservas:
            fecha_reserva = res[1]
            if  fecha_reserva > fecha_actual:
                lista.append(res)
        return lista

    def eliminar_ticket(self, bdd, id):
        bdd.delete('reserva', f'id_reserva={id}')

    def __str__(self):
        ticket = f'ID Ticket: {self.id}\nComprador: {self.dni_comprador}\nCantidad de Butacas: {self.cant_butacas}'
        ticket += f'Fecha: {self.fecha}\nHorario: {self.horario}\nPrecio: ${self.precio}'
        return ticket