from django import forms
from .models import Car,Comment

class carform(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        
class commentform(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name','email','body']