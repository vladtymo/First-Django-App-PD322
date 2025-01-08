from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    avatar = models.ImageField(blank=True, null=True, upload_to="avatars/")

    def __str__(self):
        return self.name
