from django.shortcuts import render

from django.views.generic.base import TemplateView

# Create your views here.

class MapLocationsView(TemplateView):

    template_name = "map.html"