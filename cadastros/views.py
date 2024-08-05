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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Cadastro de Autor"
        return context


class CategoriaCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Categoria
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-categoria')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Cadastro de Categoria"
        return context


class IngredienteCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Ingrediente
    fields = ['nome', 'qtde', 'unidade_medida']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-ingrediente')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Cadastro de Ingrediente"
        return context


class ReceitaCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Receita
    fields = ['nome', 'descricao', 'modo_preparo', 'autor', 'categoria']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-receita')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Cadastro de Receita"
        return context


class ComentarioCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Comentario
    fields = ['texto', 'autor']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-comentario')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Cadastro de Comentário"
        return context


class AvaliacaoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Avaliacao
    fields = ['nota', 'autor']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-avaliacao')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Cadastro de Avaliação"
        return context


# ################# UPDATE #################

# ################# UPDATE #################

class AutorUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Autor
    fields = ['nome', 'email']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-autor')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Editar Autor"
        context['botao'] = "Salvar"
        return context


class CategoriaUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Categoria
    fields = ['nome', 'descricao']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-categoria')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Editar Categoria"
        context['botao'] = "Salvar"
        return context


class IngredienteUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Ingrediente
    fields = ['nome', 'qtde', 'unidade_medida']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-ingrediente')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Editar Ingrediente"
        context['botao'] = "Salvar"
        return context


class ReceitaUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Receita
    fields = ['nome', 'descricao', 'modo_preparo', 'autor', 'categoria']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-receita')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Editar Receita"
        context['botao'] = "Salvar"
        return context


class ComentarioUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Comentario
    fields = ['texto', 'autor']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-comentario')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Editar Comentário"
        context['botao'] = "Salvar"
        return context


class AvaliacaoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Avaliacao
    fields = ['nota', 'autor']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-avaliacao')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Editar Avaliação"
        context['botao'] = "Salvar"
        return context


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
