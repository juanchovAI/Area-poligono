
def crear_funcion(punto1, punto2):
    invalida = False
    x1, y1 = punto1
    x2, y2 = punto2

    if x2 - x1 != 0 :
        m = (y2 - y1) / (x2 - x1)
    
    else: 
        m = (y2 - y1) / (x2 + 0.01 - x1)
        invalida = True
       # raise ValueError("Los puntos tienen el mismo X lo que ocaciona una división por cero")
    
    b= y1 - m * x1

    def fx_recta(x):
        return m * x + b
    
    return fx_recta, m, b, invalida

