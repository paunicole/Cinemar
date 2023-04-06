from model.reserva import Reserva
from datetime import datetime

class Descuento:
    def __init__ (self, id=0, dia="", porcentaje=0):
        self.id = id
        self.dia = dia
        self.porcentaje = porcentaje

    def __str__(self):
        return f"{self.id} {self.dia} {self.porcentaje}"
    
    def modificar_desc(self, bdd, dia, porcentaje):
        bdd.update('descuento', 'porcentaje', f'"{porcentaje}"', f"dia='{dia}'")
    
    def obtener_descuentos(self, bdd):
        lista = []
        descuentos = bdd.select_all('descuento', 'id_descuento, dia, porcentaje')
        for des in descuentos:
            lista.append(des)
        return lista
    
    def obtener_descuento_por_dia(self, bdd, dia):
        descuentos = self.obtener_descuentos(bdd)
        i = 0
        while descuentos[i][1] != dia:
            i += 1
        return descuentos[i][2]

    def aplica_descuento(self, bdd, id, fecha):
        dias = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
        numero_dia = datetime.weekday(fecha)
        print(numero_dia)
        descuento = self.obtener_descuento_por_dia(bdd, dias[numero_dia])
        print(descuento)