##### IMPORTAR LIBRERIAS #####
from widgets import *
from modules.all import all_courses

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
        self['bg'] = '#ede7f6'

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
        self.left_bar = LeftBar(self, width=50)
        self.left_bar.pack(side='left', fill='y')
        self.left_bar.load_courses(all_courses)

        self.container = Container(self, bg='#ede7f6')              # creamos el contenedor de modulos
        self.container.pack(side='top', expand=True, fill='both')   # lo colocamos y hacemos que se expanda para cubrir la ventana
        
        self.main_frame = Main(self.container)
        self.container.frames.append(self.main_frame)
        self.container.show_frame(0)

        ##### CONEXIONES #####
        self.bind('<Control-b>', self.left_bar.toggle)
    
    ##### FUNCIONES #####
    def add_pages(self, *pages):
        self.container.add_frames(*pages)

##### CREAMOS VENTANA #####
window = Window(1000, 700)

window.mainloop()