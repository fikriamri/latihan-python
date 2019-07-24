from django.db import models

# Create your models here.
class Binatang(models.Model):
    nama = models.CharField(max_length=255)
    umur = models.CharField(max_length=5)

    def __str__(self):
        return self.nama