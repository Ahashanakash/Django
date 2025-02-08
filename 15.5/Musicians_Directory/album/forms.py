from django import forms
from .models import album

class albumform(forms.ModelForm):
    class Meta:
        model = album
        fields = '__all__'
        widgets = {
            'Album_release_date': forms.DateInput(attrs={'type': 'date'}),
        }