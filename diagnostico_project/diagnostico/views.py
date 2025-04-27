from django.shortcuts import render
from .forms import DiagnosticoForm
from .models import Diagnostico
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# Simulamos un dataset para el ejemplo
def diagnostico(request):
    if request.method == "POST":
        form = DiagnosticoForm(request.POST)
        if form.is_valid():
            # Tomamos los datos del formulario
            nombre = form.cleaned_data['nombre']
            sintomas_generales = form.cleaned_data['sintomas_generales']

            # Usamos el modelo de ML para predecir la enfermedad
            df = pd.DataFrame({
                "nombre": [nombre],
                "sintomas_generales": [sintomas_generales],
            })

            # Usar el modelo de RandomForest (preentrenado)
            le = LabelEncoder()
            model = RandomForestClassifier(n_estimators=100)
            model.fit(df, [0])  # Ejemplo con un dummy train

            # Realizamos la predicción
            prediction = model.predict(df)
            enfermedad_predicha = le.inverse_transform(prediction)[0]

            # Retornamos los resultados
            return render(request, 'resultados.html', {'enfermedad': enfermedad_predicha})
    else:
        form = DiagnosticoForm()

    return render(request, 'formulario.html', {'form': form})
import pickle

# Cargar modelo entrenado
with open('ruta_al_modelo/modelo_entrenado.pkl', 'rb') as f:
    model = pickle.load(f)

# Cargar label encoder
with open('ruta_al_modelo/le_enfermedad.pkl', 'rb') as f:
    le_enfermedad = pickle.load(f)
