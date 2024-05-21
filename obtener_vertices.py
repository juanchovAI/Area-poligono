def obtener_vertices(aristas):
    vertices = set()  
    for arista in aristas:
        punto1, punto2 = arista
        vertices.add(punto1)
        vertices.add(punto2)

    return list(vertices)