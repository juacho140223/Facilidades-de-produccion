# Univesidad Central del Ecuador
# Carrera de Petroleos
# Materia: Facilidades de Producción
# Integrantes: Juan Salazar, Jessica Villacis

# Tendencia del petróleo en los últimos diez años
import numpy as np
import pandas as pd
import pymannkendall as mk
import matplotlib.pyplot as plt
import statsmodels.api as sm


# Create dataset

oil_data = pd.read_csv('Datos-históricos-Futuros-petróleo-crudo-WTI.csv',parse_dates=['Fecha'],index_col='Fecha')

# Tedencia

resultado = mk.original_test(oil_data,alpha=0.05)
nombres = ["Tendencia","Presencia de tendencia","p-valor","Estadística de prueba","Tau Kendall","Puntaje de Kendall","Varianza S","Intercepto"]

for i,j in zip(nombres,resultado):
    print(i,":",j)

data = oil_data
fig, ax = plt.subplots(figsize=(12, 8))
res = mk.hamed_rao_modification_test(data)
trend_line = np.arange(len(data)) * res.slope + res.intercept

ax.plot(data)
ax.plot(data.index, trend_line)
ax.legend(['data', 'trend line'])


