from django.db import models
from django.contrib.auth.models import User

# Métodos e Choices


def user_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'usuario_{0}/{1}'.format(instance.user.id, filename)


# Classes (modelos)

class Autor(models.Model):
    nome = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    def __str__(self):
        return "{}".format(self.nome)


class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=50)

    def __str__(self):
        return "{}".format(self.nome)


class Ingrediente(models.Model):
    nome = models.CharField(max_length=50)
    qtde = models.FloatField()
    unidade_medida = models.CharField(max_length=15)

    def __str__(self):
        return "{} ({} {})".format(self.nome, self.qtde, self.unidade_medida)


class Comentario(models.Model):
    texto = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(Autor, on_delete=models.PROTECT)

    def __str__(self):
        return "Comentário por {} em {}".format(self.autor.nome, self.data_criacao)


class Avaliacao(models.Model):
    nota = models.IntegerField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(
        Autor, on_delete=models.PROTECT, verbose_name="autor")

    def __str__(self):
        return "Avaliação {} por {} em {}".format(self.nota, self.autor.nome, self.data_criacao)


class Receita(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField()
    modo_preparo = models.TextField()

    autor = models.ForeignKey(Autor, on_delete=models.PROTECT)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    ingredientes = models.ManyToManyField(Ingrediente)

    def __str__(self):
        return "{} por {} em {}".format(self.nome, self.autor.nome, self.categoria.nome)
