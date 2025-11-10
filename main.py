# Funciones para la interfáz de consola:

from Clases.libros import libros
from Clases.prestamos_devoluciones import prestamos_devoluciones
from Clases.usuarios import usuarios

def registrar_libro():
    titulo_libro = input("Ingrese el título del libro: ")
    ano_libro = int(input("Ingrese el año de publicación del libro: "))
    autor = input("Ingrese el autor del libro: ")
    genero = input("Ingrese el género del libro: ")
    editorial = input("Ingrese la editorial en la cuál fue piblicado el libro: ")
    isbn = input("Ingrese el isbn del libro")
    libro = libros(titulo_libro, ano_libro, autor, genero, editorial, isbn)
    return libro


def registrar_usuario():
    nombre = input("Ingrese su nombre: ").lower()
    telefono = int(input("Ingrese su número de teléfono: "))
    direccion = input("Ingrese su dirección: ")
    altura = int(input("Ingrese la altura de su vivienda: "))
    dni = int(input("Ingrese su número de DNI: "))
    usuario = usuarios(nombre, telefono, direccion, altura, dni)
    return usuario

def registrar_libros_prestados(usuario, libro):
    nombre_usuario = input("Ingrese su nombre: ")
    usuario = next((c for c in usuario if c.nombre == nombre_usuario), None)
    if not usuario:
        print("No se ah encontrado el usuario")
        return
    
    nombre_libro = input("Ingrese el nombre del libro a prestar: ")
    bucle_libro = next((l for l in libro if l.titulo_libro == nombre_libro and l.disponible), None)
    if not bucle_libro:
        print("No se ah encontrado el libro o el libro no se encuentra disponible")
        return
    
    prestamo = prestamos_devoluciones(usuario, bucle_libro)
    usuario.registrar_prestamo(prestamo)
    bucle_libro.disponible = False
    print("El préstamo ah sido registrado")

def registrar_devoluciones(usuario, libro):
    nombre_usuario = input("Ingrese su nombre: ")
    usuario = next((u for u in usuario if u.nombre == nombre_usuario), None)
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
    lista_libros = []
    lista_usuarios = []

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            libro = registrar_libro()
            if libro:
                lista_libros.append(libro)
                print("El libro ah sido registrado con éxito")

        elif opcion == "2":
            usuario = registrar_usuario()
            if usuario:
                lista_usuarios.append(usuario)
                print("El usuario ah sido registrado con éxito")
        
        elif opcion == "3":
            registrar_libros_prestados(usuario, libro)
        
        elif opcion == "4":
            registrar_devoluciones(usuario, libro)

        elif opcion == "5":
            for libro in lista_libros:
                print(libro.mostrar_dispo_libros())
        
        elif opcion == "6":
            for usuario in lista_usuarios:
                print(usuario.mostrar_informacion())
                for prestamo in usuario.prestamos:
                    print(prestamo.mostrar_info())
        
        elif opcion == "7":
            print("Saliendo del programa, Gracias por usar el sistema")
            break
        
        else:
            print("La opción ingresada no es válida")

if __name__ == "__main__":
    main()