from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import View
from django.views.generic import TemplateView
from django.template import RequestContext

from forms import FormNewEscenario
from models import Esc, EscImg

class Home(View):
    template_name = 'home.html'

    def get(self, request):
        form = FormNewEscenario()
        recent = EscImg.objects.order_by('-criado_em')[:10]
        return render(request, self.template_name, 
            {'form': form, 'recent': recent })

    def post(self, request):
        form = FormNewEscenario(request.POST, request.FILES)
        if form.is_valid():
            esc = form.instance
            esc.save()
            escimg = EscImg(esc=esc)
            escimg.save()
            escimg.draw()
            return redirect('/view/' + str(escimg.id))


class EscView(View):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        form = FormNewEscenario()
        recent = EscImg.objects.order_by('-criado_em')[:10]
        created = EscImg.objects.get(id=kwargs['esc_id'])
        return render(request, self.template_name, 
            {'form': form, 'recent': recent, 'created': created })
