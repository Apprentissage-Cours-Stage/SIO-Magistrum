from django import forms
from django.contrib.auth.models import User
from .models import Professeur, Matiere

class InscriptionProfForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    matieres = forms.ModelMultipleChoiceField(
    queryset=Matiere.objects.all(),
    widget=forms.SelectMultiple(attrs={
        'class': 'select-multiple',
        'size': 5,
    }),  # au lieu de CheckboxSelectMultiple
    required=True
)
    class Meta:
        model = Professeur
        fields = ['pseudo', 'nom', "prenom", "matieres", 'photo']
    
    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data["password"] != cleaned_data['password2']:
            self.add_error("password2", "Les mots de passe ne correspondent pas.")