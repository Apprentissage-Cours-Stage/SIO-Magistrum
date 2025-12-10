from django.shortcuts import get_object_or_404, render, redirect
from dashboards.models import Cours
from users.models import Professeur
from .forms import CoursForm
from django.contrib.auth.decorators import login_required

@login_required
def dashboard_prof(request):
    professeur = request.user.professeur
    liste_cours = Cours.objects.filter(professeur=professeur)
    if request.method == 'POST':
        if 'cours-submit' in request.POST:
            form = CoursForm(request.POST, request.FILES)
            if form.is_valid():
                cours = form.save(commit=False)
                cours.professeur = request.user.professeur
                cours.save()
                return redirect('dashboard_prof')
            else:
                print(form.errors)
    else:
        form = CoursForm()
    matieres = professeur.matieres.all()
    return render(request, 'dashboards/profs/dashboardprof.html', {'cours': liste_cours, 'form': form, 'matieres': matieres})

@login_required
def modify_cours(request, pk):
    professeur = request.user.professeur
    cours = get_object_or_404(Cours, pk=pk, professeur=professeur)
    if request.method == 'POST':
        cours.titre = request.POST.get('titre')
        cours.matiere_id = request.POST.get('matiere')
        cours.type_cours = request.POST.get('type_cours')
        if 'icon' in request.FILES:
            cours.icon = request.FILES['icon']
        if 'banniere' in request.FILES:
            cours.banniere = request.FILES['banniere']
        cours.save()
        return redirect('dashboard_prof')
    return redirect('dashboard_prof')
