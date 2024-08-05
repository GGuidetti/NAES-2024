from django.urls import path

# Importa as views que criamos
from .views import (
    AutorCreate, CategoriaCreate, IngredienteCreate, ReceitaCreate, ComentarioCreate, AvaliacaoCreate,
    AutorUpdate, CategoriaUpdate, IngredienteUpdate, ReceitaUpdate, ComentarioUpdate, AvaliacaoUpdate,
    AutorDelete, CategoriaDelete, IngredienteDelete, ReceitaDelete, ComentarioDelete, AvaliacaoDelete,
    AutorList, CategoriaList, IngredienteList, ReceitaList, ComentarioList, AvaliacaoList
)

# Padrão de URLs
urlpatterns = [
    # Rotas para criar registros
    path('cadastrar/autor/', AutorCreate.as_view(), name="cadastrar-autor"),
    path('cadastrar/categoria/', CategoriaCreate.as_view(), name="cadastrar-categoria"),
    path('cadastrar/ingrediente/', IngredienteCreate.as_view(), name="cadastrar-ingrediente"),
    path('cadastrar/receita/', ReceitaCreate.as_view(), name="cadastrar-receita"),
    path('cadastrar/comentario/', ComentarioCreate.as_view(), name="cadastrar-comentario"),
    path('cadastrar/avaliacao/', AvaliacaoCreate.as_view(), name="cadastrar-avaliacao"),

    # Rotas para atualizar registros
    path('editar/autor/<int:pk>/', AutorUpdate.as_view(), name="editar-autor"),
    path('editar/categoria/<int:pk>/', CategoriaUpdate.as_view(), name="editar-categoria"),
    path('editar/ingrediente/<int:pk>/', IngredienteUpdate.as_view(), name="editar-ingrediente"),
    path('editar/receita/<int:pk>/', ReceitaUpdate.as_view(), name="editar-receita"),
    path('editar/comentario/<int:pk>/', ComentarioUpdate.as_view(), name="editar-comentario"),
    path('editar/avaliacao/<int:pk>/', AvaliacaoUpdate.as_view(), name="editar-avaliacao"),

    # Rotas para excluir registros
    path('excluir/autor/<int:pk>/', AutorDelete.as_view(), name="excluir-autor"),
    path('excluir/categoria/<int:pk>/', CategoriaDelete.as_view(), name="excluir-categoria"),
    path('excluir/ingrediente/<int:pk>/', IngredienteDelete.as_view(), name="excluir-ingrediente"),
    path('excluir/receita/<int:pk>/', ReceitaDelete.as_view(), name="excluir-receita"),
    path('excluir/comentario/<int:pk>/', ComentarioDelete.as_view(), name="excluir-comentario"),
    path('excluir/avaliacao/<int:pk>/', AvaliacaoDelete.as_view(), name="excluir-avaliacao"),

    # Rotas para listar registros
    path('listar/autores/', AutorList.as_view(), name="listar-autor"),
    path('listar/categorias/', CategoriaList.as_view(), name="listar-categoria"),
    path('listar/ingredientes/', IngredienteList.as_view(), name="listar-ingrediente"),
    path('listar/receitas/', ReceitaList.as_view(), name="listar-receita"),
    path('listar/comentarios/', ComentarioList.as_view(), name="listar-comentario"),
    path('listar/avaliacoes/', AvaliacaoList.as_view(), name="listar-avaliacao"),
]
