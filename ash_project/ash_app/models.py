from django.db import models

# Create your models here.
class UserPhoto(models.Model):
    user_pic=models.ImageField(upload_to='picture',blank=False)
