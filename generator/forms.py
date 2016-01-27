from generator.models import Esc, MicroblogPost
from django import forms

from django_summernote.widgets import SummernoteWidget


class FormNewEscenario(forms.ModelForm):
    """Form for Escenario creation"""
    class Meta(object):
        model = Esc
        exclude = ['origem']


class FormNewMicroblogPost(forms.ModelForm):
    """Form for blog posts"""
    class Meta(object):
        model = MicroblogPost
        exclude = ['author']
        widgets = {'text': SummernoteWidget()}
