from modules.common import Base

class Herramientas(Base):
    def __init__(self):
        modules = [
            Conversiones,
            Informacion
        ]
        super().__init__('images/left.png', 'Herramientas', modules)

class Conversiones(Base):
    def __init__(self):
        super().__init__('images/left.png', 'Conversiones')

class Informacion(Base):
    def __init__(self):
        super().__init__('images/left.png', 'Informacion')