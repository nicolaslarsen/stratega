from django import forms
from django.forms.models import inlineformset_factory
from .models import Map, Strategy, Nade, Bullet

class MapForm(forms.ModelForm):
    name = forms.CharField(max_length=50)
    active_duty = forms.BooleanField(initial=True, required=False)

    class Meta:
    	model = Map
    	fields = ('name', 'active_duty')

class StratForm(forms.ModelForm):
    map_name = forms.ModelChoiceField(queryset=Map.objects.all(), required=False, widget=forms.HiddenInput())
    name = forms.CharField(max_length=200)
    team = forms.ChoiceField(choices=Strategy.TEAM_CHOICES)

    class Meta:
        model = Strategy
        fields = ('map_name', 'name', 'team')

class NadeForm(forms.ModelForm):
    map_name = forms.ModelChoiceField(queryset=Map.objects.all(), required=False, widget=forms.HiddenInput())
    name = forms.CharField(max_length=200)
    description = forms.CharField(widget=forms.Textarea(), required=False)
    nade_type = forms.ChoiceField(choices=Nade.NADE_TYPE_CHOICES)
    img = forms.ImageField(required=False)
    img_link = forms.URLField(required=False)

    class Meta:
        model = Nade
        fields = ('map_name', 'name', 'description', 'nade_type', 'img', 'img_link')
