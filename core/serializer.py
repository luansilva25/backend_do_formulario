from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Formulario, Estados, Hobbies, Linguagens
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class FormSerializer(ModelSerializer):
    linguagem = serializers.SlugRelatedField(many=True, slug_field='linguagens', queryset=Linguagens.objects.all())
    hobby = serializers.SlugRelatedField(many=True, slug_field='hobbies', queryset=Hobbies.objects.all())
    estado = serializers.SlugRelatedField(many=False, slug_field='estado', queryset=Estados.objects.all())

    class Meta:
        model = Formulario
        fields = '__all__'

class EstadoSerializer(ModelSerializer):
    class Meta: 
        model = Estados
        fields = '__all__'

class HobbySerializer(ModelSerializer):
    class Meta: 
        model = Hobbies
        fields = '__all__'

class LinguagemSerializer(ModelSerializer):
    class Meta:
        model = Linguagens
        fields = '__all__'
