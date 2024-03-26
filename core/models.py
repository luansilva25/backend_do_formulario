from django.db import models
from django.contrib.auth.models import User

class Estados(models.Model):
    ESTADOS = [
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceara'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espirito Santo'),
        ('GO', 'Goiás'),
        ('MT', 'Mato Grosso'),
        ('MA', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraiba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piaui'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondonia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins')
    ]
    
    estado = models.CharField(max_length=30, choices=ESTADOS)

    def __str__(self):
        return self.estado

class Hobbies(models.Model):
    HOBBIES = [
        ('praticar esportes', 'Praticar esportes'),
        ('desenhar/pintar', 'Desenhar/Pintar'),
        ('dançar', 'Dançar'),
        ('conversar', 'Conversar'),
        ('Meditar', 'Meditar'),
        ('jogar jogos', 'Jogar jogos'),
        ('ouvir musica', 'Ouvir musica'),
        ('outros', 'Outros')
    ]

    hobbies = models.CharField(max_length= 25, choices=HOBBIES)

    def __str__(self):
        return self.hobbies

class Linguagens(models.Model):
    PROGRAM_LANGUAGES = [
        ('cpp', 'C++'),
        ('csharp', 'C#'),
        ('Java', 'java'),
        ('javascript', 'JavaScript'),
        ('python', 'Python'),
        ('ruby', 'Ruby'),
        ('php', 'PHP'),
        ('Outros', 'Outros')
    ]

    linguagens = models.CharField(max_length=25,choices=PROGRAM_LANGUAGES)
    
    def __str__(self):
        return self.linguagens


class Formulario(models.Model):
    nome = models.CharField(max_length=25)
    email = models.CharField(max_length = 100)
    senha = models.CharField(max_length=25)
    nascimento = models.DateField()
    endereco = models.CharField(max_length=50)
    cidade = models.CharField(max_length= 50)
    estado = models.ForeignKey(Estados, on_delete=models.CASCADE)
    hobby = models.ManyToManyField(Hobbies)
    linguagem = models.ManyToManyField(Linguagens)
    biografia = models.CharField(max_length=1000)

    def __str__(self):
        return self.nome
    