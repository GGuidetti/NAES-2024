from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Autor, Categoria, Ingrediente, Receita, Comentario, Avaliacao

from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin

from django.shortcuts import get_object_or_404

# ################# CREATE #################

class AutorCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Autor
    fields = ['nome', 'email']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-autor')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastro de Autor"
        context['botao'] = "Cadastrar"
        return context


class CategoriaCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Categoria
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-categoria')


class IngredienteCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Ingrediente
    fields = ['nome', 'qtde', 'unidade_medida']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-ingrediente')


class ReceitaCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Receita
    fields = ['nome', 'descricao', 'modo_preparo', 'autor', 'categoria']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-receita')


class ComentarioCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Comentario
    fields = ['texto', 'autor']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-comentario')


class AvaliacaoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Avaliacao
    fields = ['nota', 'autor']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-avaliacao')


# ################# UPDATE #################

class AutorUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Autor
    fields = ['nome', 'email']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-autor')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Editar Autor"
        context['botao'] = "Salvar"
        return context


class CategoriaUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Categoria
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-categoria')


class IngredienteUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Ingrediente
    fields = ['nome', 'qtde', 'unidade_medida']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-ingrediente')


class ReceitaUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Receita
    fields = ['nome', 'descricao', 'modo_preparo', 'autor', 'categoria']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-receita')


class ComentarioUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Comentario
    fields = ['texto', 'autor', 'receita']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-comentario')


class AvaliacaoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Avaliacao
    fields = ['nota', 'autor', 'receita']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-avaliacao')


# ################# DELETE #################

class AutorDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Autor
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-autor')


class CategoriaDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Categoria
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-categoria')


class IngredienteDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Ingrediente
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-ingrediente')


class ReceitaDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Receita
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-receita')


class ComentarioDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Comentario
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-comentario')


class AvaliacaoDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Avaliacao
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-avaliacao')


# ################# LIST #################

class AutorList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Autor
    template_name = 'cadastros/listas/autor.html'


class CategoriaList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Categoria
    template_name = 'cadastros/listas/categoria.html'


class IngredienteList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Ingrediente
    template_name = 'cadastros/listas/ingrediente.html'


class ReceitaList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Receita
    template_name = 'cadastros/listas/receita.html'


class ComentarioList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Comentario
    template_name = 'cadastros/listas/comentario.html'


class AvaliacaoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Avaliacao
    template_name = 'cadastros/listas/avaliacao.html'
