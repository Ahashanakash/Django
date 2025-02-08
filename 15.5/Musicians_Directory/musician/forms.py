from django import forms
from .models import Musician

class musicianform(forms.ModelForm):
    class Meta:
        model = Musician
        fields = '__all__'