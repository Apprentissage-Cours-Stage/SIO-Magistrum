from django import forms
from .models import Cours, Module

class CoursForm(forms.ModelForm):
    class Meta:
        model = Cours
        fields = ['titre', 'matiere', 'type_cours', 'banniere', 'icon']
        widgets = {
            'titre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Titre du cours"}),
            'matiere': forms.Select(attrs={'class': 'form-control'}),
            'type_cours': forms.Select(attrs={'class': 'form-control'})
        }

class ModuleForm(forms.ModelForm):
    class Meta:
        model = Module
        fields = ['titre', 'description', 'ordre']
        widgets = {
            'titre': forms.TextInput(attrs={'id': 'titre_module', 'required': True}),
            'description': forms.Textarea(attrs={'id': 'description_module'}),
            'ordre': forms.NumberInput(attrs={'id': 'ordre_module', 'value': 1, 'min': 1})
        }