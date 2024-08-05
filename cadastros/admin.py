from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Autor, Categoria, Ingrediente, Receita, Comentario, Avaliacao

admin.site.register(Autor)
admin.site.register(Categoria)
admin.site.register(Ingrediente)
admin.site.register(Comentario)
admin.site.register(Avaliacao)

class ReceitaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'autor', 'categoria')
    search_fields = ('nome', 'autor__nome', 'categoria__nome')
    list_filter = ('categoria', 'autor')
    filter_horizontal = ('ingredientes',)  # Usado para campos ManyToMany

admin.site.register(Receita, ReceitaAdmin)
