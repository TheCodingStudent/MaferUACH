from modules.common import Base, Module, EntryFrame, Frame

class Herramientas(Base):
    def __init__(self):
        modules = [
            Conversiones,
            Informacion
        ]
        super().__init__('images/left.png', 'Herramientas', modules)

class Conversiones(Base):
    def __init__(self):
        modules = [
            Unidades,
            Temperatura
        ]
        super().__init__('images/left.png', 'Conversiones', modules)

class Unidades(Module):
    def __init__(self):
        super().__init__('images/left.png', 'Unidades')

class Temperatura(Module):
    def __init__(self):
        super().__init__('images/left.png', 'Temperatura')

class Informacion(Base):
    def __init__(self):
        super().__init__('images/left.png', 'Informacion')