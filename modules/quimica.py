from modules.common import Base

class Quimica(Base):
    def __init__(self):
        modules = [
            Organica,
            Inorganica
        ]
        super().__init__('images/left.png', 'Quimica', modules)

class Organica(Base):
    def __init__(self):
        super().__init__('images/left.png', 'Organica')

class Inorganica(Base):
    def __init__(self):
        super().__init__('images/left.png', 'Inorganica')