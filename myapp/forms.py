from django import forms
from .models import *

class FilmKaydet(forms.ModelForm):
    class Meta:
        model = Filmler
        fields = ['title','description','image','is_active','kategori']

     


        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control w-50 '}),
            'description':forms.TextInput(attrs={'class':'form-control w-50 '}),
            
            'image':forms.FileInput(attrs={'class':'form-control w-50'}),
            'is_active':forms.CheckboxInput(attrs={'class':'form-check-input '}),
            'kategori':forms.SelectMultiple(attrs={'class':'form-select w-50 '}),
    }




        