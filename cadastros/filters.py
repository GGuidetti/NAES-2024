from django_filters import FilterSet
from .models import Categoria

class CategoriaFilter(FilterSet):
    class Meta:
        model = Categoria
        fields = {
            'nome': ['icontains'],
            'descricao': ['icontains']
        }