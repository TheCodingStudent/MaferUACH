from modules.common import Base

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

class Arquimides:
    def __init__(self):
        self.image = 'images/left.png'
        self.name = 'Principio de Arquimides'

class Dilatacion:
    def __init__(self):
        self.image = 'images/left.png'
        self.name = 'Dilatacion Termica'

class Cinematica(Base):
    def __init__(self):
        super().__init__('images/left.png', 'Cinematica')