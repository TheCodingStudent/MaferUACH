from pygame.math import Vector2

def rgb2hex(*rgb):
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
    return rgb2hex(nr, ng, nb) 

class Bezier:
    def __init__(self, points, rng, width=1, start=(0, 0)):
        self.width = width
        self.start = Vector2(start)
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
            self.curve.append(point * self.width + self.start)
    
    def eval(self, t):
        return self.curve[t][1]