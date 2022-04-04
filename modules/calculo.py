from modules.common import Base

class Calculo(Base):
    def __init__(self):
        modules = [
            Diferencial,
            Integral,
            Vectorial
        ]
        super().__init__('images/left.png', 'Calculo', modules)

class Diferencial(Base):
    def __init__(self):
        super().__init__('images/left.png', 'Diferencial')

class Integral(Base):
    def __init__(self):
        super().__init__('images/left.png', 'Integral')

class Vectorial(Base):
    def __init__(self):
        super().__init__('images/left.png', 'Vectorial')