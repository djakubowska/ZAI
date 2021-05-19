from rest_framework import serializers
from .models import Kategorie, Dania

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
    Danie_Kategoria = serializers.SlugRelatedField(queryset=Kategorie.objects.all(), slug_field='Nazwa')
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Dania
        fields = ['Danie_id', 'url', 'Opis', 'Cena', 'Danie_Kategoria', 'owner']



