from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import View
from django.views.generic import TemplateView
from django.template import RequestContext

from forms import FormNewEscenario

class Home(View):
    template_name = 'home.html'

    def get(self, request):
        form = FormNewEscenario()
        return render(request, self.template_name, 
            {'form': form })

    def post(self, request):
        form = FormNewEscenario(request.POST, request.FILES)
        if form.is_valid():
            exp = form.instance
            exp.save()
            return redirect('/')
        

