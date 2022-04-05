from modules.common import *
import utils

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
        super().__init__('images/left.png', 'Arquimides', 'Principio de Arquimides')
    
    def main_frame(self, master):
        frame = Frame(master, bg=master['bg'])
        entries = [
            ('Empuje (E):', 'N'),
            ('Densidad de fluido (ρ):', 'Kg/m3'),
            ('Peso aparente (Wa):', 'N'),
            ('Peso (w):', 'N'),
            ('Masa (m):', 'Kg'),
            ('Volumen (v):', 'm3'),
            ('Densidad del material (ρmat):', 'Kg/m3')
        ]
        text_config = {
            'bg': master['bg'],
            'fg': '#311b92',
            'font': 'Arial 12'
        }
        entry_config = {
            'bg': 'white',
            'fg': 'black',
            'selectbackground': '#651fff',
            'selectforeground': '#ede7f6',
            'relief': 'flat',
            'width': 20,
            'font': 'Arial 12'
        }
        self.entries = EntryFrame(frame, entries, padx=10, pady=10)
        self.entries.style(text_config, entry_config)
        self.entries.pack(side='top', expand=True)

        buttons = [
            [('Limpiar...', self.entries.clear), ('Calcular...', lambda: self.calculate(self.entries.get_values()))]
        ]
        button_config = {
            'width': 100,
            'height': 20,
            'bg': '#b39ddb'
        }
        self.buttons = ButtonFrame(self.entries, buttons)
        self.buttons.style(button_config)
        self.buttons.grid(row=7, column=1)
        return frame
    
    def bottom_frame(self, master):
        frame = Frame(master, bg='red')
        return frame
    
    def load(self, master):
        frame = Frame(master, bg=master['bg'])
        self.header(frame).pack(side='top', fill='x')
        self.main_frame(frame).pack(side='top', expand=True, fill='both')
        self.bottom_frame(frame).pack(side='top', expand=True, fill='both')
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
        super().__init__('images/left.png', 'Dilatacion')

class Cinematica(Base):
    def __init__(self):
        modules = [
            Uniforme,
            Variado,
        ]
        super().__init__('images/left.png', 'Cinematica', modules)

class Uniforme(Module):
    def __init__(self):
        super().__init__('images/left.png', 'Uniforme acelerado')

class Variado(Module):
    def __init__(self):
        super().__init__('images/left.png', 'Variado acelerado')