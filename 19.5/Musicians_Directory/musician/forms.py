from django import forms
from .models import Musician

class musicianform(forms.ModelForm):
    class Meta:
        model = Musician
        #user k nibo kina dekhbo jodi web a dekhay. exclude korbo user k models theke (musician app)
        exclude = ['user']