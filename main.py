##### IMPORTAR LIBRERIAS #####
import utils, color
from widgets import *
from modules.all import all_courses

STYLE = utils.get_style()

class Window(Tk):
    """
    Window es el widget principal de la aplicacion
    se encarga de contener todos los componentes como
    el contenedor de modulos y la barra lateral,
    tambien es la ventana que podemos arrastrar, cambiar
    de tamaño, minimizar o cerrar.
    Posee una combinacion de teclas para abrir/cerrar la
    barra lateral (con Ctrl+b)
    """
    def __init__(self, width, height, **kwargs):
        super().__init__(**kwargs)

        ##### ESTILO #####
        self['bg'] = color.atenuate(STYLE['color'], 30, 30)

        ##### PROPIEDADES #####
        self.screen_width = self.winfo_screenwidth()                        # obtenemos el ancho de la pantalla
        self.screen_height = self.winfo_screenheight()                      # tambien el alto
        self.original_width, self.original_height = width, height           # guardamos el ancho y alto original de la ventana
        self.centerx = (self.screen_width - width) // 2                     # obtenemos el centro horizontal
        self.centery = (self.screen_height - height) // 2                   # y el centro vertical
        self.geometry(f'{width}x{height}+{self.centerx}+{self.centery}')    # le damos dimensiones a la ventana
        self.title('MAFER -Facultad de ingenieria')                         # le damos nombre
        self.iconbitmap("images/uach.ico")                                  # y un icono

        ##### COMPONENTES #####
        self.bottom_bar = Frame(self, height=25, bg='#651fff')  # creamos la barra inferior, para poner informacion variada
        self.bottom_bar.pack(side='bottom', fill='x')           # la ponemos abajo y que ocupe todo el ancho
        config = {                                              # esta sera la configuracion para el texto de la barra inferior
            'bg': self.bottom_bar['bg'],                        # el fondo del texto sera el mismo que de la barra
            'fg': "#ede7f6",                                    # el color de texto sera un blanco con morado
            'font': 'Arial 8 bold'                              # fuente arial 8 negrita
        }
        self.creator = Label(self.bottom_bar, text='Ing.Armando Chaparro', **config)    # creamos la etiqueta para el creador. Debo darme credito a mi mismo 🤣
        self.creator.place(relx=1, rely=1, anchor='se')                                 # lo colocamos hasta la derecha

        self.container = Container(self, bg=self['bg'])              # creamos el contenedor de modulos
        self.container.place(x=50, y=0, relwidth=1, relheight=1)

        self.left_bar = LeftBar(self, width=50)     # esta sera la barra lateral, donde se escogeran las herramientas
        self.left_bar.place(x=0, y=0, relheight=1)

        self.left_bar.load_courses(all_courses)         # cargamos todos los modulos
        
        self.main_frame = Main(self.container)          # cargamos la ventana de presentacion, ahi vendran creditos, logos, mensajes, etc...
        self.main_frame.bind('<Button-1>', self.left_bar.deactivate)
        self.container.frames.append(self.main_frame)   # lo agregamos al contenedor de la aplicacion
        self.container.show_frame(-1)                   # hacemos que muestre la pagina principal (-1 por que es la ultima agregada)

        ##### CONEXIONES #####
        self.bind('<Control-b>', self.left_bar.toggle)
    
    ##### FUNCIONES #####
    def add_frame(self, frame):
        """
        Permite añadir marcos al contenedor de la aplicacion.
        """
        self.container.frames.append(frame)

##### CREAMOS VENTANA #####
window = Window(1000, 700)

window.mainloop()