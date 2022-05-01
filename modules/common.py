##### IMPORTAMOS LIBRERIAS Y CLASES #####
from tkinter import Frame, Label, Entry
from widgets import Photo
import json

with open('style.json', 'r') as f:
    data = json.load(f)

class Module:
    """
    La clase Module es una plantilla para los modulos, los modulos
    son las herramientas que se cargaran a cada tema.
    Recibe como argumentos la imagen y el nombre del modulo.
    """
    def __init__(self, image='images/left.png', name='Por Asignar', extended_name=None):
        self.image = image
        self.name = name
        self.extended_name = extended_name if extended_name else self.name
    
    def load(self, master, event=None, func=None):
        """
        Esta es la funcion predefinida para cargar un modulo, crea un 
        marco con el nombre del modulo
        """
        self.frame = Frame(master, bg=master['bg'])
        Photo(self.frame, 'images/left.png').place(relx=0.5, rely=0.3, anchor='center')
        Label(self.frame, text=self.name, bg=self.frame['bg'], fg='#000000', font='Robotica 36').place(relx=0.5, rely=0.5, anchor='center')
        return self.frame
    
    def header(self, master):
        frame = Frame(master, bg=master['bg'])
        Label(
            frame, 
            text=self.extended_name,
            bg=master['bg'],
            font=data['big_font'],
            fg=data['text_color']
        ).pack(side='top', fill='x', pady=10)
        return frame

class Base:
    """
    La clase Base es una plantilla para las materias y 
    temas que se quieran agregar a la aplicacion.
    Recibe como argumentos la direccion de la imagen que 
    representa a la materia/tema, el nombre y los modulos
    que se quieran almacenar.
    """
    def __init__(self, image, name, modules=[Module for _ in range(5)]):
        self.image = image
        self.name = name
        self.modules = modules

class EntryFrame(Frame):
    def __init__(self, master, entries, padx=0, pady=0):
        super().__init__(master, bg=master['bg'])
        self.entries = []
        text_config = {
            'bg': master['bg'],
            'fg': data['text_color'],
            'font': data['normal_font']
        }
        entry_config = {
            'bg': 'white',
            'fg': 'black',
            'selectbackground': data['select_background'],
            'selectforeground': data['select_foreground'],
            'relief': 'flat',
            'width': 20,
            'font': data['normal_font']
        }
        for i, (label, unit) in enumerate(entries):
            Label(self, text=label, **text_config).grid(row=i, column=0, sticky='e')
            entry = Entry(self, **entry_config)
            entry.grid(row=i, column=1, padx=padx, pady=pady)
            self.entries.append(entry)
            Label(self, text=unit, **text_config).grid(row=i, column=2, sticky='w')
    
    def get_values(self):
        values = []
        for entry in self.entries:
            if val := entry.get(): values.append(eval(val))
            else: values.append(None)
        return values
    
    def clear(self):
        for entry in self.entries:
            entry.delete(0, 'end')
    
    def insert(self, values):
        for i, value in enumerate(values):
            if not value: continue
            self.entries[i].delete(0, 'end')
            self.entries[i].insert(0, str(value))

class ButtonFrame(Frame):
    def __init__(self, master, buttons, padx=0, pady=0, width=100, height=20):
        super().__init__(master, bg=master['bg'])
        self.buttons = []
        for i, row in enumerate(buttons):
            for j, (text, command) in enumerate(row):
                if not command: command = lambda: None
                button = FlatButton(self, text, command, width, height)
                button.grid(row=i, column=j, padx=padx, pady=pady)
                self.buttons.append(button)

class FlatButton(Frame):
    def __init__(self, master, text, command, width, height):
        frame_config = {
            'width': width,
            'height': height,
            'bg': '#b39ddb'
        }
        super().__init__(master, **frame_config)
        self.command = command
        text_config = {
            'bg': self['bg'],
            'fg': data['text_color'],
            'font': data['normal_font']
        }
        self.original_color = self['bg']
        self.hover_color = data['hover_color']
        self.click_color = data['click_color']
        self.text = Label(self, text=text, **text_config)
        self.text.place(relx=0.5, rely=0.5, anchor='center')
        self.was_hovered = False

        ##### CONEXIONES #####
        self.bind('<Enter>', self.hover)            # cuando el mouse entre al boton, cambiamos el color
        self.bind('<Leave>', self.unhover)          # cuando el mouse deje el boton, cambiamos el color
        self.bind('<Button-1>', self.exec)          # cuando demos click ejecutamos el comando
        self.bind('<ButtonRelease-1>', self.normal)
        self.text.bind('<Button-1>', self.exec)     # cuando demos click en la etiqueta ejecutamos
        self.text.bind('<ButtonRelease-1>', self.normal)
    
    def normal(self, event):
        if not self.was_hovered:
            self['bg'] = self.original_color
            self.text['bg'] = self.original_color
        else: self.hover(event)
    
    def unhover(self, event):
        self.was_hovered = False
        self.normal(event)
    
    def hover(self, event):
        self['bg'] = self.hover_color
        self.text['bg'] = self.hover_color
        self.was_hovered = True
    
    def exec(self, event): 
        self['bg'] = self.click_color
        self.text['bg'] = self.click_color
        self.command()