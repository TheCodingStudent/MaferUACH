##### IMPORTAMOS LIBRERIAS Y CLASES #####
from tkinter import Frame, Label

from widgets import Photo

class Base:
    """
    La clase Base es una plantilla para las materias y 
    temas que se quieran agregar a la aplicacion.
    Recibe como argumentos la direccion de la imagen que 
    representa a la materia/tema, el nombre y los modulos
    que se quieran almacenar.
    """
    def __init__(self, image, name, modules=[]):
        self.image = image
        self.name = name
        self.modules = modules
        self.buttons = []

class Module:
    """
    La clase Module es una plantilla para los modulos, los modulos
    son las herramientas que se cargaran a cada tema.
    Recibe como argumentos la imagen y el nombre del modulo.
    """
    def __init__(self, image, name):
        self.image = image
        self.name = name
    
    def load(self, master):
        """
        Esta es la funcion predefinida para cargar un modulo, crea un 
        marco con el nombre del modulo
        """
        self.frame = Frame(master, bg=master['bg'])
        Photo(self.frame, 'images/left.png').place(relx=0.5, rely=0.3, anchor='center')
        Label(self.frame, text=self.name, bg=self.frame['bg'], fg='#ffffff', font='Robotica 36').place(relx=0.5, rely=0.5, anchor='center')
        return self.frame