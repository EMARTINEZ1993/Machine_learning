import pandas as pd

# Simulación de un dataset con los campos mencionados
data = {
    "nombre": ["Juan", "Ana", "Pedro", "Maria"],
    "edad": [45, 34, 23, 56],
    "peso": [70, 60, 80, 90],
    "fuma": ["si", "no", "si", "no"],
    "sexo": ["masculino", "femenino", "masculino", "femenino"],
    "antecedentes_medicos": ["ninguno", "diabetes", "hipertensión", "asma"],
    "sintomas_generales": ["fiebre, dolor de cabeza", "fatiga, pérdida de peso", "dolor abdominal", "tos, dificultad para respirar"],
    "enfermedad": ["Gripe", "Diabetes", "Gastroenteritis", "Neumonía"]
}

# Convertirlo en un DataFrame
df = pd.DataFrame(data)
