from django.urls import path, include


from .views import PaginaInicial, SobreView

urlpatterns = [
    path('', PaginaInicial.as_view(), name='index'),
    path('sobre/', SobreView.as_view(), name='sobre'),
    path('', include('cadastros.urls')),
    path('usuarios/', include('usuarios.urls')), 
]