
from django.views.generic import TemplateView

class PaginaInicial(TemplateView):
    template_name = 'paginas/index2.html'
 
class SobreView(TemplateView):
    template_name = 'paginas/sobre.html'