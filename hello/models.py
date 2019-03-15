from django.db import models

# Create your models here.
class Greeting(models.Model):
    noun = models.TextField("greeting noun", default='Stranger')
    when = models.DateTimeField("date created", auto_now_add=True)
