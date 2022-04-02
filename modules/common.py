from tkinter import Frame
from widgets import IconButton

class Base:
    def __init__(self, image, name, modules=[]):
        self.image = image
        self.name = name
        self.modules = modules
        self.buttons = []