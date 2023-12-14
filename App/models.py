from django.db import models

# Create your models here.

class Atm(models.Model):
    Name = models.CharField(max_length=200)
    Card_Number = models.CharField(max_length=200)
    Pin = models.CharField(max_length=20)
    Balance = models.BigIntegerField(null=True)
    class Meta:
        db_table = 'ATM'
