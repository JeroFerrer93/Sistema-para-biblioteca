from clases.libros import Libro
from clases.usuarios import Usuario

class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []

    def registrar_libro(self, titulo, autor, isbn, copias):
        libro = Libro(titulo, autor, isbn, copias)
        self.libros.append(libro)
        print(f"Libro '{titulo}' registrado exitosamente.")

    def registrar_usuario(self, nombre, id_usuario):
        usuario = Usuario(nombre, id_usuario)
        self.usuarios.append(usuario)
        print(f"Usuario '{nombre}' registrado exitosamente.")

    def prestar_libro(self, id_usuario, isbn):
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
        libro = next((l for l in self.libros if l.isbn == isbn), None)

        if not usuario:
            print("Usuario no encontrado.")
            return
        if not libro:
            print("Libro no encontrado.")
            return
        if libro.prestar():
            usuario.tomar_prestado(libro)
            print(f"El libro '{libro.titulo}' fue prestado a {usuario.nombre}.")
        else:
            print(f"No hay copias disponibles del libro '{libro.titulo}'.")

    def devolver_libro(self, id_usuario, isbn):
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
        libro = next((l for l in self.libros if l.isbn == isbn), None)

        if not usuario:
            print("Usuario no encontrado.")
            return
        if not libro:
            print("Libro no encontrado.")
            return
        if libro.devolver():
            usuario.devolver_libro(libro)
            print(f"El libro '{libro.titulo}' fue devuelto por {usuario.nombre}.")
        else:
            print(f"Error al devolver el libro '{libro.titulo}'.")

    def consultar_estado_libro(self, isbn):
        libro = next((l for l in self.libros if l.isbn == isbn), None)
        if libro:
            print(libro.estado())
        else:
            print("Libro no encontrado.")

    def estado_usuarios(self):
        for usuario in self.usuarios:
            print(usuario.estado())
