from django.db import models 

class Tarea(models.Model):
    nombre = models.TextField(max_length=100)
    estado = models.TextField(max_length=100,default="por_hacer")
    creado_el = models.DateTimeField(auto_now_add=True)
    modificado_el = models.DateTimeField(auto_now=True)

    def terminar(self):
        self.estado = "terminado"


    def __str__(self):
        return f"{self.id} - {self.nombre}"


class Persona(models.Model):
    nombre = models.TextField(max_length=100)
    apellido = models.TextField(max_length=100)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return f"{self.id} - Nombre: {self.nombre} - Apellido: {self.apellido}"
    

class Mascota(models.Model):
    especie=models.CharField(max_length=20)
    raza=models.CharField(max_length=20,default="Desconocida")
    nombre=models.CharField(max_length=20, default="No tiene")
    nombre_duenio=models.CharField(max_length=20, default="No tiene")
    tel_duenio=models.CharField(max_length=30)

    def __str__(self):
        return f"Id: {self.id} - Especie: {self.especie} - Raza: {self.raza} - Tel Dueño: {self.tel_duenio}"

