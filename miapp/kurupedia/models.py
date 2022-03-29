from django.db import models
from django.contrib.auth.models import User
#django crea por defecto los usuarios en la tabla auth_user
from django.utils import timezone
from django.db.models.signals import post_save
# Create your models here.
#dentro del archivo de models se crea una clase para
#cada tabla de base de datos
#para actualizar la base de datos hay que ejecutar "migrate"
class Usuario(models.Model):
     #nombre=models.CharField(max_length=30)
     #email=models.EmailField()
     #telefono=models.CharField(max_length=30,blank=True,null=True)  #esto permite hacer opcional el dejar en blanco el telefono
     #otro campo puede ser direccion y telefono
     user=models.OneToOneField(User, on_delete=models.CASCADE)
     image=models.ImageField(default='tony_tony_chopper.jpg')

     def __str__(self):
         return f'Perfil de {self.user.username}'

class Posteo(models.Model):
    #nombre=models.CharField(max_length=20)
    #creador=models.CharField(max_length=30)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='posts')
    timestamp=models.DateTimeField(default=timezone.now)
    content=models.TextField()

    class Meta:   #esto indica como se va a comportar una clase
        ordering=['-timestamp']

    def __str__(self):
        return f'{self.user.username}:{self.content}'

class Comentario(models.Model):
    fecha=models.DateField()
    numero=models.IntegerField()
    creador=creador=models.CharField(max_length=30)

#para borrar un elemento d una clase se borra
#con la siguiente manera:
#1-creamos una variable que guarde el objeto
#variable='objeto'.objects.get(id=nro de id)
# para borrar hacemos
#variable.delete()
