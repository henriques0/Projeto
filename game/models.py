from django.db import models

# Create your models here.

class Estado(models.Model):
    sigla       = models.CharField(max_length=2)
    nome        = models.CharField(max_length=50, unique=True)

    #Like "ToString" self == this
    def __str__(self):
        return self.sigla + ' - ' + self.nome


class Cidade(models.Model):
    nome        = models.CharField(max_length=50)
    estado      = models.ForeignKey(Estado, on_delete=models.PROTECT)
    descricao   = models.TextField(blank=True, null=True, verbose_name="Descrição", help_text="Informações relevantes")

    def __str__(self):
        return self.nome + ' - ' + self.estado.sigla

class Pessoa(models.Model):
    nome        = models.CharField(max_length=50, verbose_name="Digite seu nome")
    idade       = models.IntegerField(max_length=3)
    celular     = models.IntegerField(max_length=13, verbose_name="Digie o seu numero de telefone celular")
    nascimento  = models.DateField(verbose_name="Sua data de Nascimento")
    email       = models.EmailField(max_length=100)
    Cidade      = models.ForeignKey(Cidade, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome + ' - ' + str(self.nascimento)

class Plataforma(models.Model):
    nome        = models.CharField(max_length=50, verbose_name="Digite seu nome")
    marca       = models.CharField(max_length=50, verbose_name="Digite a marca")
    descricao   = models.CharField(max_length=50, verbose_name="Digite a descrição da plataforma")


class Jogo(models.Model):
    nome        = models.CharField(max_length=50, verbose_name="Digite o nome do jogo")
    descricao   = models.CharField(max_length=50, verbose_name="Digite uma breve descrição")
    Plataforma  = models.ForeignKey(Plataforma, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome + ' - ' + self.Plataforma.nome

    
class Login(models.Model):
    usuario       = models.CharField(max_length=2)
    senha        = models.CharField(max_length=50, unique=True)

    #Like "ToString" self == this
    def __str__(self):
        return self.senha + ' - ' + self.usuario