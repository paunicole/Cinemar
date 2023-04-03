class Pelicula():
    def __init__ (self, id=0, nombre=" ", duracion=0, genero="", tipo="", director="", actores="", sinopsis=""):
        self.id = id
        self.nombre = nombre
        self.duracion = duracion
        self.genero = genero
        self.tipo = tipo
        self.director = director
        self.actores = actores
        self.sinopsis = sinopsis
        
    def __str__(self):
        return f"{self.id} {self.nombre} {self.duracion} {self.genero} {self.tipo} {self.director} {self.actores} {self.sinopsis}"
    
    def mostrar_peliculas(self, bdd):
        lista=[]
        pelicula = bdd.select_all('peliculas','id_pelicula, nombre, duracion, genero, tipo, director, actores, sinopsis')
        for i in range(len(pelicula)):
            lista.append(pelicula[i])
        return lista
    
    def mas_detalles(self, bdd, id):
        return bdd.select('peliculas', 'director, actores, sinopsis', f'id_pelicula = {id}')
    
    def ver_mas(self, bdd, id):
        return bdd.select('peliculas', 'nombre, duracion, genero, director, actores, sinopsis', f'id_pelicula = {id}')

    def obtener_id(self, bdd, nombre):
        tupla = bdd.select('peliculas', 'id_pelicula', f"nombre = '{nombre}'")
        lista = list(tupla)
        id = lista[0]
        return id

    def mostrar_nombres(self, bdd):
        lista=[]
        pelicula = bdd.select_all('peliculas WHERE id_pelicula != 0', 'id_pelicula, nombre, tipo')
        for i in range(len(pelicula)):
            lista.append(pelicula[i])
        return lista
    
    def eliminar_pelicula(self,bdd,id_pelicula):
        bdd.delete('peliculas', f'id_pelicula = {id_pelicula}')
        
    def cargar_pelicula(self,bdd,nombre=" ",duracion=0,genero=" ",tipo=" ",director=" ",actores=" ",sinopsis=" "):
        bdd.insert('peliculas',
                    'nombre,duracion,genero,tipo,director,actores,sinopsis',
                    f"'{nombre}',{duracion},'{genero}','{tipo}','{director}','{actores}','{sinopsis}'")