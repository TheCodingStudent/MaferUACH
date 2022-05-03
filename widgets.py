##### IMPORTAR LIBRERIAS #####
from tkinter import *
from PIL import ImageTk, Image
from bezier import Bezier
import utils

STYLE = utils.get_style()

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
        self.hide_current()                         # ocultar el marco anterior
        self.current = cont                         # actualizamos el numero del marco actual
        frame = self.frames[cont]                   # obtenemos el marco que queremos
        frame.grid(row=0, column=0, sticky='nsew')  # colocamos el marco en el contenedor
        frame.tkraise()                             # mostramos el marco
    
    def hide_current(self):                         # con esta funcion ocultamos el marco que este mostrandose
        if self.current == None: return             # si no hay marco entonces salimos de la funcion
        self.frames[self.current].grid_forget()     # si hay entonces lo quitamos de la pantalla
        self.current = None                         # y guardamos que ya no hay marco mostrandose

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

class Text(Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self['bg'] = master['bg']
        self.parragraphs = 0
    
    def add(self, lines, config={}, padx=0, pady=0, sticky='w'):
        for i, line in enumerate(lines):
            Label(
                self,
                text=line,
                **config
            ).grid(
                row=i+self.parragraphs, 
                column=0, 
                padx=padx, 
                pady=pady, 
                sticky=sticky
            )
        self.parragraphs += len(lines)

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
        self.text = Label(
            self, 
            text=text, 
            bg=self['bg'], 
            fg=utils.atenuate(STYLE['color'], 230, 30),
            font=STYLE['menu_font']
        )   # creamos el texto del boton
        self.text.place(relx=0.6, rely=0.5, anchor='center')            # lo colocamos a la mitad, cargado ligeramente a la derecha

        self.original_color = self['bg']                # guardamos el color original, ya que despues sera cambiado
        self.hover_color = utils.atenuate(STYLE['color'], 145, 120)

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
    """
    La clase Main sera la pantalla que se muestre al iniciar el 
    programa, asi puedo
    """
    def __init__(self, master):
        super().__init__(master, bg=master['bg'])

        self.creator = Label(
            self,
            text='ARMANDO CHAPARRO',
            font=('Segoe UI Black', 12),
            bg=self['bg'],
            fg=utils.atenuate(STYLE['color'], 200, 30)
        )
        self.creator.place(x=30, y=30)

        self.main = Frame(self, bg=self['bg'])

        self.logo = Photo(self.main, 'images/neologo300x240.png')
        self.logo.grid(column=0, row=0, padx=20)

        self.text = Text(self.main)
        self.text.add(
            ['MAFER'],
            {
                'font': ('Segoe UI Black', 36),
                'bg': self['bg'],
                'fg': utils.atenuate(STYLE['color'], 200, 30)
            }
        )
        self.text.add(
            [
                '"UNA PERSONA INTELIGENTE RESUELVE PROBLEMAS,',
                'UN INGENIERO INVENTA ALGO QUE RESUELVA PROBLEMAS."'
            ],
            {
                'font': ('Segoe UI', 12),
                'bg': self['bg'],
                'fg': utils.atenuate(STYLE['color'], 150, 30)
            }
        )
        self.text.grid(column=1, row=0, sticky='ne')
        self.main.place(relx=0.5, rely=0.5, anchor='center')
    
    def bind(self, event, func):
        pass

##### ELEMENTOS #####
class Bar(Frame):
    """
    La clase Bar sera una plantilla para la barra lateral, simplifica
    el codigo y lo hace mas facil de manipular.
    """
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        ##### COMPONENTES #####
        self.container = Frame(self, bg=self['bg'])                 # este sera el contenedor principal
        self.container.place(x=0, y=0, relwidth=1, relheight=1)     # hacemos que rellene todo el espacio

        self.top_frame = Frame(self.container, bg=self['bg'])       # este sera el marco superior, para logos
        self.top_frame.pack(side='top', fill='x')                   # lo colocamos arriba

        self.main_frame = Frame(self.container, bg=self['bg'])      # este sera el marco principal, para botones
        self.main_frame.pack(side='top', expand=True, fill='both')  # hacemos que ocupe todo el espacio sobrante

        self.bottom_frame = Frame(self.container, bg=self['bg'])    # y este sera el marco inferior, sin uso actual
        self.bottom_frame.pack(side='bottom', fill='x')             # lo colocamos abajo

class LeftBar(Frame):
    """
    LeftBar se encargar de contener los botones para llamar
    a los modulos de la aplicacion, tambien mostrara el logo.
    """
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        ##### PROPERTIES #####
        self.master = master                # elemento padre, podremos referenciarlo despues
        self.width = self['width']          # guardamos el ancho minimo de la barra
        self.bar_width = (200, 200, 200)    # estos son los anchos para cada elemento en la barra
        self.toggled = False                # esta propiedad nos dice si la barra esta desplegada o no
        self.on_animation = False           # esta propiedad nos permite saber si la barra se esta contrayendo/desplegando
        self.current_index = None           # este sera el menu que este activo, inicialmente ninguno esta activo

        ##### QUANTITIES #####
        self.subjects = 0
        self.modules = 0

        ##### STYLE #####
        self.time = 20      # tiempo que dura la animacion de la barra en completarse (frames)
        control_points = [  # estos son los puntos de control para crear una curva bezier y darle un efecto elegante a la barra
            (0, 0),
            (1, 0),
            (1, 1)
        ]
        self.curve = Bezier(              # creamos la curva bezier (mas informacion en utils.py)
            control_points,
            self.time,
            width=sum(self.bar_width)-self.width
        )

        ##### CONTENT #####
        self.course_frame = Bar(self, width=self.bar_width[0], bg=utils.atenuate(STYLE['color'], 50, 30))        # este sera el contenedor de los botones para las materias
        self.course_frame.place(x=0, y=0, relheight=1)                              # lo colocamos a la izquierda

        self.subject_frame = Container(self, width=self.bar_width[1], bg=utils.atenuate(STYLE['color'], 75, 30)) # este sera el contenedor para los temas de cada materia
        self.subject_frame.place(x=self.bar_width[0], y=0, relheight=1)             # lo colocamos al centro
        self.module_frame = Container(self, width=self.bar_width[2], bg=utils.atenuate(STYLE['color'], 100, 30))  # y este sera el contenedor para los modulos de cada tema
        self.module_frame.place(x=sum(self.bar_width[:2]), y=0, relheight=1)        # lo colocamos a la derecha

    def show_course(self, index):
        """
        Se encarga de cambiar el marco de la barra de temas, tambien de reiniciar
        el marco en la barra de modulos, para que los modulos y los temas concuerden.
        Tambien actualiza cual es la materia actual.
        Recibe como argumento el indice de la materia que queremos mostrar
        """
        if index == self.current_index: return  # si seleccionamos la misma materia entonces no hacemos algo
        self.current_index = index              # asignamos el indice actual con el que corresponde a la materia
        self.module_frame.hide_current()        # ocultamos los modulos para no causar confusiones
        self.subject_frame.show_frame(index)    # mostramos los temas correspondientes a la materia seleccionada
    
    def load_courses(self, courses):
        """
        Cargamos cada materia a la barra de materias, tenemos que hacerlo uno por
        uno para poder asignar indices diferentes, si lo hicieramos en esta misma
        funcion Python asignaria el mismo indice a todos los botones aunque 
        siguieramos iterando.
        Recibe como argumento una lista con las materias a cargar, estas provienen de 
        modules.all.all_courses
        """
        for i, course in enumerate(courses):    # asignamos un indice a cada materia
            self.load_course(course(), i)       # cargamos cada materia por separado, pasandole el indice correspondiente
    
    def load_course(self, course, index):
        """
        Carga cada materia, creando un boton que mostraremos en la barra de materias,
        le asignara el comando de mostrar los temas de la materia correspondiente y a
        su vez cargara los temas en la barra correspondiente.
        Recibe como argumento la materia a cargar y el indice que le corresponde.
        """
        IconButton(
            self.course_frame.main_frame,
            course.image,
            course.name,
            width=self.bar_width[0],
            height=50,
            command=lambda: self.show_course(index)
        ).grid(row=index, column=0)
        self.load_subjects(course.modules)
    
    def load(self, destiny_frame, objects, function):
        """
        Carga cada marco que corresponde a las barras laterales, es una plantilla
        para cargar los temas y los modulos, nos simplifica el codigo y si edito algo
        aqui obtendre el mismo efecto en las demas barras.
        """
        new_frame = Frame(destiny_frame, bg=destiny_frame['bg'])    # creamos el marco que añadiremos a la barra lateral
        for i, obj in enumerate(objects):                           # iteramos por cada objecto que añadiremos y le asignaremos un indice
            function(new_frame, obj(), i)                           # utilizamos la funcion que hayamos pasado como argumento
        destiny_frame.frames.append(new_frame)                      # por ultimo añadimos el marco ya con los botones creados
    
    def load_subjects(self, subjects):
        """
        Carga los temas de cada materia, utiliza la funcion load para simplificar las cosas,
        le decimos que queremos añadir los botones al marco de temas, le pasamos
        los temas y le damos la funcion 'load subject' para que esta funcion se encargue
        de crear el boton correspondiente.
        """
        self.load(self.subject_frame, subjects, self.load_subject)
        self.subjects += len(subjects)
    
    def load_modules(self, modules):
        """
        Carga los modulos de cada tema, utiliza la funcion load para simplificar las cosas,
        le decimos que queremos añadir los botones al marco de modulos, le pasamos
        los modulos y le damos la funcion 'load module' para que esta funcion se encargue
        de crear el boton correspondiente.
        """
        self.load(self.module_frame, modules, self.load_module)
    
    def create_button(self, frame, obj, width) -> IconButton:
        """
        Crea y regresa un boton con icono en el marco que le pasemos como argumento
        y obtiene los atributos del objecto que le demos.
        """
        return IconButton(
            frame,
            obj.image,
            obj.name,
            height=50,
            width=width
        )
    
    def load_subject(self, frame, subject, index):
        """
        Carga el tema que le demos como argumento, crea el boton correspondiente
        y lo agrega al marco que debe, aparte carga los modulos que le corresponden
        al tema.
        """
        offset = self.subjects
        subject_button = self.create_button(frame, subject, self.bar_width[1])  # creamos el boton
        subject_button.command = lambda: self.module_frame.show_frame(offset + index)    # le asignamos el comando
        subject_button.grid(row=index, column=0)                                # lo colocamos en la posicion que corresponde
        self.load_modules(subject.modules)                                      # cargamos los modulos del tema
        self.modules += len(subject.modules)
    
    def load_module(self, frame, module, index):
        """
        Carga el modolo que le demos como argumento, crea el boton que le corresponde
        y lo agrega al marco que debe, ademas agrega el modulo al contenedor de la
        aplicacion para que podamos usarlo posteriormente.
        """
        offset = self.modules
        module_button = self.create_button(frame, module, self.bar_width[2])    # creamos el boton
        module_button.command = lambda: self.call_module(offset + index)                 # le asignamos el comando
        module_button.grid(row=index, column=0)                                 # lo colocamos en la posicion que corresponde

        new_module = module.load(self.master.container, '<Button-1>', self.deactivate) # creamos el marco de la herramienta
        self.master.add_frame(new_module)               # lo agregamos al contenedor de la aplicacion

    def call_module(self, index):
        """
        Esta funcion se encarga de mostrar la herramienta que deseamos en el
        contenedor de la aplicacion.
        """
        self.master.container.show_frame(index)
    
    def activate(self, event):
        if self.on_animation: return
        self.on_animation = True
        rng = range(self.time + 1)
        for t in rng:
            self['width'] = self.width + self.curve.eval(t)
            self.update()
        self.on_animation = False
        self.toggled = True
    
    def deactivate(self, event):
        if self.on_animation or (not self.toggled): return
        self.on_animation = True
        rng = range(self.time + 1)
        for t in reversed(rng):
            self['width'] = self.width + self.curve.eval(t)
            self.update()
        self.on_animation = False
        self.toggled = False

    def toggle(self, event):
        """
        Se encarga de la animacion de desplegar/contraer la barra lateral,
        utiliza una curva bezier para realizar la animacion y actualiza la 
        aplicacion a cada frame. El tiempo de la animacion puede ser cambiado
        con la propiedad 'self.time'
        """
        if not self.toggled: self.activate(event)
        else: self.deactivate(event)