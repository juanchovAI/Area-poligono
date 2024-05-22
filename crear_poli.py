import matplotlib.pyplot as plt
import numpy as np 
import random
from crear_fx import crear_funcion
from calcular_area import shoelace_area
from obtener_vertices import obtener_vertices
from scipy.spatial import ConvexHull, QhullError


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

    try:
        hull = ConvexHull(puntos)
        hull_puntos = [puntos[i] for i in hull.vertices]
        for i in range(len(hull_puntos)):
            punto1 = hull_puntos[i]
            punto2 = hull_puntos[(i + 1) % len(hull_puntos)]
            aristas.append((punto1, punto2))
    except QhullError as e:
        punto1 = (min(p[0] for p in puntos), min(p[1] for p in puntos))
        punto2 = (max(p[0] for p in puntos), max(p[1] for p in puntos))
        aristas.append((punto1, punto2))


    funciones = []
    coeficientes = []
    fx_invalida = False
    
    for i in aristas:
        func, m, b, invalida = crear_funcion(i[0], i[1])

        if func == False:
            return
        funciones.append(func)
        coeficientes.append((m, b))
        if invalida == True:
            fx_invalida = invalida


    def verificar_poligono_valido(funciones):
        n = len(funciones)
        for i in range(n):
            for j in range(i + 1, n):
                m1, b1 = coeficientes[i]
                m2, b2 = coeficientes[j]
                if m1 != m2:  
                    x_interseccion = (b2 - b1) / (m1 - m2)
                    y_interseccion = m1 * x_interseccion + b1
                    if (min(aristas[i][0][0], aristas[i][1][0]) <= x_interseccion <= max(aristas[i][0][0], aristas[i][1][0]) and
                        min(aristas[j][0][0], aristas[j][1][0]) <= x_interseccion <= max(aristas[j][0][0], aristas[j][1][0])):
                        print(f"Las aristas {i+1} y {j+1} se intersectan en el punto ({x_interseccion}, {y_interseccion}), lo cual no debería suceder en un polígono válido.")
                else:
                    print(f"Las aristas {i+1} y {j+1} son paralelas y no se intersectan.")

    #verificar_poligono_valido(funciones)

    plt.figure(figsize=(3,3.5))
    for i in range(0, len(funciones) ): 
        dominio = []
        rango = []
        if(aristas[i][0][0] < aristas[i][1][0]):
            dominio = np.arange(aristas[i][0][0], aristas[i][1][0] + 0.01)
            rango = [funciones[i](x) for x in dominio]
        elif(aristas[i][0][0] == aristas[i][1][0]):
            if(aristas[i][1][1] < aristas[i][0][1]):
                rango = np.arange(aristas[i][1][1], aristas[i][0][1] + 0.01)
                dominio = [funciones[i](x) for x in rango]
            else:
                rango = np.arange(aristas[i][0][1], aristas[i][1][1] + 0.01)
                dominio = [funciones[i](x) for x in rango]
        else:
            dominio = np.arange(aristas[i][1][0], aristas[i][0][0] + 0.01)
            rango = [funciones[i](x) for x in dominio]
        
        plt.plot(dominio, rango, "black", linewidth = 2)
        print(dominio, rango,)
        

    plt.xlim(0,5)
    plt.ylim(0,5)
    plt.xticks([1,2,3,4,5])
    plt.yticks([1,2,3,4,5])
    plt.grid()


    vertices = obtener_vertices(aristas)


    area = round(shoelace_area(vertices))
    
    if fx_invalida == False:
        plt.savefig(f"./imgs/A_{area}_{random.randint(1,9999999999)}.jpg")