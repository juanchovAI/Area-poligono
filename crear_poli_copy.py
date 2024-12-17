import pandas as pd
import numpy as np
import random
from scipy.spatial import ConvexHull, QhullError
from crear_fx import crear_funcion
from calcular_area import shoelace_area
from obtener_vertices import obtener_vertices

def crear_poli():
    puntos = []  
    numero_random_puntos = random.randint(3, 10)

    def crear_punto():
        x = random.randint(0, 5)
        y = random.randint(0, 5)
        return (x, y)

    for i in range(numero_random_puntos):
        puntos.append(crear_punto())

    aristas = []
    if len(puntos) < 3:
        raise ValueError("Se necesitan al menos 3 puntos no colineales para calcular el ConvexHull.")

    try:
        hull = ConvexHull(puntos)
        hull_puntos = [puntos[i] for i in hull.vertices]
        for i in range(len(hull_puntos)):
            punto1 = hull_puntos[i]
            punto2 = hull_puntos[(i + 1) % len(hull_puntos)]
            aristas.append((punto1, punto2))

    except QhullError:
        punto1 = (min(p[0] for p in puntos), min(p[1] for p in puntos))
        punto2 = (max(p[0] for p in puntos), max(p[1] for p in puntos))
        aristas.append((punto1, punto2))
        hull_puntos = [punto1, punto2]

    # Calcular las longitudes de los lados
    longitudes = []
    for i in range(len(hull_puntos)):
        punto1 = hull_puntos[i]
        punto2 = hull_puntos[(i + 1) % len(hull_puntos)]
        longitud = np.sqrt((punto2[0] - punto1[0])**2 + (punto2[1] - punto1[1])**2)
        longitudes.append(longitud)


    max_vertices = 10
    while len(longitudes) < max_vertices:
        longitudes.append(0) 
    longitudes = longitudes[:max_vertices]  


    area = np.ceil(shoelace_area(hull_puntos))

    print(longitudes, area)

    return longitudes, area