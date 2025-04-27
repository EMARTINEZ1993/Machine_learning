import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import pickle

# Dataset de entrenamiento
data = {
    'fuma': ['si', 'no', 'si', 'no', 'si'],
    'sexo': ['masculino', 'femenino', 'masculino', 'femenino', 'femenino'],
    'peso': [70, 60, 80, 55, 65],
    'estatura': [170, 160, 180, 155, 165],
    'edad': [45, 34, 23, 56, 30],
    'enfermedad': ['Gripe', 'Ninguna', 'COVID-19', 'Bronquitis', 'Gripe']
}

# Crear DataFrame
df = pd.DataFrame(data)

# Codificación de columnas categóricas
le_fuma = LabelEncoder()
le_sexo = LabelEncoder()
le_enfermedad = LabelEncoder()

df['fuma'] = le_fuma.fit_transform(df['fuma'])
df['sexo'] = le_sexo.fit_transform(df['sexo'])
df['enfermedad'] = le_enfermedad.fit_transform(df['enfermedad'])

# Separar características (X) y variable objetivo (y)
X = df[['fuma', 'sexo', 'peso', 'estatura', 'edad']]
y = df['enfermedad']

# División de datos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar modelo
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Guardar modelo y codificador
pickle.dump(model, open('diagnostico/static/modelo_entrenado.pkl', 'wb'))
pickle.dump(le_enfermedad, open('diagnostico/static/le_enfermedad.pkl', 'wb'))
