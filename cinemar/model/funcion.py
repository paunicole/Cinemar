class Funcion:
    def __init__ (self, id=0, sala=0, pelicula=" ", butacas_libres=0, fecha=" ", horario=" ", precio=0.0):
        self.id = id
        self.sala = sala
        self.pelicula = pelicula
        self.butacas_libres = butacas_libres
        self.fecha = fecha
        self.horario = horario
        self.precio = precio

    def __str__(self):
        f"{self.id} {self.sala} {self.pelicula} {self.butacas_libres} {self.fecha} {self.horario} {self.precio}"
        
    def crear_funcion(self, bdd, sala, pelicula, butacas_libres, fecha, horario, precio):
        bdd.insert('sesion',
                    'id_sala, id_pelicula, fecha, hora', 
                    f'{sala},"{pelicula}",{butacas_libres},"{fecha}","{horario}",{precio}')
    
    def modificar_funcion(self, bdd, id_funcion, **datos):
        """Método que ."""
        for clave, valor in datos.items():
            if clave == 'sala':
                bdd.update('funcion', 'id_sala', f'{valor}', f'id_funcion={id_funcion}')
            elif clave == 'pelicula':
                bdd.update('funcion', 'id_pelicula', f'"{valor}"', f'id_funcion={id_funcion}')
            elif clave == 'fecha':
                bdd.update('funcion', 'fecha', f'"{valor}"', f'id_funcion={id_funcion}')
            elif clave == 'horario':
                bdd.update('funcion', 'hora', f'"{valor}"', f'id_funcion={id_funcion}')
    
    def eliminar_funcion(self, bdd, id_funcion):
        bdd.delete('sesion', f'id_funcion={id_funcion}')

    def obtener_funciones_por_peli(self, bdd, id):
        """Metodo que retorna todas las funciones de la pelicula 'peli' pasada por parametro."""
        funciones = bdd.select_all(f'funcion WHERE id_pelicula={id}', 'id_funcion, fecha, hora, id_sala, id_pelicula')
        return funciones

    def obtener_pelicula(self, bdd, id):
        id_pelicula = bdd.select('funcion', 'id_pelicula', f'id_funcion="{id}"')
        return id_pelicula[0]

    def obtener_funciones(self, bdd):
        """Método que retorna una lista de tuplas con los datos de todas las funciones disponibles."""
        lista = []
        funciones = bdd.select_all('funcion', 'id_funcion, fecha, hora, id_sala, id_pelicula')
        for fun in funciones:
            lista.append(fun)
        return lista

    def devolver_sala(self, bdd, nombre, fecha, hora):
        sala = bdd.select('funcion', 'id_sala', f'fecha="{fecha}" AND horario="{hora}"')
        return sala