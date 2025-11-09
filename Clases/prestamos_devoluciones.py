from datetime import datetime


class prestamos_devoluciones:
    
    def __init__(self, usuario, libro):
        self.usuario = usuario
        self.libro = libro
        self.fecha_prestamo = datetime.now
        self.fecha_devolucion = None

    def registrar_devolucion(self):
        self.fecha_devolucion = datetime.now
        self.libro_disponible = True

    def mostrar_info(self):
        fecha_devolucion = (
            self.fecha_devolucion if self.fecha_devolucion else "El libro ah sido devuelto"
        )
        return f"Usuario: {self.usuario}, Nombre del libro: {self.libro}, Fecha de préstamo: {self.fecha_prestamo}, Fecha de devolución: {self.fecha_devolucion}"
