from generator.models import Esc
from django import forms

class FormNewEscenario(forms.ModelForm):
    class Meta(object):
        model = Esc
        exclude = []

