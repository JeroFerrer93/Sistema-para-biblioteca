 
class Libro:
    def __init__(self, titulo, autor, isbn, copias):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.copias = copias
        self.copias_disponibles = copias

    def prestar(self):
        if self.copias_disponibles > 0:
            self.copias_disponibles -= 1
            return True
        return False

    def devolver(self):
        if self.copias_disponibles < self.copias:
            self.copias_disponibles += 1
            return True
        return False

    def estado(self):
        return f"'{self.titulo}' por {self.autor} - ISBN: {self.isbn}, Disponibles: {self.copias_disponibles}/{self.copias}"
