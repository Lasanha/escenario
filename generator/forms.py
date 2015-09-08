from generator.models import Esc, MicroblogPost
from django import forms

from django_summernote.widgets import SummernoteWidget


class FormNewEscenario(forms.ModelForm):
    class Meta(object):
        model = Esc
        exclude = ['origem']


class FormNewMicroblogPost(forms.ModelForm):
    class Meta(object):
        model = MicroblogPost
        exclude = ['author']
        widgets = {'text': SummernoteWidget()}