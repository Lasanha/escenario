from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from django.views.generic import TemplateView
from django.template import RequestContext

class Home(View):
    template_name = 'home.html'

    def get(self, request):
        return render(request, self.template_name, {})


