from crear_poli_copy import crear_poli
import pandas as pd
import numpy as np


array_support_final = np.empty((0, 11))  # 10 longitudes + 1 área

for i in range(200000):
    longitudes, area = crear_poli()
    fila = np.array(longitudes + [area])  # Combinar longitudes y área en una fila
    array_support_final = np.vstack((array_support_final, fila))  # Agregar la fila al array final

# Crear el DataFrame con los datos
array_support_df = pd.DataFrame(array_support_final, columns=[f"longitud_{i+1}" for i in range(10)] + ["area"])

# Eliminar duplicados
array_support_df = array_support_df.drop_duplicates()

# Guardar el DataFrame en un archivo CSV
array_support_df.to_csv("poligonos_data.csv", index=False)

print("CSV creado exitosamente con las longitudes y el área.")