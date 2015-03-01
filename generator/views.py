from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.base import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from generator.forms import FormNewEscenario, FormNewMicroblogPost
from generator.models import Esc, EscImg, MicroblogPost
import json


def gera_imagem(esc, autonumber):
    escimg = EscImg(esc=esc)
    if autonumber:
        escimg.autonumber() 
    alvo = escimg.prepare()
    escimg.draw(alvo)
    escimg.upload(alvo)
    escimg.save()
    return escimg


class Home(View):
    template_name = 'home.html'

    def get(self, request, **kwargs):
        form = FormNewEscenario()
        recent = EscImg.objects.order_by('-criado_em')[:10]
        try:
            created = EscImg.objects.get(id=kwargs['esc_id'])
        except Exception:
            created = None
        return render(request, self.template_name, 
            {'form': form, 'recent': recent, 'created': created })


    def post(self, request):
        form = FormNewEscenario(request.POST, request.FILES)
        if form.is_valid():
            esc = form.instance
            esc.save()
            escimg = gera_imagem(esc, 'autonumber' in request.POST)
            return redirect('view', str(escimg.id))


def api_create(request):
    auto = request.GET.get('auto')
    titulo = request.GET.get('titulo')
    faltam = request.GET.get('faltam')
    descricao = request.GET.get('descricao')
    esc = Esc(titulo=titulo,faltam=faltam,descricao=descricao)
    esc.save()
    escimg = gera_imagem(esc, auto)
    link = {'id':escimg.id, 'link':escimg.img_id}
    return HttpResponse(json.dumps(link), content_type='application/json')


class About(View):
    template_name = 'about.html'

    def get(self, request):
        try:
            fixed = MicroblogPost.objects.get(fixed=True)
        except:
            fixed = None
        microposts = MicroblogPost.objects.filter(fixed=False).order_by('-created_at')
        return render(request, self.template_name, {'fixed': fixed, 'microposts': microposts})


class List(View):
    template_name = 'list.html'
    criterio = None

    def get(self, request):
        escimgs = EscImg.objects.order_by(self.criterio)
        paginator = Paginator(escimgs, 20)
        page = request.GET.get('page')
        try:
            escs = paginator.page(page)
        except PageNotAnInteger:
            escs = paginator.page(1)
        except EmptyPage:
            escs = paginator.page(paginator.num_pages)
        zipped = zip(escs[::2], escs[1::2])

        return render(request, self.template_name, {'escs': escs, 'zipped': zipped})


def api_list(request):
    escimgs = EscImg.objects.order_by('-criado_em')
    links = dict([(i.id, i.img_id) for i in escimgs])
    return HttpResponse(json.dumps(links), content_type='application/json')


class Restricted(View):
    template_name = 'restricted.html'

    @method_decorator(login_required)
    def get(self, request):
        return render(request, self.template_name, {})


class NewMicroblogPost(View):
    template_name = 'compose.html'

    @method_decorator(login_required)
    def get(self, request):
        form = FormNewMicroblogPost()
        return render(request, self.template_name, {'form': form})

    @method_decorator(login_required)
    def post(self, request):
        form = FormNewMicroblogPost(request.POST, request.FILES)
        if form.is_valid():
            microblog_post = form.instance
            microblog_post.author = request.user
            microblog_post.save()
            return redirect('sobre')


def api_vote(request, escimg_id):
    escimg = EscImg.objects.get(id=int(escimg_id))
    votos = escimg.gostei()
    escimg.save()
    result = {'id': escimg.id, 'votos': votos}
    return HttpResponse(json.dumps(result), content_type='appliscation/json')
