import sqlite3
from sqlite3 import Error
from crear_bdd import create_connection


def create_tipo_pelicula(conn, tipo_pelicula):
    """
    Create a new project into the projects table
    :param conn: object of type sqlite3.Connection
    :param descuento:list of values
    :return: descuento id
    """
    sql = ''' INSERT INTO tipo_pelicula(formato, idioma, subtitulada)
            VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, tipo_pelicula)
    conn.commit()
    return cur.lastrowid


def create_clasificacion_pelicula(conn, clasificacion_pelicula):
    """
    Create a new task
    :param conn: Connection to the SQLite database
    :param localidad: list of values
    :return:
    """
    sql = ''' INSERT INTO clasificacion_pelicula(identificador, recomendacion, descripcion)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, clasificacion_pelicula)
    conn.commit()
    return cur.lastrowid


def create_pelicula(conn, pelicula):
    """
    Create a new task
    :param conn: Connection to the SQLite database
    :param tipo: list of values
    :return:
    """
    sql = ''' INSERT INTO pelicula(nombre, genero, duracion, direccion, reparto, sinopsis, id_tipo_pelicula, id_clasificacion)
              VALUES(?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, pelicula)
    conn.commit()
    return cur.lastrowid


def create_descuento(conn, descuento):
    """
    Create a new task
    :param conn: Connection to the SQLite database
    :param domicilio: list of values
    :return:
    """
    sql = ''' INSERT INTO descuento(dia, porcentaje)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, descuento)
    conn.commit()
    return cur.lastrowid


def create_usuario(conn, usuario):
    """
    Create a new task
    :param conn: Connection to the SQLite database
    :param usuario: list of values
    :return:
    """
    sql = ''' INSERT INTO usuario(nombre, apellido, email, dni, fecha_nacimiento, username, password, tipo)
              VALUES(?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, usuario)
    conn.commit()
    return cur.lastrowid


def create_tarjeta_credito(conn, tarjeta_credito):
    """
    Create a new task
    :param conn: Connection to the SQLite database
    :param tarjeta_credito: list of values
    :return:
    """
    sql = ''' INSERT INTO tarjeta_credito(numero, banco, titular, fecha_caducidad, codigo_seguridad, id_usuario)
              VALUES(?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, tarjeta_credito)
    conn.commit()
    return cur.lastrowid


def create_sala(conn, sala):
    """
    Create a new task
    :param conn: Connection to the SQLite database
    :param comprobante: list of values
    :return:
    """
    sql = ''' INSERT INTO sala(numero, formato, capacidad)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, sala)
    conn.commit()
    return cur.lastrowid


def create_butaca(conn, butaca):
    """
    Create a new task
    :param conn: Connection to the SQLite database
    :param detalle_comprobante: list of values
    :return:
    """
    sql = ''' INSERT INTO butaca(fila, numero, reservada, id_sala)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, butaca)
    conn.commit()
    return cur.lastrowid


def create_funcion(conn, funcion):
    """
    Create a new task
    :param conn: Connection to the SQLite database
    :param detalle_comprobante: list of values
    :return:
    """
    sql = ''' INSERT INTO funcion(fecha, hora, id_sala, id_pelicula)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, funcion)
    conn.commit()
    return cur.lastrowid


def create_reserva(conn, reserva):
    """
    Create a new task
    :param conn: Connection to the SQLite database
    :param detalle_comprobante: list of values
    :return:
    """
    sql = ''' INSERT INTO reserva(fecha_reserva, precio, id_funcion, id_butaca, id_usuario, id_tarjeta, id_descuento)
              VALUES(?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, reserva)
    conn.commit()
    return cur.lastrowid


