class Butaca:
    def __init__ (self, id=0, fila="", numero=0, reservada="", id_sala=None):
        self.id = id
        self.fila = fila
        self.numero = numero
        self.reservada = reservada
        self.id_sala = id_sala

    def __str__(self):
        f"{self.id} {self.fila} {self.numero} {self.reservada} {self.id_sala}"
    
    def devolver_butacas(self, bdd):
        lista = []
        butacas = bdd.select_all('butaca', 'id_butaca, fila, numero, reservada, id_sala')
        for i in range(len(butacas)):
            lista.append(butacas[i])
        return lista

    def devolver_butacas_por_sala(self, bdd, id_sala):
        butacas = self.devolver_butacas(bdd)
        butacas_sala = []
        for butaca in butacas:
            if butaca[4] == id_sala:
                butacas_sala.append(butaca)
        return butacas_sala