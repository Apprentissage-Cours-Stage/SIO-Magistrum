from django import forms
from .models import Cours
from users.models import Matiere

class CoursForm(forms.ModelForm):
    class Meta:
        model = Cours
        fields = ['titre', 'matiere', 'type_cours', 'banniere', 'icon']
        widgets = {
            'titre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Titre du cours"}),
            'matiere': forms.Select(attrs={'class': 'form-control'}),
            'type_cours': forms.Select(attrs={'class': 'form-control'})
        }