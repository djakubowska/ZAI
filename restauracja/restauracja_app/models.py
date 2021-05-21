from django.db import models

class Kategorie(models.Model):
    Kategorie_id = models.AutoField(primary_key=True, unique=True)
    Nazwa = models.CharField(max_length=50)
    Opis = models.CharField(max_length=100)

    class Meta:
       ordering = ('Kategorie_id',)

    def __str__(self):
        return self.Nazwa

class Dania(models.Model):
    Danie_id = models.AutoField(primary_key=True, unique=True)
    Cena = models.IntegerField()
    Opis = models.CharField(max_length=100)
    Kategorie_id = models.ForeignKey(Kategorie, related_name='dania', on_delete=models.SET_NULL, null=True)
    owner = models.ForeignKey('auth.User', related_name ='dania', on_delete=models.CASCADE)

    class Meta:
        ordering = ('Danie_id',)

    def __str__(self):
        return self.Opis

ZamowienieStatus = (

                       ('PRZ', 'PRZYJETE'),
                       ('ZRE', 'ZREALIZOWANE'),
                       ('OPL', 'OPLACONE')
)

PlatnoscStatus = (

    ('WPR', 'WPROWADZONA'),
    ('ZAK', 'ZAKSIEGOWANA')
)

class Platnosc(models.Model):
    Platnosc_id = models.AutoField(primary_key=True, unique=True)
    Status_platnosc = models.CharField(max_length=100, choices=PlatnoscStatus)
    Opis = models.CharField(max_length=100)

    class Meta:
        ordering = ('Platnosc_id',)

    def __str__(self):
        return str(self.Platnosc_id) + ' ' + self.Status_platnosc


class Stolik_Klient(models.Model):
    Stolik_Klient_id = models.AutoField(primary_key=True, unique=True)
    Ilosc_osob = models.IntegerField()
    Status_zamowienia = models.CharField(max_length=100, choices=ZamowienieStatus)

    class Meta:
        ordering = ('Stolik_Klient_id',)

    def __str__(self):
        return str(self.Stolik_Klient_id)

class Zamowienia(models.Model):
    Zamowienie_id = models.AutoField(primary_key=True, unique=True)
    Danie_id = models.ForeignKey(Dania, related_name='dania', on_delete=models.SET_NULL, null=True)
    Stolik_Klient_id = models.ForeignKey(Stolik_Klient, related_name='stolikklient', on_delete=models.SET_NULL, null=True)
    Platnosc_id = models.ForeignKey(Platnosc, related_name='platnosc', on_delete=models.SET_NULL, null=True)
    Ilosc = models.IntegerField()
    Uwagi = models.CharField(max_length=100)
    Status_zamowienia = models.CharField(max_length=100, choices=ZamowienieStatus)
    Wartosc = models.IntegerField()

    class Meta:
        ordering = ('Zamowienie_id',)

    def __str__(self):
        return self.Uwagi



# Create your models here.
