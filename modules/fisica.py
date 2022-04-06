from tkinter.ttk import Combobox
from modules.common import *

class Fisica(Base):
    def __init__(self):
        modules = [Termodinamica, Cinematica]
        super().__init__('images/left.png', 'Física', modules)

class Termodinamica(Base):
    def __init__(self):
        modules = [Arquimedes, Dilatacion]
        super().__init__('images/left.png', 'Termodinámica', modules)

class Arquimedes(Module):
    def __init__(self):
        super().__init__('images/left.png', 'Arquímedes', 'Principio de Arquímedes')
    
    def main_frame(self, master):
        frame = Frame(master, bg=master['bg'])
        entries = [
            ('Empuje (E):', 'N'),
            ('Densidad de fluído (ρ):', 'Kg/m3'),
            ('Peso aparente (Wa):', 'N'),
            ('Peso (w):', 'N'),
            ('Masa (m):', 'Kg'),
            ('Volumen (v):', 'm3'),
            ('Densidad del material (ρmat):', 'Kg/m3')
        ]
        self.entries = EntryFrame(frame, entries, padx=10, pady=10)
        self.entries.pack(side='top', expand=True)

        buttons = [
            [('Limpiar...', self.entries.clear), ('Calcular...', lambda: self.calculate(self.entries.get_values()))]
        ]
        self.buttons = ButtonFrame(self.entries, buttons)
        self.buttons.grid(row=7, column=1)
        return frame
    
    def bottom_frame(self, master):
        frame = Frame(master, bg='red')
        return frame
    
    def load(self, master, event=None, func=None):
        frame = Frame(master, bg=master['bg'])
        bottom_frame = self.bottom_frame(frame)
        bottom_frame['width'] = 300
        bottom_frame.pack(side='right', fill='y')
        header_frame = self.header(frame)
        header_frame.pack(side='top', fill='x')
        main_frame = self.main_frame(frame)
        main_frame.pack(side='top', expand=True, fill='both')
        Frame(frame, bg='blue').pack(side='top', expand=True, fill='both')
        if event:
            header_frame.bind(event, func)
            main_frame.bind(event, func)
            bottom_frame.bind(event, func)
        return frame
    
    def calculate(self, values):
        empuje, densidad, paparente, peso, masa, volumen, denmaterial = values

        match (denmaterial != None, volumen != None, masa != None):
            case (False, True, True): denmaterial = masa / volumen
            case (True, False, True): volumen = masa / denmaterial
            case (True, True, False): masa = denmaterial * volumen
        
        match (empuje != None, paparente != None, peso != None):
            case (False, True, True): empuje = peso - paparente
            case (True, False, True): paparente = peso - empuje
            case (True, True, False): peso = empuje + paparente
        
        match (masa != None, peso != None):
            case (False, True): masa = peso / 9.81
            case (True, False): peso = masa * 9.81
        
        match (empuje != None, densidad != None, volumen != None):
            case (False, True, True): empuje = 9.81 * densidad * volumen
            case (True, False, True): densidad = empuje / (9.81 * volumen)
            case (True, True, False): volumen = empuje / (9.81 * densidad)
        
        new_values = [empuje, densidad, paparente, peso, masa, volumen, denmaterial]
        if new_values != values: self.calculate(new_values.copy())
        else: self.entries.insert(new_values)

class Dilatacion(Module):
    def __init__(self):
        super().__init__('images/left.png', 'Dilatación')
    
    def main_frame(self, master):
        frame = Frame(master, bg=master['bg'])
        entries = [
            ('Dimensión inicial', ''),
            ('Dimensión final', ''),
            ('Diferencia de dimensión', ''),
            ('Temperatura inicial', '°C'),
            ('Temperatura final', '°C'),
            ('Diferencia de temperatura', '°C'),
            ('Coeficiente', '°C-1')
        ]
        self.entries = EntryFrame(frame, entries, padx=10, pady=10)
        self.entries.pack(side='top', expand=True)

        self.unit = Combobox(self.entries, width=25)
        self.unit['values'] = (
            'Lineal',
            'Superficial',
            'Volumétrico'
        )
        self.unit.current(0)
        self.unit.grid(row=7, column=1)

        buttons = [
            [('Limpiar...', self.entries.clear), ('Calcular...', lambda: self.calculate(self.entries.get_values()))]
        ]
        self.buttons = ButtonFrame(self.entries, buttons, width=100, height=20)
        self.buttons.grid(row=8, column=1, pady=10)
        return frame
    
    def bottom_frame(self, master):
        frame = Frame(master, bg='red')
        return frame
    
    def load(self, master, event=None, func=None):
        frame = Frame(master, bg=master['bg'])
        header_frame = self.header(frame)
        header_frame.pack(side='top', fill='x')
        main_frame = self.main_frame(frame)
        main_frame.pack(side='top', expand=True, fill='both')
        bottom_frame = self.bottom_frame(frame)
        bottom_frame.pack(side='top', expand=True, fill='both')
        if event:
            header_frame.bind(event, func)
            main_frame.bind(event, func)
            bottom_frame.bind(event, func)
        return frame
    
    def calculate(self, values):
        print(values)
        
        new_values = []
        if new_values != values and new_values: self.calculate(new_values.copy())
        else: self.entries.insert(new_values)

class Cinematica(Base):
    def __init__(self):
        modules = [
            Uniforme,
            Variado,
        ]
        super().__init__('images/left.png', 'Cinemática', modules)

class Uniforme(Module):
    def __init__(self):
        super().__init__('images/left.png', 'Uniforme acelerado')

class Variado(Module):
    def __init__(self):
        super().__init__('images/left.png', 'Variado acelerado')