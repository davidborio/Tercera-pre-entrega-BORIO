from django import forms

class PersonaForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    fecha_nacimiento = forms.DateField()

class BuscarPersonasForm(forms.Form):
    criterio_nombre = forms.CharField(max_length=100)


class MascotaForm(forms.Form):
    especie=forms.CharField(max_length=20)
    nombre=forms.CharField(max_length=20)
    raza=forms.CharField(max_length=20)
    nombre_duenio=forms.CharField(max_length=20)
    tel_duenio=forms.CharField(max_length=30)
    
    
class BuscarMascotasForm(forms.Form):
    criterio_especie = forms.CharField(max_length=20)


