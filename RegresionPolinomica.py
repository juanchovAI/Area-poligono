from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import pandas as pd
import numpy as np
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

df = pd.read_csv("poligonos_data.csv")

X = df.drop(columns=["area"])  
y = df["area"]  

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

poly = PolynomialFeatures(degree=2)  
X_poly = poly.fit_transform(X)


X_train, X_test, y_train, y_test = train_test_split(X_poly, y, test_size=0.2, random_state=42)


model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
print(f"Error Cuadrático Medio (MSE) para la regresión polinómica: {mse}")


error_absoluto_relativo = np.abs((y_test - y_pred) / np.where(y_test != 0, y_test, 1)) 
porcentaje_acierto = 100 - np.mean(error_absoluto_relativo) * 100
print(f"Porcentaje de acierto: {porcentaje_acierto}%")

