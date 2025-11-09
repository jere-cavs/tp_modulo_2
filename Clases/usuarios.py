class usuarios:

    def __init__(self, nombre, telefono, direccion, altura, dni):
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.altura = altura
        self.dni = dni
        self.prestamos = []

    def actualizar_informacion(self, nombre = None, telefono = None, direccion = None, altura = None, dni = None):
        if nombre:
            self.nombre
        if telefono:
            self.telefono
        if direccion:
            self.direccion
        if altura:
            self.altura
        if dni:
            self.dni

    def registrar_prestamos(self, prestamo):
        self.prestamos.append(prestamo)
    
    def mostrar_informacion(self):
        info_usuarios = f"Datos del usuario a prestar: {self.nombre}, {self.telefono}, {self.direccion} al {self.altura}, {self.dni}"
        return info_usuarios