from generator.models import Esc
from django import forms

class FormNewEscenario(forms.ModelForm):
    class Meta:
        model = Esc
        exclude = []

