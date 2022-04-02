##### IMPORTAR LIBRERIAS #####
from tkinter import *
from PIL import ImageTk, Image
import utils

##### WIDGETS #####
class Container(Frame):
    """
    Container es un marco especial que ofrece capacidades
    para mostrar multiples marcos y almacenarlos, esto es
    utilizado para alamcenar las diferentes herramientas
    del programa, en Window se crea un Container y ahi se
    ponen los marcos de herramientas.
    """
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        ##### PROPIEDADES #####
        self.master = master                        # guardamos al widget padre
        self.frames = []                            # aqui estaran los marcos de la aplicacion
        self.current = None                         # este sera el numero de la pagina actual 
        self.grid_rowconfigure(0, weight = 1)       # creamos una cuadricula con una sola fila
        self.grid_columnconfigure(0, weight = 1)    # y una sola columna
    
    ##### FUNCIONES #####
    def show_frame(self, cont):                     # esta funcion mostrara el marco que se le indique
        if self.current != None:                    # si hay algun marco que previamente estaba mostrado, entonces lo quitamos
            self.frames[self.current].grid_forget()
        self.current = cont                         # actualizamos el numero del marco actual
        frame = self.frames[cont]                   # obtenemos el marco que queremos
        frame.grid(row=0, column=0, sticky='nsew')  # colocamos el marco en el contenedor
        frame.tkraise()                             # mostramos el marco

class Photo(Label):
    """
    Photo facilita el poner imagenes, en realidad es una etiqueta
    pero "tkinter" permite poner imagenes a etiquetas, asi que
    explotaremos eso.
    """
    def __init__(self, master, image, **kwargs):

        ##### PROPIEDADES #####
        self.image = ImageTk.PhotoImage(Image.open(image))          # creamos una imagen con el formato que soporta "tkinter"
        kwargs['image'] = self.image                                # damos como argumento la imagen que hicimos previamente
        super().__init__(master, image=self.image, bg=master['bg']) # creamos una etiqueta con la imagen y obtenemos sus propiedades

class IconButton(Frame):
    """
    LeftBarButton es un tipo de boton especial para ser 
    colocado en la barra lateral, tiene propiedades como
    cambiar de color cuando se esta encima de el, asi dara
    la sensacion de estar siendo pisado. Al ser presionado
    mandara llamar la funcion que le hayamos dado.
    """
    def __init__(self, master, image, text, command=lambda: None, **kwargs):
        super().__init__(master, bg=master['bg'], **kwargs)

        ##### PROPIEDADES #####
        if image:
            self.image = Photo(self, image)                             # creamos la imagen del boton
            self.image.place(x=0, y=0)                                  # colocamos la imagen al lado izquierdo
        self.text = Label(self, text=text, bg=self['bg'], fg='white')   # creamos el texto del boton
        self.text.place(relx=0.6, rely=0.5, anchor='center')            # lo colocamos a la mitad, cargado ligeramente a la derecha

        r, g, b = utils.hex_to_rgb(self['bg'])          # obtenemos los colores del boton
        light = 0.9                                     # damos valor a la luminosidad del boton cuando el cursor se pose
        nr, ng, nb = r * light, g * light, b * light    # obtenemos los colores con la luminosidad deseada
        self.original_color = self['bg']                # guardamos el color original, ya que despues sera cambiado
        self.hover_color = utils.rgb2hex(nr, ng, nb)    # guardamos el nuevo color con diferente luminosidad

        self.command = command  # guardamos el comando a ejecutar

        ##### CONEXIONES #####
        self.bind('<Enter>', self.hover)            # cuando el mouse entre al boton, cambiamos el color
        self.bind('<Leave>', self.unhover)          # cuando el mouse deje el boton, cambiamos el color
        self.bind('<Button-1>', self.exec)          # cuando demos click ejecutamos el comando
        self.text.bind('<Button-1>', self.exec)     # cuando demos click en la etiqueta ejecutamos
        self.image.bind('<Button-1>', self.exec)    # cuando demos click en la imagen ejecutamos

    ##### FUNCIONES #####
    def exec(self, event):      # esta funcion ejecuta el comando, pero absorbe un evento que "tkinter" crea
        self.command()
    
    def hover(self, event):     # esta funcion cambia el color del boton cuando el mouse esta encima
        self['bg'] = self.hover_color
        self.image['bg'] = self.hover_color
        self.text['bg'] = self.hover_color
    
    def unhover(self, event):   # esta funcion cambia el color del boton cuando el mouse deja de estar encima
        self['bg'] = self.original_color
        self.image['bg'] = self.original_color
        self.text['bg'] = self.original_color

