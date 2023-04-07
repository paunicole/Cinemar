class TipoPelicula():
    def __init__ (self, id=0, formato="", idioma="", subtitulada=""):
        self.id = id
        self.formato = formato
        self.idioma = idioma
        self.subtitulada = subtitulada

    def __str__(self):
        return f"{self.id} {self.formato} {self.idioma} {self.subtitulada}"
    
    def obtener_tipos(self, bdd):
        lista = []
        tipos = bdd.select_all('tipo_pelicula', 'id_tipo_pelicula, formato, idioma, subtitulada')
        for tipo in tipos:
            lista.append(tipo)
        return lista

    def obtener_tipo(self, bdd, id):
        tipo = bdd.select_all(f'tipo_pelicula WHERE id_tipo_pelicula = {id}', 'id_tipo_pelicula, formato, idioma, subtitulada')
        return tipo