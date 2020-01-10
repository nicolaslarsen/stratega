from django import forms
from .models import Map, Strategy

class MapForm(forms.ModelForm):
    name = forms.CharField(max_length=50)
    active_duty = forms.BooleanField(initial=True, required=False)

    class Meta:
    	model = Map
    	fields = ('name', 'active_duty')

class StratForm(forms.ModelForm):
    map_name = forms.ModelChoiceField(queryset=Map.objects.all(), required=False, widget=forms.HiddenInput())
    name = forms.CharField(max_length=200)
    description = forms.CharField(widget=forms.Textarea())
    team = forms.ChoiceField(choices=Strategy.TEAM_CHOICES)

    class Meta:
        model = Strategy
        fields = ('map_name', 'name', 'description', 'team')
