from django import forms
from .models import Brand

class brandform(forms.ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'