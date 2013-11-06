from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import View
from django.views.generic import TemplateView
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from forms import FormNewEscenario
from models import Esc, EscImg

class Home(View):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        form = FormNewEscenario()
        recent = EscImg.objects.order_by('-criado_em')[:10]
        try:
            created = EscImg.objects.get(id=kwargs['esc_id'])
        except:
            created = None
        return render(request, self.template_name, 
            {'form': form, 'recent': recent, 'created': created })


    def post(self, request, *args, **kwargs):
        form = FormNewEscenario(request.POST, request.FILES)
        if form.is_valid():
            esc = form.instance
            esc.save()
            escimg = EscImg(esc=esc)
            if request.POST.has_key('autonumber'):
                escimg.autonumber() 
            escimg.save()
            alvo = escimg.prepare()
            escimg.draw(alvo)
            escimg.upload(alvo)
            return redirect('/view/' + str(escimg.id))


class About(View):
    template_name = 'about.html'

    def get(self, request):
        return render(request, self.template_name, {})


class List(View):
    template_name = 'list.html'

    def get(self, request):
        escimgs = EscImg.objects.order_by('-criado_em')
        paginator = Paginator(escimgs, 20)
        page = request.GET.get('page')
        try:
            escs = paginator.page(page)
        except PageNotAnInteger:
            escs = paginator.page(1)
        except EmptyPage:
            escs = paginator.page(paginator.num_pages)

        return render(request, self.template_name, {'escs': escs})

