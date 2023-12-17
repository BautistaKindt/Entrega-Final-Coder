from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class Usuario(models.Model):
    username = models.CharField(max_length=30, unique=True)
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    pasword = models.CharField(max_length=30)
    avatar = models.ImageField()
    def __str__(self):
        return f"Hola {self.username}"

def get_image_filename(instance, filename):
    title =  'titulo'
    slug = slugify(title)
    return "imagenesAvatares/%s-%s" % (slug, filename)


class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)

    def __str__(self):
        return f"Imagen de: {self.user.username}"