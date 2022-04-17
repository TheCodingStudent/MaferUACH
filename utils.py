from pygame.math import Vector2

def lerp(a, b, t):
    return a + (b - a) * t

def rgb_to_hex(*rgb):
    r, g, b = int(rgb[0]), int(rgb[1]), int(rgb[2])
    return  '#{:02x}{:02x}{:02x}'.format(r, g, b)

def hex_to_rgb(value):
    if not value.startswith('#'): value = '#ffffff'
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

def opacity(hex_color, opacity):
    r, g, b = hex_to_rgb(hex_color)                                              
    nr, ng, nb = r * opacity, g * opacity, b * opacity    
    return rgb_to_hex(nr, ng, nb)

def light(hex_color, light):
    r, g, b = hex_to_rgb(hex_color)                                              
    nr, ng, nb = lerp(r, 255, light), lerp(g, 255, light), lerp(b, 255, light)    
    return rgb_to_hex(nr, ng, nb)

def color_lerp(a, b, t):
    ar, ag, ab = hex_to_rgb(a)
    br, bg, bb = hex_to_rgb(b)
    nr, ng, nb = lerp(ar, br, t), lerp(ag, bg, t), lerp(ab, bb, t)
    return rgb_to_hex(nr, ng, nb)

class Bezier:
    def __init__(self, points, rng, width=1):
        self.width = width
        self.range = [step/rng for step in range(rng+1)]
        self.points = [Vector2(point) for point in points]
        self.get_curve()

    def get_point(self, points, t):
        if len(points) == 1: return points[0]
        new_points = []
        for i in range(len(points)-1):
            a = points[i]
            b = points[i+1]
            p = a.lerp(b, t)
            new_points.append( p )
        return self.get_point(new_points, t)
    
    def get_curve(self):
        self.curve = []
        for t in self.range:
            point = self.get_point(self.points, t)
            self.curve.append(point * self.width)
    
    def eval(self, t):
        return self.curve[t][1]

    
def rgb_to_hsl(r, g, b):
    r = float(r)
    g = float(g)
    b = float(b)
    high = max(r, g, b)
    low = min(r, g, b)
    h, s, v = ((high + low) / 2,)*3

    if high == low:
        h = 0.0
        s = 0.0
    else:
        d = high - low
        s = d / (2 - high - low) if v > 0.5 else d / (high + low)
        h = {
            r: (g - b) / d + (6 if g < b else 0),
            g: (b - r) / d + 2,
            b: (r - g) / d + 4,
        }[high]
        h /= 6

    return 240*h, (360*s%240), v

print(rgb_to_hsl(191, 64, 128))