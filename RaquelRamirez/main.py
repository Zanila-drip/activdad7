"""
Cargar el iris_dataset.csv en un DataFrame
    Mostrar las primeras 5 filas del DataFrame
    e
    Identificar la columna categórica target.
Aplicar Label Encoding:
    Importar LabelEncoder de sklearn.preprocessing.
    Convertir la columna target en valores numéricos.
    Agregar la nueva columna target_label al DataFrame.
Aplicar One-Hot Encoding:
    Usar pd.get_dummies() para transformar la columna target.
    Agregar las nuevas columnas generadas al DataFrame.
"""
import pandas as pd
from sklearn.preprocessing import LabelEncoder


df = pd.read_csv('iris.csv')

#print(df.describe().head())
#print(df["target"].head())

#enconder = LabelEncoder()

#print(df['target'].unique())
#enconder.fit(df['target'])
#enconder.classes_
#print(enconder.transform(df['target']))

#dummy_Target = pd.get_dummies(df['target'])
#print(dummy_Target.head())
