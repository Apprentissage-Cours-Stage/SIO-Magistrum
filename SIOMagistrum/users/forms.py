from django import forms
from django.contrib.auth.models import User
from .models import Professeur, Matiere

class InscriptionProfForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    matieres = forms.ModelMultipleChoiceField(
    queryset=Matiere.objects.all(),
    widget=forms.SelectMultiple(attrs={"id": "matières"}),
    required=True)

    class Meta:
        model = Professeur
        fields = ['pseudo', 'nom', "prenom", "matieres", 'photo']
        widgets = {
            'matières': forms.SelectMultiple(attrs={'id': 'matières'})
        }
    
    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get("password") != cleaned_data.get('password2'):
            self.add_error("password2", "Les mots de passe ne correspondent pas.")
        return cleaned_data
    
    def cleanmatière(self):
        data = self.cleaned_data.get('matieres')
        return data