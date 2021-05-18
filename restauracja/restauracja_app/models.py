from django.db import models

class Kategorie(models.Model):
    Kategorie_id = models.IntegerField(primary_key=True, unique=True)
    Nazwa = models.CharField(max_length=50)
    Opis = models.CharField(max_length=100)

    class Meta:
       ordering = ('Kategorie_id',)

    def __str__(self):
        return self.Nazwa

class Dania(models.Model):
    Danie_id = models.IntegerField(primary_key=True, unique=True)
    Cena = models.IntegerField()
    Kategorie_id = models.IntegerField()
    Opis = models.CharField(max_length=100)
    Danie_Kategoria = models.ForeignKey(Kategorie, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ('Danie_id',)

    def __str__(self):
        return self.Opis
# Create your models here.
