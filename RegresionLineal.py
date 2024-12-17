import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.preprocessing import StandardScaler
from math import sqrt

# Cargar los datos desde el CSV
df = pd.read_csv("poligonos_data.csv")

# Separar las características (longitudes de los lados) y la variable objetivo (área)
X = df.drop(columns=["area"])  # Las longitudes de los lados (entradas)
y = df["area"]  # El área (salida)

# Normalizar los datos para que todas las características tengan la misma escala
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Dividir los datos en conjunto de entrenamiento y conjunto de prueba
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Crear un modelo de regresión lineal
model = LinearRegression()

# Entrenar el modelo
model.fit(X_train, y_train)

# Hacer predicciones con los datos de prueba
y_pred = model.predict(X_test)

# Evaluar el modelo con el MSE
mse = mean_squared_error(y_test, y_pred)
print(f"Error Cuadrático Medio (MSE): {mse}")

# Calcular el RMSE (Raíz del Error Cuadrático Medio)
rmse = sqrt(mse)
print(f"Raíz del Error Cuadrático Medio (RMSE): {rmse}")

# Evaluar el modelo con MAE (Error Absoluto Medio)
mae = mean_absolute_error(y_test, y_pred)
print(f"Error Absoluto Medio (MAE): {mae}")

# Evaluar el modelo con R² (Coeficiente de Determinación)
r2 = r2_score(y_test, y_pred)
print(f"Coeficiente de Determinación (R²): {r2}")

# Calcular el Error Absoluto Relativo (ARE) y el porcentaje de acierto
error_absoluto_relativo = np.abs((y_test - y_pred) / y_test)
porcentaje_acierto = 100 - np.mean(error_absoluto_relativo) * 100
print(f"Porcentaje de acierto: {porcentaje_acierto}%")

# Ver los coeficientes del modelo y la intercepción
print(f"Coeficientes del modelo: {model.coef_}")
print(f"Intercepción: {model.intercept_}")

# Hacer predicciones para nuevos polígonos (ejemplo de entrada)
nuevas_longitudes = np.array([[3.5, 4.2, 3.8, 2.0, 4.1, 0, 0, 0, 0, 0]])  # Asegúrate de usar 10 longitudes
nuevas_longitudes_scaled = scaler.transform(nuevas_longitudes)
prediccion_area = model.predict(nuevas_longitudes_scaled)
print(f"Predicción del área para nuevas longitudes: {prediccion_area[0]}")
