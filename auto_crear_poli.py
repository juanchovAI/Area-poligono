from crear_poli_copy import crear_poli
import pandas as pd
import numpy as np


array_support_final = np.empty((0,11))

for i in range(0,20000):
    soporte, auxiliar = crear_poli()
    array_support_final = np.vstack((array_support_final, soporte))
    array_support_final = np.vstack((array_support_final, auxiliar))

array_support_df = pd.DataFrame(array_support_final, columns=[1,2,3,4,5,6,7,8,9,10,'convexo'])
array_support_df = array_support_df.drop_duplicates()
