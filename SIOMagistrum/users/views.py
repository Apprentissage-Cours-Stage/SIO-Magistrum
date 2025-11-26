from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.db import transaction
from .forms import InscriptionProfForm
from .models import Professeur

def eleve_login(request):
    return render(request, 'users/logineleve.html')

@transaction.atomic
def inscription_prof(request):
    if request.method == 'POST':
        form = InscriptionProfForm(request.POST, request.FILES)
        if form.is_valid():
            # Création du User
            user = User.objects.create_user(
                email=form.cleaned_data.get('email',''),
                password=form.cleaned_data['password']
            )
            # Création du Professeur sans matières
            professeur = form.save(commit=False)
            professeur.user = user
            professeur.save()

            # Ajout des matières (ManyToMany)
            form.save_m2m()
            return redirect('prof_login')
    else:
        form = InscriptionProfForm()
    return render(request, 'users/loginprof.html', {'form': form})