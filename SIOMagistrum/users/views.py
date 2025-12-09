from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.db import transaction
from .forms import InscriptionProfForm
from .models import Professeur

def eleve_login(request):
    return render(request, 'users/logineleve.html')

def prof_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            user = None
        if user:
            user = authenticate(request, username=user.username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard_prof')
        error_message = "Email ou mot de passe incorrect."
        return render(request, 'user/loginprof.html', {"error_message": error_message})
    return render(request, 'users/loginprof.html')

@transaction.atomic
def inscription_prof(request):
    if request.method == 'POST':
        form = InscriptionProfForm(request.POST, request.FILES)
        if form.is_valid():
            # Création du User
            user = User.objects.create_user(
                username=form.cleaned_data['pseudo'],
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
        print(form.errors)
    return render(request, 'users/inscriptionprof.html', {'form': form})