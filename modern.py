from tkinter import Frame, Label, Tk
from utils import Bezier, color_lerp, lerp, rgb_to_hex

class FlatButton(Frame):
    def __init__(self, master, text, expand=1, **kwargs):
        super().__init__(master, **kwargs)

        ##### PROPERTIES #####
        self.on_animation = False
        self.expand = expand
        self.time = 50
        self.width, self.height = self['width'], self['height']
        self.final_width, self.final_height = 300, 300
        self.curve = Bezier([(0, 0), (1, 1)], self.time, expand)

        ##### BUTTON STYLE #####
        self.base_color = self['bg']
        self.highlight_color = "#00ffff"

        ##### TEXT STYLE #####
        self.font_size = 12
        self.font = 'Arial'
        self.font_color = '#ffffff'
        self.final_font_size = 18

        ##### COMPONENTS #####
        self.text = Label(self, text=text, fg=self.font_color, bg=self['bg'], font=f'{self.font} {self.font_size}')
        self.text.place(relx=0.5, rely=0.5, anchor='center')

        ##### CONNECTIONS #####
        self.bind('<Enter>', self.hover)
        self.bind('<Leave>', self.unhover)
    
    def update_values(self, rng):
        if self.on_animation: return
        self.on_animation = True
        for t in rng:
            percent = self.curve.eval(t) / self.expand
            self['width'] = lerp(self.width, self.final_width, percent)
            self['height'] = lerp(self.height, self.final_height, percent)
            new_bg = color_lerp(self.base_color, self.highlight_color, percent)
            self['bg'] = new_bg
            self.text['bg'] = new_bg
            self.text['font'] = f'{self.font} {int(lerp(self.font_size, self.final_font_size, percent))}'
            self.update()
        self.on_animation = False
    
    def hover(self, event):
        self.update_values(range(1, self.time+1))
    
    def unhover(self, event):
        self.update_values(reversed(range(1, self.time+1)))

window = Tk()
window.geometry('800x600')

button = FlatButton(window, 'Hola', width=200, height=50, bg='#262626')
button.place(relx=0.5, rely=0.5, anchor='center')

window.mainloop()