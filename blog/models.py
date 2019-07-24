from django.db import models
from django.db.models import CharField
from django.db.models import TextField
from datetime import date
from django.utils import timezone

# Create your models here.
class Blog(models.Model):
    judul = models.CharField(max_length=255)
    isi = models.TextField(max_length=2000)
    pic = models.CharField(max_length=255)
    tanggal_pembuatan = models.DateField(auto_now=True)
    comment = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.judul

class Mentee(models.Model):
    nama = models.CharField(max_length=255)
    quotes = models.TextField(max_length=255)
    pic = models.CharField(max_length=255)

    def __str__(self):
        return self.nama

class Mentor(models.Model):
    nama = models.CharField(max_length=255)
    experience = models.PositiveIntegerField(default=0, verbose_name='Experience (in years)')
    julukan = models.CharField(max_length=255)
    quotes = models.TextField(max_length=255)
    pic = models.CharField(max_length=255)

    def __str__(self):
        return self.nama