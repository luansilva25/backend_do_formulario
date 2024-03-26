from ..serializer import FormSerializer, HobbySerializer, EstadoSerializer, LinguagemSerializer
from ..models import Formulario, Hobbies, Estados, Linguagens
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User


class FormViewSet(ModelViewSet):
    queryset = Formulario.objects.all()
    serializer_class = FormSerializer

class HobbyViewSet(ModelViewSet):
    queryset = Hobbies.objects.all()
    serializer_class = HobbySerializer

class EstadoViewSet(ModelViewSet):
    queryset = Estados.objects.all()
    serializer_class = EstadoSerializer

class LinguagemViewSet(ModelViewSet):
    queryset = Linguagens.objects.all()
    serializer_class = LinguagemSerializer

class GetFormViewSet(ModelViewSet):
    def get_queryset(self):
        nome = self.request.GET.get('nome')
        return Formulario.objects.filter(nome=nome)
    serializer_class = FormSerializer


    