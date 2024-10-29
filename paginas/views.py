
from django.views.generic import TemplateView
import random
from cadastros.models import Receita

class PaginaInicial(TemplateView):
    template_name = 'paginas/index2.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Página Inicial"
        context['qtdeReceitas'] = Receita.objects.count()
      
        receitas = list(Receita.objects.order_by('nome'))
        if receitas:
            numero_receitas = min(3, len(receitas))
            context['receitassAleatorias'] = random.sample(
                receitas, numero_receitas)
        else:
            context['receitassAleatorias'] = []

        print(context['receitassAleatorias'])

        return context
 
class SobreView(TemplateView):
    template_name = 'paginas/sobre.html'