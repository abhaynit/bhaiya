from django.db import models

# Create your models here.
class addimg(models.Model):
    im = models.ImageField(upload_to = "media")

