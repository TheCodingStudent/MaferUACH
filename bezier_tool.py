import pygame
from pygame.math import Vector2

pygame.init()
SCREEN = pygame.display.set_mode((1000, 1000))
WIDTH, HEIGHT = SCREEN.get_size()
RUNNING = True

class Point:
    def __init__(self, pos):
        self.pos = Vector2(pos)
    
    def show(self):
        pygame.draw.circle(SCREEN, 'white', self.pos, RADIUS, width=1)
    
    def move(self, rel):
        self.pos += Vector2(rel)

CURVE = []
POINTS = [
    Point((0, 0)),
    Point((1000, 0)),
    Point((800, 1000)),
    Point((800, 1000)),
    Point((800, 1000)),
    Point((1000, 0)),
    Point((1000, 1000)),
]
SELECTED = None
RADIUS = 20

def add_point(pos, button):
    click_pos = Vector2(pos)
    for point in POINTS:
        if click_pos.distance_to(point.pos) < RADIUS: 
            if button == 1: return point
            POINTS.remove(point)
    if button == 1: POINTS.append(Point(pos))
    get_curve()
    return None

def get_point(points, t):
    if len(points) == 1: return points[0]
    new_points = []
    for i in range(len(points)-1):
        a = points[i]
        b = points[i+1]
        p = a.lerp(b, t)
        new_points.append( p )
    return get_point(new_points, t)

def get_curve(steps=100):
    global CURVE
    points = [point.pos for point in POINTS]
    CURVE = []
    for t in range(steps):
        point = get_point(points, t/steps)
        CURVE.append(point)

while RUNNING:
    SCREEN.fill('black')
    for event in pygame.event.get():
        match (event.type, SELECTED != None):
            case (pygame.QUIT, _): RUNNING = False
            case (pygame.MOUSEBUTTONDOWN, _): SELECTED = add_point(event.pos, event.button)
            case (pygame.MOUSEBUTTONUP, _): SELECTED = None
            case (pygame.MOUSEMOTION, True): 
                SELECTED.move(event.rel)
                get_curve()
    
    for point in POINTS:
        point.show()
    
    for point in CURVE:
        if point: pygame.draw.circle(SCREEN, 'red', point, 1)
    
    pygame.display.update()

for point in POINTS:
    print(point.pos)
        