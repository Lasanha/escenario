from django.shortcuts import render, redirect
from django.db.models import ObjectDoesNotExist
from django.views.generic.base import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from ipware.ip import get_ip

from generator.forms import FormNewEscenario, FormNewMicroblogPost
from generator.models import EscImg, MicroblogPost


def gera_imagem(esc, autonumber):
    """
    Draw the images, uploads to imgur and saves into EscImg
    :param esc: Escenario with text information
    :param autonumber: automatically give a number True or False
    :return: EscImg instance
    """
    escimg = EscImg(esc=esc)
    if autonumber:
        escimg.autonumber() 
    alvo = escimg.prepare()
    escimg.draw(alvo)
    escimg.upload(alvo)
    escimg.save()
    return escimg


class Home(View):
    """Home View"""
    template_name = 'home.html'

    def get(self, request, **kwargs):
        form = FormNewEscenario()
        recent = EscImg.objects.order_by('-criado_em')[:10]
        try:
            created = EscImg.objects.get(id=kwargs['esc_id'])
        except KeyError:
            created = None
        return render(request, self.template_name, {'form': form, 'recent': recent, 'created': created})

    @staticmethod
    def post(request):
        form = FormNewEscenario(request.POST, request.FILES)
        if form.is_valid():
            ip = get_ip(request)
            esc = form.instance
            if ip is not None:
                esc.origem = ip
            esc.save()
            escimg = gera_imagem(esc, 'autonumber' in request.POST)
            return redirect('view', str(escimg.id))


class About(View):
    """About View"""
    template_name = 'about.html'

    def get(self, request):
        try:
            fixed = MicroblogPost.objects.get(fixed=True)
        except ObjectDoesNotExist:
            fixed = None
        microposts = MicroblogPost.objects.filter(fixed=False).order_by('-created_at')
        return render(request, self.template_name, {'fixed': fixed, 'microposts': microposts})


class List(View):
    """List Escenarios View"""
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


class Restricted(View):
    """Empty, login required view"""
    template_name = 'restricted.html'

    @method_decorator(login_required)
    def get(self, request):
        return render(request, self.template_name, {})


class NewMicroblogPost(View):
    """Post form view"""
    template_name = 'compose.html'

    @method_decorator(login_required)
    def get(self, request):
        form = FormNewMicroblogPost()
        return render(request, self.template_name, {'form': form})

    @staticmethod
    @method_decorator(login_required)
    def post(request):
        form = FormNewMicroblogPost(request.POST, request.FILES)
        if form.is_valid():
            microblog_post = form.instance
            microblog_post.author = request.user
            microblog_post.save()
            return redirect('sobre')
