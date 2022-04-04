from modules.common import Base, Module

class Fisica(Base):
    def __init__(self):
        modules = [
            Termodinamica,
            Cinematica
        ]
        super().__init__('images/left.png', 'Fisica', modules)

class Termodinamica(Base):
    def __init__(self):
        modules = [
            Arquimides,
            Dilatacion
        ]
        super().__init__('images/left.png', 'Termodinamica', modules)

class Arquimides(Module):
    def __init__(self):
        super().__init__('images/left.png', 'Arquimides')

class Dilatacion(Module):
    def __init__(self):
        super().__init__('images/left.png', 'Dilatacion')

class Cinematica(Base):
    def __init__(self):
        super().__init__('images/left.png', 'Cinematica')