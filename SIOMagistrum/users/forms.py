from django import forms
from django.contrib.auth.models import User
from .models import Professeur, Matiere

class InscriptionProfForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    matieres = forms.ModelMultipleChoiceField(
    queryset=Matiere.objects.all(),
    widget=forms.Select(attrs={"id": "matières"})
)
    class Meta:
        model = Professeur
        fields = ['pseudo', 'nom', "prenom", "matieres", 'photo']
        widgets = {
            'matières': forms.Select(attrs={'id': 'matières'})
        }
    
    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data["password"] != cleaned_data['password2']:
            self.add_error("password2", "Les mots de passe ne correspondent pas.")