from rest_framework import serializers
from .models import Kategorie, Dania, Zamowienia, Platnosc, Stolik_Klient

#class KategorieSerializer(serializers.Serializer):
    #Kategorie_id = serializers.IntegerField(required=True)
    #Nazwa = serializers.CharField(required=True,max_length=50)
    #Opis = serializers.CharField(max_length=100)

    #def create(self, validated_data):
    #    return Kategorie.objects.create(**validated_data)

    #def update(self, instance, validated_data):
    #    instance.nazwa = validated_data.get('nazwa', instance.nazwa)
    #    instance.save()
    #    return instance

    #def validate_nazwa(self,value):
    #    if '' in value:
    #        raise serializers.validationError('Nie wolno spacji')
    #    return value

class KategorieSerializer(serializers.HyperlinkedModelSerializer):
    dania = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='dania-detail')
    class Meta:
        model = Kategorie
        fields = ['Kategorie_id', 'url', 'Nazwa', 'dania']


class DaniaSerializer(serializers.HyperlinkedModelSerializer):
    Kategorie_id = serializers.SlugRelatedField(queryset=Kategorie.objects.all(), slug_field='Nazwa')
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Dania
        fields = ['Danie_id', 'url', 'Opis', 'Cena', 'Kategorie_id', 'owner']


class ZamowieniaSerializer(serializers.HyperlinkedModelSerializer):
    Danie_id = serializers.SlugRelatedField(queryset=Dania.objects.all(), slug_field='Opis')
    Platnosc_id = serializers.SlugRelatedField(queryset=Platnosc.objects.all(), slug_field='Platnosc_id')
    Stolik_Klient_id = serializers.SlugRelatedField(queryset=Stolik_Klient.objects.all(), slug_field='Stolik_Klient_id')
    class Meta:
        model = Zamowienia
        fields = ['Zamowienie_id', 'Platnosc_id', 'Stolik_Klient_id','Danie_id', 'Ilosc', 'Uwagi', 'Status_zamowienia','Wartosc']

class PlatnoscSerializer(serializers.HyperlinkedModelSerializer):
    platnosc = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='zamowienie-detail')
    class Meta:
        model = Platnosc
        fields = ['Platnosc_id', 'Status_platnosc','Opis', 'url', 'platnosc']

class StolikKlientSerializer(serializers.HyperlinkedModelSerializer):
    stolikklient = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='zamowienie-detail')
    class Meta:
        model = Stolik_Klient
        fields = ['Stolik_Klient_id', 'Ilosc_osob','Status_zamowienia', 'url', 'stolikklient']




