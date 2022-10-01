##### IMPORTAR LIBRERIAS #####
import pygame

class Bezier:
    """
    La clase Bezier toma como argumento una serie de puntos de control
    y permite evaluar el progreso de la curva entre el intervalo [0, 1].
    """
    def __init__(self, points, rng, width=1):
        self.width = width                                              # ancho de la curva
        self.range = [step/rng for step in range(rng+1)]                # rango de divisiones de la curva
        self.points = [pygame.math.Vector2(point) for point in points]  # vectores para puntos de control
        self.get_curve()                                                # obtenemos la curva

    def get_point(self, points, t):
        """
        Una curva bezier de n grado se puede calcular generando
        curvas bezier de un grado menor, por ejemplo una curva
        de segundo grado se obtiene generando curvas de primer grado
        entre los puntos (A-B) y (B-C), estos a su vez son interpolados
        y generan una nueva curva de primer grado (ABt-BCt) y esta a su
        vez es interpolada y nos da un punto P, y asi interpolamos t de 
        0 a 1.
        """
        if len(points) == 1: return points[0]   # si solo hay un punto entonces lo regresamos
        new_points = []                         # esta sera la lista con los nuevos puntos, la curva bezier es recursiva
        for i in range(len(points)-1):          # iteramos por cada punto en lista de puntos
            a = points[i]                       # punto inicial
            b = points[i+1]                     # punto final
            p = a.lerp(b, t)                    # p es el punto que se encuentra en el porcentaje t de la recta
            new_points.append( p )              # añadimos el punto p a la lista de nuevos puntos
        return self.get_point(new_points, t)    # volvemos a llamar a la funcion pero con los nuevos puntos
    
    def get_curve(self):
        self.curve = []                             # lista de puntos que conforman la curva
        for t in self.range:                        # iteramos por cada t en el rango de la curva
            point = self.get_point(self.points, t)  # obtenemos el punto en el intervalo t
            self.curve.append(point * self.width)   # añadimos el punto a la lista de puntos
    
    def eval(self, t):
        return self.curve[t][1]     # accedemos a la curva en el intervalo t y regresamos el punto