def insert_data(database):

    # formato, idioma, subtitulada
    tipo_peliculas = [
        ['2D', "Español", "No"],
        ['2D', "Ingles", "Si"],
        ["2D", "Ingles", "No"],
        ['3D', "Español", "No"],
        ["3D", "Ingles", "No"],
        ["3D", "Ingles", "Si"],
        ["4D", "Español", "No"],
        ["4D", "Ingles", "No"],
        ["4D", "Ingles", "Si"]
    ]

    # identificador, recomendacion, descripcion
    clasificacion_peliculas = [
        ["A", "+18", "Violencia extrema"],
        ["B", "+16", "Violencia moderada"],
        ["C", "+13", "Violencia leve"],
        ["D", "+7", "Sin violencia"]
    ]

    # nombre, direccion, reparto, genero, duracion, sinopsis, id_tipo_pelicula, id_clasificacion
    peliculas = [
        ["Barbie", "Comedia, Fantástico", 180, "Greta Gerwig", "Margot Robbie, Ryan Gosling", "Una muñeca que vive en 'Barbieland' es expulsada al mundo real por no ser lo suficientemente perfecta. Basada en la popular muñeca Barbie.", 1, 1],
        ["La Sirenita", "Aventura, Drama, Familia, Fantasía", 180, "Rob Marshall", "Halle Bailey, Melissa McCarthy, Awkwafina", "Ariel es una joven y soñadora sirena, hija del Rey Tritón, que está cansada de su vida como princesa bajo el mar. Su mayor deseo es abandonar el fondo marino y tener una vida normal y apacible en la superficie. La bruja Úrsula descubre su anhelo y, por eso, a cambio de su preciosa voz le ofrece un cuerpo totalmente humano. Ariel acepta, movida por su pasión por conocer el mundo terrestre y porque está enamorada de un apuesto príncipe humano. Pero las cosas no serán fáciles para Ariel, ya que la bruja Úrsula esconde oscuras intenciones.", 2, 2],
        ["La Ballena", "Drama", 117, "Darren Aronofsky", "Brendan Fraser, Hong Chau, Sadie Sink", "Un solitario profesor de inglés con obesidad severa (Brendan Fraser) intenta reconectar con su hija adolescente en una última oportunidad de redención.", 3, 1],
        ["La Extorsión",  "Suspenso", 105, "Martino Zaidelis", "Andrea Frigerio, Carlos Portaluppi, Guillermo Francella, Pablo Rago", "Alejandro es un experimentado piloto aeronáutico. Amante de su profesión, esconde un secreto: una condición médica que implicaría su retiro inmediato. Los Servicios de Inteligencia lo descubren y muy pronto lo extorsionarán exigiéndole que transporte unas misteriosas valijas en la ruta Buenos Aires–Madrid sin hacer preguntas. Alerta por el enigmático cargamento que lleva, Alejandro se sumergirá en un universo de intriga y corrupción que lo pondrá en peligro a él y a los que ama mientras intenta escapar con vida a cualquier precio.", 4, 2],
        ["Scream 6", "Terror", 180, "Matt Bettinelli Olpin, Tyler Gillett", "Courteney Cox, Jenna Ortega, Melissa Barrera", 'Tras los últimos asesinatos de Ghostface, los cuatro sobrevivientes dejan atrás Woodsboro y comienzan un nuevo capítulo. En Scream 6, Melissa Barrera ("Sam Carpenter"), Jasmin Savoy Brown ("Mindy Meeks-Martin"), Mason Gooding ("Chad Meeks-Martin"), Jenna Ortega ("Tara Carpenter"), Hayden Panettiere ("Kirby Reed”) y Courteney Cox (“Gale Weathers”) regresan a sus roles en la franquicia junto a Jack Champion, Henry Czerny, Liana Liberato, Dermot Mulroney, Devyn Nekoda, Tony Revolori, Josh Segarra y Samara Weaving.', 5, 3],
        ["13 exorcismos", "Terror", 100, "Jacobo Martínez", "María Romanillos, Ruth Díaz, Urko Olazabal", "Tras una sesión de espiritismo realizada la víspera de Todos Los Santos, la joven Laura Villegas comienza a comportarse de manera extraña. Alarmados por el extraño comportamiento de su hija y convencidos de que el demonio la ha poseído, sus padres acuden al Padre Olmedo, uno de los 15 exorcistas autorizados en España por el Vaticano para intervenir en casos de posesiones demoníacas. A partir de ahí una serie de fenómenos extraños comenzarán a envolver a los protagonistas de la historia.", 6, 1],
        ["Asfixiado", "Comedia Dramatica", 97, "Luciano Podcaminsky", "Julieta Diaz, Leonardo Sbaraglia", "Nacho y Lucía son matrimonio que decide festejar los veinte años de casados, pero también buscan recuperar el deseo que la rutina se llevó. Inician la aventura con un grupo de amigos pero, en un giro, quedan solos y a la deriva en el mar.", 1, 2],
        ["Batman Inicia", "Acción", 140, "Christopher Nolan", "Christian Bale, Ken Watanabe, Liam Neeson", "Tras entrenar con su mentor, Batman comienza su lucha para liberar a Gotham City de la corrupción.", 2, 3],
    ]

    # dia, porcentaje
    descuentos = [
        ["Lunes", 0.2],
        ["Martes", 0.15],
        ["Miercoles", 0.2],
        ["Jueves", 0.15],
        ["Viernes", 0.1],
        ["Sabado", 0.1],
        ["Domingo", 0.1]
    ]

    #
    usuarios = [
        ['Mia', 'Gata', 'mia@gmail.com',
         '11111111', '2020-01-01',  'mia', 'mia123', 'admin'],
        ['Lali', 'Esposito', 'lali@gmail.com',
         '22222222', '2000-01-01',  'lali_star', 'lali123', 'cliente'],
        ['Lionel', 'Messi', 'lio_messi@gmail.com',
         '33333333', '1998-01-01', 'lio_messi', 'lio123', 'cliente'],
        ['Julian', 'Alvarez', 'juli_alvarez@gmail.com',
         '44444444', '2002-01-01', 'la_araña', 'juli123', 'cliente'],
        ["Moria", "Casan", "moria_laone@gmail.com",
         "55555555", '2002-01-01',  'moria_la_one', 'moria123', 'cliente'],
        ["Emiliano", "Martinez", "dibu@gmail.com",
         "66666666", '2002-01-01', 'dibu_martinez', 'dibu1234', 'cliente'],
        ["Martina", "Stoessel", "tini@gmail.com",
         "66666666", '2002-01-01', 'triple_t', 'tinitinitini', 'cliente'],
    ]

    # 
    tarjetas_credito = [
        ['123456789', 'Banco 1', 'lali_star', '2020-01-01', '123', 2],
        ['987654321', 'Banco 2', 'lio_messi', '2020-01-01', '123', 3],
        ['111222333', 'Banco 3', 'la_araña', '2020-01-01', '123', 4],
        ['444555666', 'Banco 4', 'moria_la_one', '2020-01-01', '123', 5],
        ['777888999', 'Banco 5', 'dibu_martinez', '2020-01-01', '123', 6],
        ['000111222', 'Banco 6', 'triple_t', '2020-01-01', '123', 7],
    ]

    # numero, formato, capacidad
    salas = [
        ["1", "2D", 10],
        ["2", "3D", 10],
        ["3", "2D", 10],
        ["4", "3D", 10],
        ["5", "2D", 10],
        ["6", "4D", 10],
        ["7", "4D", 10],
    ]

    # fila, numero, reservada, id_sala
    butacas = [
        # sala 1
        ["A", 1, "No", 1],
        ["A", 2, "No", 1],
        ["A", 3, "No", 1],
        ["A", 4, "No", 1],
        ["A", 5, "No", 1],
        ["B", 1, "No", 1],
        ["B", 2, "No", 1],
        ["B", 3, "No", 1],
        ["B", 4, "No", 1],
        ["B", 5, "No", 1],
        # sala 2
        ["A", 1, "No", 2],
        ["A", 2, "No", 2],
        ["A", 3, "No", 2],
        ["A", 4, "No", 2],
        ["A", 5, "No", 2],
        ["B", 1, "No", 2],
        ["B", 2, "No", 2],
        ["B", 3, "No", 2],
        ["B", 4, "No", 2],
        ["B", 5, "No", 2],
        # sala 3
        ["A", 1, "No", 3],
        ["A", 2, "No", 3],
        ["A", 3, "No", 3],
        ["A", 4, "No", 3],
        ["A", 5, "No", 3],
        ["B", 1, "No", 3],
        ["B", 2, "No", 3],
        ["B", 3, "No", 3],
        ["B", 4, "No", 3],
        ["B", 5, "No", 3],
        # sala 4
        ["A", 1, "No", 4],
        ["A", 2, "No", 4],
        ["A", 3, "No", 4],
        ["A", 4, "No", 4],
        ["A", 5, "No", 4],
        ["B", 1, "No", 4],
        ["B", 2, "No", 4],
        ["B", 3, "No", 4],
        ["B", 4, "No", 4],
        ["B", 5, "No", 4],
        # sala 5
        ["A", 1, "No", 5],
        ["A", 2, "No", 5],
        ["A", 3, "No", 5],
        ["A", 4, "No", 5],
        ["A", 5, "No", 5],
        ["B", 1, "No", 5],
        ["B", 2, "No", 5],
        ["B", 3, "No", 5],
        ["B", 4, "No", 5],
        ["B", 5, "No", 5],
    ]

    # fecha, hora, butacas_disponibles, id_sala, id_pelicula
    funciones = [
        ["2023-01-01", "12:00", 1, 1],
        ["2023-01-01", "15:00", 2, 1],
        ["2023-01-01", "18:00", 3, 1],
        ["2023-01-01", "21:00", 4, 1],
        ["2023-01-02", "12:00", 1, 2],
        ["2023-01-02", "15:00", 2, 2],
        ["2023-01-02", "18:00", 3, 2],
        ["2023-01-02", "21:00", 4, 2],
        ["2023-01-03", "12:00", 1, 3],
        ["2023-01-03", "15:00", 2, 3],
        ["2023-01-03", "18:00", 3, 3],
        ["2023-01-03", "21:00", 4, 3],
        ["2023-01-04", "12:00", 1, 4],
        ["2023-01-04", "15:00", 2, 4],
        ["2023-01-04", "18:00", 3, 4],
        ["2023-01-04", "21:00", 4, 4],
        ["2023-01-05", "12:00", 1, 5],
        ["2023-01-05", "15:00", 2, 5],
        ["2023-01-05", "18:00", 3, 5],
        ["2023-01-05", "21:00", 4, 5],
        ["2023-01-06", "12:00", 1, 6],
        ["2023-01-06", "15:00", 2, 6],
        ["2023-01-06", "18:00", 3, 6],
        ["2023-01-06", "21:00", 4, 6],
        ["2023-01-07", "12:00", 1, 7],
        ["2023-01-07", "15:00", 2, 7],
        ["2023-01-07", "18:00", 3, 7],
        ["2023-01-07", "21:00", 4, 7],
        ["2023-01-08", "12:00", 1, 8],
        ["2023-01-08", "15:00", 2, 8],
        ["2023-01-08", "18:00", 3, 8],
        ["2023-01-08", "21:00", 4, 8],
        ["2023-01-09", "12:00", 1, 9],
        ["2023-01-09", "15:00", 2, 9],
        ["2023-01-09", "18:00", 3, 9],
        ["2023-01-09", "21:00", 4, 9],
        ["2023-01-10", "12:00", 1, 10],
        ["2023-01-10", "15:00", 2, 10],
        ["2023-01-10", "18:00", 3, 10],
        ["2023-01-10", "21:00", 4, 10],
        ["2023-01-11", "12:00", 1, 11],
        ["2023-01-11", "15:00", 2, 11],
        ["2023-01-11", "18:00", 3, 11],
        ["2023-01-11", "21:00", 4, 11],
        ["2023-01-12", "12:00", 1, 12],
        ["2023-01-12", "15:00", 2, 12],
        ["2023-01-12", "18:00", 3, 12],
        ["2023-01-12", "21:00", 4, 12],
    ]
    # fecha_reserva, precio, id_funcion, id_butaca, id_usuario, id_tarjeta, id_descuento
    reservas = [
        ["2023-01-01", 500, 1, 1, 1, 1, 1],
        ["2023-12-12", 500, 1, 2, 1, 1, 1],
        ["2023-01-01", 500, 2, 1, 2, 2, 2],
        ["2023-01-01", 500, 2, 2, 2, 2, 2],
        ["2023-12-12", 500, 5, 2, 2, 2, 2],
        ["2023-01-01", 500, 3, 1, 3, 3, 3],
        ["2023-12-01", 500, 3, 2, 3, 3, 3],
        ["2023-01-01", 500, 4, 1, 4, 4, 4],
        ["2023-01-01", 500, 4, 2, 4, 4, 4],
        ["2023-01-02", 500, 5, 1, 5, 5, 5],
        ["2023-12-02", 500, 5, 2, 5, 5, 5],
        ["2023-01-02", 500, 6, 1, 6, 6, 6],
        ["2023-01-02", 500, 6, 2, 6, 6, 6],
        ["2023-01-02", 500, 7, 1, 7, 7, 7],
        ["2023-12-12", 500, 7, 2, 7, 7, 7],
    ]

    # create a database connection
    conn = create_connection(database)
    with conn:
        # create a new descuento
        for tipo_pelicula in tipo_peliculas:
            create_tipo_pelicula(conn, tipo_pelicula)

        # create a new localidad
        for clasificacion in clasificacion_peliculas:
            create_clasificacion_pelicula(conn, clasificacion)

        # create a new pelicula
        for pelicula in peliculas:
            create_pelicula(conn, pelicula)

        # create a new descuento
        for descuento in descuentos:
            create_descuento(conn, descuento)

        # create a new usuario
        for usuario in usuarios:
            create_usuario(conn, usuario)

        # create a new tarjeta_credito
        for tarjeta in tarjetas_credito:
            create_tarjeta_credito(conn, tarjeta)

        # create a new sala
        for sala in salas:
            create_sala(conn, sala)

        # create a new butaca
        for butaca in butacas:
            create_butaca(conn, butaca)

        # create a new funcion
        for funcion in funciones:
            create_funcion(conn, funcion)

        # create a new reserva
        for reserva in reservas:
            create_reserva(conn, reserva)

        print("Valores insertados")


if __name__ == '__main__':
    insert_data("cinemar.db")
    pass
