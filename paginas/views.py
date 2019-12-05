from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

class TrabalhoPageView(TemplateView):
    template_name = 'trabalho.html'

class ONGsDeAnimaisPageView(TemplateView):
    template_name = 'ONGsDeAnimais.html'

class ONGsDeAnimaisPedroIIView(TemplateView):
    template_name = 'ONGsDeAnimaisPedroII-PI.html'

class VoluntariadoView(TemplateView):
    template_name = 'Voluntariado.html'

class ListadeEventosView(TemplateView):
    template_name = 'ListadeEventos.html'

class oqEView(TemplateView):
    template_name = 'oqE.html'