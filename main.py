from clases.biblioteca import Biblioteca
from clases.libros import Libro
from clases.usuarios import Usuario

def main():
    biblioteca = Biblioteca()

    # Registrar libros
    biblioteca.registrar_libro("1984", "George Orwell", "1234567890", 5)
    biblioteca.registrar_libro("Cien Años de Soledad", "Gabriel García Márquez", "0987654321", 3)

    # Registrar usuarios
    biblioteca.registrar_usuario("Juan Pérez", 1)
    biblioteca.registrar_usuario("Ana López", 2)

    while True:
        print("\n--- Menú de la Biblioteca ---")
        print("1. Tomar un libro prestado")
        print("2. Consultar estado de un libro")
        print("3. Devolver un libro")
        print("4. Registrar un nuevo libro")
        print("5. Registrar un nuevo usuario")
        print("6. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            id_usuario = int(input("Ingresa tu ID de usuario: "))
            titulo_libro = input("Escribe el título del libro que deseas tomar prestado: ")

            # Buscar el libro por título
            libro = next((l for l in biblioteca.libros if l.titulo.lower() == titulo_libro.lower()), None)
            if libro:
                biblioteca.prestar_libro(id_usuario, libro.isbn)
            else:
                print(f"El libro '{titulo_libro}' no se encuentra en la biblioteca.")
                print("Por favor, solicita al administrador que lo registre.")
        
        elif opcion == "2":
            isbn = input("Ingresa el ISBN del libro que deseas consultar: ")
            biblioteca.consultar_estado_libro(isbn)
        
        elif opcion == "3":
            id_usuario = int(input("Ingresa tu ID de usuario: "))
            isbn = input("Ingresa el ISBN del libro que deseas devolver: ")
            biblioteca.devolver_libro(id_usuario, isbn)
        
        elif opcion == "4":
            titulo = input("Título del libro: ")
            autor = input("Autor del libro: ")
            isbn = input("ISBN del libro: ")
            copias = int(input("Cantidad de copias disponibles: "))
            biblioteca.registrar_libro(titulo, autor, isbn, copias)
        
        elif opcion == "5":
            nombre = input("Nombre del usuario: ")
            id_usuario = int(input("ID del usuario: "))
            biblioteca.registrar_usuario(nombre, id_usuario)
        
        elif opcion == "6":
            print("¡Gracias por usar el sistema de la biblioteca!")
            break
        
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
