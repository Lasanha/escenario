from django.views.decorators.cache import cache_page
from django.conf import settings
from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from generator.forms import FormNewMicroblogPost


ESCENARIO_CACHE = getattr(settings, 'ESCENARIO_CACHE', {})
CACHE_NAME = ESCENARIO_CACHE.get('CACHE_NAME', 'default')


class EscenarioBaseCachedView(View):
    template_name = NotImplemented
    cache_config = NotImplemented

    @method_decorator(
        cache_page(
            ESCENARIO_CACHE.get(cache_config, 1),
            cache=CACHE_NAME
        )
    )
    def get(self, request):
        return render(request, self.template_name)


class Home(EscenarioBaseCachedView):
    """Home View"""
    template_name = 'home.html'
    cache_config = 'HOME_TIME'


class List(EscenarioBaseCachedView):
    """List Escenarios View"""
    template_name = 'list.html'
    cache_config = 'LIST_TIME'


class About(EscenarioBaseCachedView):
    """About View"""
    template_name = 'about.html'
    cache_config = 'ABOUT_TIME'


class EscenarioBaseLoggedView(View):
    template_name = NotImplemented

    @method_decorator(login_required)
    def get(self, request):
        return render(request ,self.template_name)


class Restricted(EscenarioBaseLoggedView):
    """Empty, login required view"""
    template_name = 'restricted.html'


class NewMicroblogPost(View):
    """Post form view"""
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
