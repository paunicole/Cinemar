class Persona:
    def __init__(self, apellido='', nombre='', dni='', email='', fecha_nac='', id=None):
        self.apellido = apellido
        self.nombre = nombre
        self.dni = dni
        self.email = email
        self.fecha_nac = fecha_nac
        self.id = id
    
    def apellido_setter(self, apellido):
        self.apellido = apellido.title()
    
    def nombre_setter(self, nombre = None):
        self.nombre = nombre.title()
    
    def dni_setter(self, bdd, dni):
        if bdd.count('personas', 'dni', f'dni = "{dni}"') == 1:
            return '\nDNI ya registrado!'
        else:
            self.dni = str(dni)
            return ''

    def email_setter(self, bdd, email):
        if bdd.count('personas', 'email', f'email = "{email}"') == 1:
            return '\nCorreo Electrónico ya registrado!'
        else:
            self.email = email
            return ''

    def fecha_setter(self, bdd, fecha_nac):
        if bdd.count('personas', 'telefono', f'fecha_nac = "{fecha_nac}"') == 1:
            return '\nFecha de Nacimiento ya registrado!'
        else:
            self.fecha_nac = fecha_nac
            return ''

    def modificar_persona(self, bdd, id_persona, **datos):
        for clave, valor in datos.items():
            if clave == 'apellido':
                bdd.update('personas', 'apellido', f'"{valor}"', f'id_persona={id_persona}')
            elif clave == 'nombre':
                bdd.update('personas', 'nombre', f'"{valor}"', f'id_persona={id_persona}')
            elif clave == 'dni':
                bdd.update('personas', 'dni', f'"{valor}"', f'id_persona={id_persona}')
            elif clave == 'email':
                bdd.update('personas', 'email', f'"{valor}"', f'id_persona={id_persona}')
            elif clave == 'fecha_nac':
                bdd.update('personas', 'fecha_nac', f'"{valor}"', f'id_persona={id_persona}')
    
    def crear_persona(self, bdd, apellido, nombre, dni, email, fecha_nac):
        mensaje = ''
        self.apellido_setter(apellido)
        self.nombre_setter(nombre)
        mensaje += self.dni_setter(bdd, dni)
        mensaje += self.email_setter(bdd, email)
        mensaje += self.telefono_setter(bdd, fecha_nac)
        return mensaje
    
    def cargar_persona(self, bdd):
        bdd.insert('personas',
                    'nombre, apellido, dni, email, fecha_nac', 
                    f'"{self.nombre}", "{self.apellido}", "{self.dni}", "{self.email}", {self.fecha_nac}')
    
    def eliminar_persona(self, bdd, id_persona):
        bdd.delete('personas', f'id_persona = {id_persona}')
    
    def __str__(self):
        persona = f'\nDNI: {self.dni}\tApellido y nombre: {self.apellido.upper()}, {self.nombre}'
        persona += f'\nFecha de Nacimiento: {self.fecha_nac}\tCorreo Electrónico: {self.email}'
        return persona