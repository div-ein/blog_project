from django.db import models

# Create your models here.
class Tisto(models.Model):
  jemok = models.CharField(max_length=100)
  sigan = models.DateTimeField('date published')
  naeyong = models.TextField()