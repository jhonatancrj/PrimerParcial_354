# -*- coding: utf-8 -*-
"""RESPUESTA_4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qv5huBQYOOBvomOG6vwvik4euseLkX04
"""

from google.colab import drive
drive.mount('/content/drive')

# Instalar sklearn en caso de que no esté instalado (opcional)
!pip install -U scikit-learn pandas

import pandas as pd
from scipy.io import arff
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, KBinsDiscretizer, MinMaxScaler

from scipy.io import arff
import pandas as pd

# Cargar el archivo ARFF
file_path = '/content/drive/MyDrive/datos/diabetes_datos.arff'
data, meta = arff.loadarff(file_path)

# Convertir a DataFrame
df = pd.DataFrame(data)

# Mostrar las primeras filas del dataset
df.head()

from sklearn.preprocessing import LabelEncoder

# Ejemplo con la columna 'Sex'
le = LabelEncoder()
df['Sex_encoded'] = le.fit_transform(df['Sex'])

# Ver resultados
df[['Sex', 'Sex_encoded']].head()

from sklearn.preprocessing import OneHotEncoder

# Crear un OneHotEncoder
ohe = OneHotEncoder()

# Aplicar el encoder
sex_onehot = ohe.fit_transform(df[['Sex']]).toarray()

# Convertir a DataFrame para mejor visualización
sex_onehot_df = pd.DataFrame(sex_onehot, columns=ohe.get_feature_names_out(['Sex']))

# Añadir las columnas al dataframe original
df = pd.concat([df, sex_onehot_df], axis=1)

# Ver resultados
df[['Sex'] + list(sex_onehot_df.columns)].head()

from sklearn.preprocessing import KBinsDiscretizer

# Discretizar la columna 'Age' en 3 categorías
kbins = KBinsDiscretizer(n_bins=3, encode='ordinal', strategy='uniform')
df['Age_discretized'] = kbins.fit_transform(df[['Age']])

# Ver resultados
df[['Age', 'Age_discretized']].head()

from sklearn.preprocessing import MinMaxScaler

# Normalizar la columna 'BMI'
scaler = MinMaxScaler()
df['BMI_normalized'] = scaler.fit_transform(df[['BMI']])

# Ver resultados
df[['BMI', 'BMI_normalized']].head()

# Mostrar el dataframe con las nuevas columnas
df.head()