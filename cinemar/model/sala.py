class Sala:
    def __init__ (self,id=0,cant_butacas=0,tipo=""):
        self.id = id
        self.cant_butacas = cant_butacas
        self.tipo = tipo
        
    def __str__(self):
        return f"{self.id} {self.cant_butacas} {self.tipo}"
    
    def modificar_sala(self,bdd,cant_butacas=0,id_sala=0):
        bdd.update('sala', 'capacidad', f'{cant_butacas}', f"id_sala='{id_sala}'")
    
    def cargar_sala(self,bdd,id,cant_butacas=0,tipo =" "):
        bdd.insert('sala','id_sala, capacidad, formato',f"{id},{cant_butacas},'{tipo}'")

    def eliminar_sala(self,bdd,id_sala):
        bdd.delete('sala', f'id_sala = {id_sala}')
        
    def mostrar_salas(self, bdd):
        lista=[]
        salas = bdd.select_all('sala','id_sala, numero, capacidad, formato')
        for i in range(len(salas)):
            lista.append(salas[i])
        return lista