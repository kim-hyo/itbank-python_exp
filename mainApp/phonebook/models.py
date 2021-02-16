from django.db import models

# Create your models here.
class phonebooks(models.Model):
    name = models.CharField(max_length=50, null=False)
    pnum = models.CharField(max_length=20)
    email = models.EmailField()
    addr = models.CharField(max_length=100)
    birth = models.DateField()

