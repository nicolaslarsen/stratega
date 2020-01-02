from django import forms
from .models import Map, Strategy

class MapForm(forms.Form):
    name = forms.CharField(max_length=50)

class StratForm(forms.ModelForm):
    map_name = forms.ModelChoiceField(queryset=Map.objects.all())
    name = forms.CharField(max_length=200)
    description = forms.CharField(widget=forms.Textarea)
    team = forms.ChoiceField(choices=[('CT', 'CT'), ('T', 'T')])

    class Meta:
        model = Strategy
        fields = ('name', 'map_name', 'description', 'team')
