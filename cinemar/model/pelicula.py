class Pelicula():
    def __init__ (self, id=0, nombre=" ", duracion=0, sinopsis="", descripcion=""):
        self.id = id
        self.nombre = nombre
        self.duracion = duracion
        self.sinopsis = sinopsis
        self.descripcion = descripcion

    def __str__(self):
        return f"{self.id} {self.nombre} {self.duracion} {self.sinopsis} {self.descripcion}"
    
    def obtener_peliculas(self, bdd):
        lista = []
        peliculas = bdd.select_all('pelicula', 'id_pelicula, nombre, genero, duracion, direccion, reparto, sinopsis, id_tipo_pelicula, id_clasificacion')
        for peli in peliculas:
            lista.append(peli)
        return lista
    
    def obtener_pelicula(self, bdd, id):
        return bdd.select('pelicula', 'id_pelicula, nombre, genero, duracion, direccion, reparto, sinopsis, id_tipo_pelicula', f'id_pelicula = {id}')

    def obtener_nombres(self, bdd):
        lista = []
        peliculas = bdd.select_all('pelicula', 'nombre')
        for peli in peliculas:
            lista.append(peli[0])
        return lista

    def obtener_detalles(self, bdd, id):
        return bdd.select('pelicula', 'nombre, genero, duracion, direccion, reparto, sinopsis', f'id_pelicula = {id}')

    def obtener_id(self, bdd, nombre):
        id = bdd.select('pelicula', 'id_pelicula', f"nombre = '{nombre}'")
        return id[0]

    def obtener_pelicula_por_id(self, bdd, id):
        pelicula = bdd.select('pelicula', 'id_pelicula, nombre, duracion, sinopsis', f'id_pelicula = {id}')
        return pelicula
    
    def eliminar_pelicula(self,bdd,id_pelicula):
        bdd.delete('pelicula', f'id_pelicula = {id_pelicula}')
        
    def cargar_pelicula(self, bdd, nombre=" ", genero=" ", duracion=0, direccion=" ", reparto=" ", sinopsis=" "):
        bdd.insert('pelicula',
                    'nombre, duracion, sinopsis',
                    f"'{nombre}', {genero}, '{duracion}', '{direccion}', '{reparto}', '{sinopsis}'")