from django import forms

from .models import Binatang

class BinatangForm(forms.ModelForm):


    class Meta:
        model = Binatang
        fields = ('nama', 'umur',)