class Main(Frame):
    def __init__(self, master):
        super().__init__(master, bg=master['bg'], width=100, height=100)

        self.container = Frame(self, bg=self['bg'])
        self.container.place(relx=0.5, rely=0.5, anchor='center', relwidth=1, relheight=1)

        self.logos = Frame(self.container, bg=self['bg'])
        self.logos.place(relx=0.5, rely=0.33, anchor='center', relwidth=1, height=300)
        self.logo_mafer = Photo(self.logos, 'images/logo.png')
        self.logo_mafer.place(relx=0.25, rely=0.5, anchor='center')
        self.logo_uach = Photo(self.logos, 'images/uach.png')
        self.logo_uach.place(relx=0.75, rely=0.5, anchor='center')

        self.text = Frame(self.container)
        self.text.place(relx=0.5, rely=0.66, anchor='center')
        self.message = [
            "MAFER es una herramienta para la facultad de ingeniería",
            "para el desarrollo académico y reforzamiento de aprendizaje.",
            "Mejora tu conocimiento y resuelve tareas de manera",
            "sencilla con MAFER."
        ]
        config = {
            'bg': self['bg'],
            'fg': "#673ab7",
            'font': 'Arial 12 bold'
        }
        for message in self.message:
            Label(self.text, text=message, **config).pack(side='top', fill='x')
        
        Label(self.container, text='Ing.Armando Chaparro', **config).place(relx=1, rely=1, anchor='se')

##### ELEMENTOS #####
class Bar(Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.container = Frame(self, bg=self['bg'])
        self.container.place(x=0, y=0, relwidth=1, relheight=1)

        self.top_frame = Frame(self.container, bg=self['bg'])
        self.top_frame.pack(side='top', fill='x')

        self.main_frame = Frame(self.container, bg=self['bg'])
        self.main_frame.pack(side='top', expand=True, fill='both')

class LeftBar(Frame):
    """
    LeftBar se encargar de contener los botones para llamar
    a los modulos de la aplicacion, tambien mostrara el logo.
    """
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        ##### PROPERTIES #####
        self.width = self['width']
        self.bar_width = (175, 175, 175)
        self.toggled = False
        self.on_animation = False

        ##### STYLE #####
        self.time = 1
        control_points = [
            (0, 0),
            (1, 0),
            (2, 0),
            (1, 1)
        ]
        self.curve = utils.Bezier(
            control_points,
            self.time,
            width=sum(self.bar_width)-self.width
        )

        ##### CONTENT #####
        self.course_frame = Bar(self, width=self.bar_width[0], bg='#673ab7')
        self.course_frame.place(x=0, y=0, relheight=1)

        self.subject_frame = Container(self, width=self.bar_width[1], bg='#9575cd')
        self.subject_frame.place(x=self.bar_width[0], y=0, relheight=1)
        self.module_frame = Container(self, width=self.bar_width[2], bg='#b39ddb')
        self.module_frame.place(x=sum(self.bar_width[:2]), y=0, relheight=1)
    
    def load_courses(self, courses):
        for i, course in enumerate(courses):
            self.load_course(course(), i)
    
    def load_course(self, course, index):
        IconButton(
            self.course_frame.main_frame,
            course.image,
            course.name,
            width=self.bar_width[0],
            height=50,
            command=lambda: self.subject_frame.show_frame(index)
        ).grid(row=index, column=0)
    
    def toggle(self, event):
        if self.on_animation: return
        self.on_animation = True
        rng = range(self.time+1)
        if self.toggled: rng = reversed(rng)
        for t in rng:
            self['width'] = self.width + self.curve.eval(t)
            self.update()
        self.toggled = not self.toggled
        self.on_animation = False