from django import forms
from .models import HeroType

class HeroTypeForm(forms.Form):
    hero_type = forms.ModelChoiceField(queryset=HeroType.objects.all(),label="Select hero type")
    