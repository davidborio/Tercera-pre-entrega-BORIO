from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Tarea,Persona,Mascota
from AppCoder.forms import PersonaForm, MascotaForm, TareaForm
from django.views.generic import ListView
from AppCoder.forms import BuscarPersonasForm, BuscarMascotasForm, BuscarTareaForm
    
def crear_tarea(request):
     form=TareaForm(request.POST)
     context = {
        "form":form
        } 
     if form.is_valid():
          nueva_tarea=form.save()
          form=TareaForm()

     context["tareas"] = Tarea.objects.all()
     context["total_tareas"] = len(Tarea.objects.all()) 
    
     return render(request, "AppCoder/tareas.html",context)

class BuscarTarea(ListView):
    model = Tarea
    context_object_name = "tareas"

    def get_queryset(self):
        f = BuscarTareaForm(self.request.GET)
        if f.is_valid():
                return Tarea.objects.filter(nombre__icontains= f.data["criterio_nombre"]).all() #__icontains filtra todas las palabras que contengan la cadena ingresada en nombre

        return Tarea.objects.none()


def mostrar_mis_tareas(request):
    tareas = Tarea.objects.all()

    return render(request, "AppCoder/tareas.html", {"tareas": tareas})

def crear_persona(request):
    f = PersonaForm(request.POST)
    context = {
        "form":f
        } #crea un contexto con un dicc con los datos del form vacios
        

    if f.is_valid():
        Persona(nombre= f.data["nombre"],
        apellido= f.data["apellido"],
        fecha_nacimiento= f.data["fecha_nacimiento"]).save() #Carga los datos inggresados y guarda en la BD. La persona ya está creada
        context['form'] = PersonaForm()  #Para que limpie los campos del form al ingresar datos correctos

    context["personas"] = Persona.objects.all()
    context["total_personas"] = len(Persona.objects.all()) #Agrega claves al dicc context para pasar al template

    return render(request,"AppCoder/personas.html",context)


def mostrar_personas(request):

    personas = Persona.objects.all()
    total_personas = len(personas)
    context= {"personas": personas, 
    "total_personas":total_personas,
    "form":PersonaForm()}

    return render(request, "AppCoder/personas.html",context)

def crear_mascota(request):
    f = MascotaForm(request.POST)
    context = {
        "form":f
        } #crea un contexto con un dicc con los datos del form vacios
        

    if f.is_valid():
        Mascota(especie= f.data["especie"],raza=f.data["raza"],
        nombre= f.data["nombre"],
        nombre_duenio= f.data["nombre_duenio"],
        tel_duenio=f.data["tel_duenio"]).save() #Carga los datos inggresados y guarda en la BD. La persona ya está creada
        context['form'] = MascotaForm()  #Para que limpie los campos del form al ingresar datos correctos

    context["mascotas"] = Mascota.objects.all()
    context["total_mascotas"] = len(Mascota.objects.all()) #Agrega claves al dicc context para pasar al template

    return render(request,"AppCoder/mascotas.html",context)
    

def mostrar_mascotas(request):
    mascotas = Mascota.objects.all()
    total_mascotas = len(mascotas)

    return render(request, "AppCoder/mascotas.html", 
    {"mascotas":mascotas,
    "total_mascotas":total_mascotas,
    "form":MascotaForm()
    })

class BuscarPersonas(ListView):
    model = Persona
    context_object_name = "personas"

    def get_queryset(self):
        f = BuscarPersonasForm(self.request.GET)
        if f.is_valid():
                return Persona.objects.filter(nombre__icontains= f.data["criterio_nombre"]).all() #__icontains filtra todas las palabras que contengan la cadena ingresada en nombre

        return Persona.objects.none() #si no se encontró
    
class BuscarMascotas(ListView):
    model = Mascota
    context_object_name = "mascotas"

    def get_queryset(self):
        f = BuscarMascotasForm(self.request.GET)
        if f.is_valid():                
                return Mascota.objects.filter(nombre__icontains= f.data["criterio_especie"]).all() #__icontains filtra todas las palabras que contengan la cadena ingresada en nombre

        return Mascota.objects.none() #si no se encontró







# Create your views here.




