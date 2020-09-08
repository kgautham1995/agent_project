from django.db import models

# Create your models here.

class agent_model(models.Model):
    idno = models.IntegerField(unique=True)
    name = models.CharField(max_length=50)
    add = models.TextField()
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    state = models.CharField(max_length=50)