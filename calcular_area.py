import math

def shoelace_area(vertices):

    vertices = list(dict.fromkeys(vertices))
    
    if len(vertices) < 3:
        return 0

    def ordenar_puntos(vertices):
        centro_x = sum([v[0] for v in vertices]) / len(vertices)
        centro_y = sum([v[1] for v in vertices]) / len(vertices)
        
        def angulo(p):
            return math.atan2(p[1] - centro_y, p[0] - centro_x)
        
        return sorted(vertices, key=angulo)
    
    vertices = ordenar_puntos(vertices)

    vertices.append(vertices[0])

    S1 = 0
    S2 = 0

    for i in range(len(vertices) - 1):
        S1 += vertices[i][0] * vertices[i + 1][1]
        S2 += vertices[i][1] * vertices[i + 1][0]

    area = abs(S1 - S2) / 2
    
    return area