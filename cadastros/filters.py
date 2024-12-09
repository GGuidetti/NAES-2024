from django_filters import FilterSet
from .models import Categoria
from .models import Autor

class CategoriaFilter(FilterSet):
    class Meta:
        model = Categoria
        fields = {
            'nome': ['icontains'],
            'descricao': ['icontains']
        }
        

class AutorFilter(FilterSet):
    class Meta:
        model = Autor
        fields = {
            'nome': ['icontains'],
            'email': ['icontains']
        }
