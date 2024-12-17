from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.preprocessing import StandardScaler
from math import sqrt

df = pd.read_csv("poligonos_data.csv")

X = df.drop(columns=["area"])  
y = df["area"]  

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

df = pd.read_csv("poligonos_data.csv")

X = df.drop(columns=["area"])  
y = df["area"]  

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


mlp_model = MLPRegressor(hidden_layer_sizes=(3000,), max_iter=30000, random_state=42)
mlp_model.fit(X_train, y_train)


y_pred = mlp_model.predict(X_test)


mse = mean_squared_error(y_test, y_pred)
print(f"Error Cuadrático Medio (MSE) para la red neuronal: {mse}")

error_absoluto_relativo = np.abs((y_test - y_pred) / np.where(y_test != 0, y_test, 1))  
porcentaje_acierto = 100 - np.mean(error_absoluto_relativo) * 100
print(f"Porcentaje de acierto: {porcentaje_acierto}%")



# Error en el conjunto de entrenamiento
y_train_pred = mlp_model.predict(X_train)
mse_train = mean_squared_error(y_train, y_train_pred)
r2_train = r2_score(y_train, y_train_pred)
print(f"Error Cuadrático Medio (MSE) en entrenamiento: {mse_train}")
print(f"R² en entrenamiento: {r2_train}")

# Error en el conjunto de prueba (ya calculado, pero aquí lo organizamos mejor)
mse_test = mean_squared_error(y_test, y_pred)
r2_test = r2_score(y_test, y_pred)
print(f"Error Cuadrático Medio (MSE) en prueba: {mse_test}")
print(f"R² en prueba: {r2_test}")

# Diferencia entre entrenamiento y prueba
print(f"Diferencia de MSE: {mse_train - mse_test}")