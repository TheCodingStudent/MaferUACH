##### IMPORTAR LIBRERIAS #####
import json
from colorsys import rgb_to_hls, hls_to_rgb

##### ESTILO #####
def get_style():
    with open('style.json') as f:   # abre el archivo
        data = json.load(f)         # obtenemos la informacion y la guardamos
    return data                     # regresamos la informacion

rgb_to_hex = lambda r, g, b: '#%02x%02x%02x' % (int(r), int(g), int(b))     # convierte colores (r, g, b) a #rrggbb
hex_to_rgb = lambda color: tuple(int(color[i:i+2], 16) for i in (1, 3, 5))  # convierte colores #rrggbb a (r, g, b)
hex_to_hls = lambda color: rgb_to_hls(*hex_to_rgb(color))                   # convierte colores #rrggbb a (h, s, l)

def hls_to_hex(h, l, s):                            # convierte colores (h, s, l) a #rrggbb
    r, g, b = hls_to_rgb(h, l, s)
    return int(255*r), int(255*g), int(255*b)

def atenuate(color, light, saturation):                 # toma un color #rrggbb y le aplica la saturacion e iluminacion deseada
    h, _, _ = rgb_to_hls(*hex_to_rgb(color))            # esto es muy util para escalas monocromaticas
    r, g, b = hls_to_rgb(h, light/240, saturation/240)
    return rgb_to_hex(255*r, 255*g, 255*b)