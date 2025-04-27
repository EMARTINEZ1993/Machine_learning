from django import forms

class DiagnosticoForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    tipo_documento = forms.ChoiceField(choices=[('CC', 'Cédula de Ciudadanía'), ('TI', 'Tarjeta de Identidad'), ('CE', 'Cédula de Extranjería')])
    numero_documento = forms.CharField(max_length=20)
    fecha_nacimiento = forms.DateField()
    peso = forms.IntegerField()
    fuma = forms.ChoiceField(choices=[('si', 'Sí'), ('no', 'No')])
    sexo = forms.ChoiceField(choices=[('masculino', 'Masculino'), ('femenino', 'Femenino')])
    estatura = forms.IntegerField()
    antecedentes_medicos = forms.CharField(widget=forms.Textarea)
    sintomas_generales = forms.CharField(widget=forms.Textarea)

