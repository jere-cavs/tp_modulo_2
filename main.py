# Funciones para la interfáz de consola:

from Clases.libros import libros
from Clases.prestamos_devoluciones import prestamos_devoluciones
from Clases.usuarios import usuarios

def registrar_libro():
    titulo = input("Ingrese el título del libro: ")
    ano_libro = int(input("Ingrese el año de publicación del libro: "))
    autor = input("Ingrese el autor del libro: ")
    genero = input("Ingrese el género del libro: ")
    editorial = input("Ingrese la editorial en la cuál fue piblicado el libro: ")
    isbn = input("Ingrese el isbn del libro")
    libro = libros(titulo, ano_libro, autor, genero, editorial, isbn)
    return libro


def registrar_usuario():
    nombre = input("Ingrese su nombre: ").lower()
    telefono = int(input("Ingrese su número de teléfono: "))
    direccion = input("Ingrese su dirección: ")
    altura = int(input("Ingrese la altura de su vivienda: "))
    dni = int(input("Ingrese su número de DNI: "))
    usuario = usuarios(nombre, telefono, direccion, altura, dni)
    return usuario

def registrar_libros_prestados(usuarios, libros):
    nombre_usuario = input("Ingrese su nombre: ")
    usuario = next((c for c in usuarios if c.nombre == nombre_usuario), None)
    if not usuario:
        print("No se ah encontrado el usuario")
        return
    
    nombre_libro = input("Ingrese el nombre del libro a prestar: ")
    libro = next((l for l in libros if l.nombre == nombre_libro and l.disponible), None)
    if not libro:
        print("No se ah encontrado el libro o el libro no se encuentra disponible")
        return
    
    prestamo = prestamos_devoluciones(usuario, libro)
    usuario.registrar_prestamo(prestamo)
    libro.disponible = False
    print("El préstamo ah sido registrado")

def registrar_devoluciones(usuarios, libros):
    nombre_usuario = input("Ingrese su nombre: ")
    usuario = next((u for u in usuarios if u.nombre == nombre_usuario), None)
    if not usuario:
        print("El usuario ingresado no se encuentra registrado")
        return
    
    titulo_libro = input("Ingrese el nombre del libro: ")
    prestamo = next((p for p in usuario.prestamos if p.libro.titulo == titulo_libro and not p.fecha_devolucion), None)
    if not prestamo:
        print("El prestamo no ah sido encontrado")
        return
    
    prestamo.registrar_devoluciones()
    print("Devolucion regitrada con éxito")

def mostrar_menu():
    print("\n-- Menú de Biblioteca")
    print("1. Registrar Libro")
    print("2. Registrar Usuario")
    print("3. Registrar Préstamo")
    print("4. Registrar devolución")
    print("5. Mostrar Información de Libros")
    print("6. Mostrar información de Usuarios")
    print("7. Salir del programa")

def main():
    libros = []
    usuarios = []

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            libro = registrar_libro()
            if libro:
                libros.append(libro)
                print("El libro ah sido registrado con éxito")

        elif opcion == "2":
            usuario = registrar_usuario()
            if usuario:
                usuarios.append(usuario)
                print("El usuario ah sido registrado con éxito")
        
        elif opcion == "3":
            registrar_libros_prestados(usuarios, libros)
        
        elif opcion == "4":
            registrar_devoluciones(usuarios, libros)

        elif opcion == "5":
            for libro in libros:
                print(libros.mostrar_dispo_libros())
        
        elif opcion == "6":
            for usuario in usuarios:
                print(usuarios.mostrar_informacion())
                for prestamo in prestamos_devoluciones:
                    print(prestamo.mostrar_info())
        
        elif opcion == "7":
            print("Saliendo del programa, Gracias por usar el sistema")
            break
        
        else:
            print("La opción ingresada no es válida")

if __name__ == "__main__":
    main()