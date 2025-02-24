"""
Objetivo:
Aplicar técnicas de Feature Engineering en un dataset real de calidad del aire, incluyendo transformación de variables, encoding de datos categóricos y generación de variables temporales.

Descargar y cargar el dataset "Air Quality Data in India" disponible en Kaggle:
🔗 https://www.kaggle.com/datasets/rohanrao/air-quality-data-in-india
    Realizar preprocesamiento de datos para manejar valores nulos y duplicados.
    Contabilizar los registros con valores nulos  y llenarlos con el valor de la media de su columna.
    Eliminar los registros duplicados (mostrando cuántos registros había antes y después de eliminarlos)
    Eliminar las columnas irrelevantes como: "Xylene", "Benzene"]
Aplicar técnicas de Feature Engineering, como:
    Generación de variables temporales, es decir, crea 5 columnas extra en la tabla (date (de tipo datetime para facilitar la manipulación, year donde sólo extraiga el año, month, para mes, day para día y weekday para que ponga el día de la semana que fue (del 0 al 6)
    Encoding de datos categóricos, es decir, convertir la columna "City" en variables dummy (0 o 1) para cada categoría distinta en esa columna, creando nuevas columnas con nombres basados en los valores únicos de "City".
    Realiza una transformación logarítmica a las columnas "PM2.5" y "CO", ya que dichos datos suelen tener una distribución sesgada a la derecha. y queremos una distribución normal.
    Documenta cada operación que hagas y explica la ventaja de su uso.

https://chat.deepseek.com/a/chat/s/e1989d17-92b2-4e9e-b2ce-fee0b03cbc85
"""
import pandas as pd

cityDayDF = pd.read_csv('city_day.csv')
cityHourDF = pd.read_csv('city_hour.csv')
stationDayDF = pd.read_csv('station_day.csv')
stationHourDF = pd.read_csv('station_hour.csv',low_memory=False)
stationsDF = pd.read_csv('stations.csv')

datasheetCombinadas = pd.concat([cityDayDF,cityHourDF,stationDayDF,stationHourDF,stationsDF],axis=1)

datasheetCombinadas.isnull().duplicated()

