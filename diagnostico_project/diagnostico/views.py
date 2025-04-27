from django.shortcuts import render
from .forms import DiagnosticoForm
from .models import Diagnostico
import pandas as pd
import pickle
from datetime import date

# Cargar modelo y label encoder
model = pickle.load(open('diagnostico/static/modelo_entrenado.pkl', 'rb'))
le_enfermedad = pickle.load(open('diagnostico/static/le_enfermedad.pkl', 'rb'))

def calcular_edad(fecha_nacimiento):
    today = date.today()
    edad = today.year - fecha_nacimiento.year - ((today.month, today.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    return edad

def formulario(request):
    if request.method == 'POST':
        form = DiagnosticoForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            tipo_documento = form.cleaned_data['tipo_documento']
            numero_documento = form.cleaned_data['numero_documento']
            fecha_nacimiento = form.cleaned_data['fecha_nacimiento']
            peso = form.cleaned_data['peso']
            fuma = form.cleaned_data['fuma']
            sexo = form.cleaned_data['sexo']
            estatura = form.cleaned_data['estatura']
            antecedentes_medicos = form.cleaned_data['antecedentes_medicos']
            sintomas_generales = form.cleaned_data['sintomas_generales']

            edad = calcular_edad(fecha_nacimiento)

            # Codificar para el modelo
            fuma_modelo = 1 if fuma == 'si' else 0
            sexo_modelo = 1 if sexo == 'masculino' else 0

            df_usuario = pd.DataFrame({
                'fuma': [fuma_modelo],
                'sexo': [sexo_modelo],
                'peso': [peso],
                'estatura': [estatura],
                'edad': [edad]
            })

            prediccion = model.predict(df_usuario)
            enfermedad = le_enfermedad.inverse_transform(prediccion)[0]

            # Guardar en la base de datos
            Diagnostico.objects.create(
                nombre=nombre,
                apellido=apellido,
                tipo_documento=tipo_documento,
                numero_documento=numero_documento,
                fecha_nacimiento=fecha_nacimiento,
                peso=peso,
                fuma=fuma,
                sexo=sexo,
                estatura=estatura,
                antecedentes_medicos=antecedentes_medicos,
                sintomas_generales=sintomas_generales,
                enfermedad_predicha=enfermedad
            )

            contexto = {
                'nombre': nombre,
                'apellido': apellido,
                'tipo_documento': tipo_documento,
                'numero_documento': numero_documento,
                'edad': edad,
                'peso': peso,
                'sexo': 'Masculino' if sexo_modelo == 1 else 'Femenino',
                'fuma': 'Sí' if fuma_modelo == 1 else 'No',
                'estatura': estatura,
                'antecedentes_medicos': antecedentes_medicos,
                'sintomas_generales': sintomas_generales,
                'enfermedad': enfermedad
            }

            return render(request, 'diagnostico/resultados.html', contexto)
    else:
        form = DiagnosticoForm()
    return render(request, 'diagnostico/formulario.html', {'form': form})


from .models import Diagnostico

def lista_diagnosticos(request):
    diagnosticos = Diagnostico.objects.all().order_by('-fecha_diagnostico')  # Últimos primero
    return render(request, 'diagnostico/lista_diagnosticos.html', {'diagnosticos': diagnosticos})


