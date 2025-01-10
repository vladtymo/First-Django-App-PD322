from django.db import models



# Create your models here.
class User(models.Model):
    ROLE_CHOICES = [
        (0, 'Admin'),
        (1, 'User'),
        (2, 'Manager'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    avatar = models.ImageField(blank=True, null=True, upload_to="avatars/")
    role = models.IntegerField(choices=ROLE_CHOICES, default=0)

    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField( 
        max_length = 40, 
        choices = User.ROLE_CHOICES, 
        default = 0) 

    def __str__(self):
        return self.name
