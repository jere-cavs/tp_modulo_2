class libros:
    
    """
    Defino la clase y el constructor donde va a estar cada atributo que voy a tomar en cuenta a registrar
    """

    def __init__(self, titulo_libro, ano_libro, autor, genero, editorial, isbn):
        self.titulo_libro = titulo_libro
        self.ano_libro = ano_libro
        self.autor = autor
        self.genero = genero
        self.editorial = editorial
        self.isbn = isbn
        self.registro_libros = []
        self.disponible = True

    """
    La única información que puede actualizarse sería el año de publicación del libro y la editorial
    en donde fue publicada, ya que esta misma puede variar según la editorial en donde fue publicada.
    De ésta manera puede haber un mismo libro de un mismo autor pero de una editorial distinta,
    y por ende de un año distinto.
    """

    def actualizar_informacion(self, titulo_libro = None, ano_libro=None, editorial=None, isbn=None):
        if titulo_libro:
            self.titulo_libro = titulo_libro
        if ano_libro:
            self.ano_libro = ano_libro
        if editorial:
            self.editorial = editorial
        if isbn:
            self.isbn = isbn

    def registrar_libro(self, libro):
        self.registro_libros.append(libro)

    """
    Una vez tenga los datos registrados procedo a mostrar la información de cada uno de los libros    
    """
    def mostrar_dispo_libros(self):
        """disponibilidad = f"Los libros disponibles son los siguientes: {self.registro_libros}" if self.disponible else "No hay libros disponibles"
        return disponibilidad"""
        return f"Libros disponble: {self.registro_libros}"
    