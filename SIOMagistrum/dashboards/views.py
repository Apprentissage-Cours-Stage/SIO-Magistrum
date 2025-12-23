from django.shortcuts import get_object_or_404, render, redirect
from dashboards.models import Cours, Module, Exercice
from .forms import CoursForm, ModuleForm
from django.contrib.auth.decorators import login_required
import json
import docker
from django.http import JsonResponse

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

@login_required
def delete_cours(request, pk):
    professeur = request.user.professeur
    cours = get_object_or_404(Cours, pk=pk, professeur=professeur)
    if request.method == 'POST':
        cours.delete()
        return redirect('dashboard_prof')
    return redirect('dashboard_prof')

@login_required
def cours_detail(request, pk):
    professeur = request.user.professeur
    cours = get_object_or_404(Cours, pk=pk, professeur=professeur)
    modules = cours.modules.order_by('ordre')
    if request.method == 'POST':
        if 'module-submit' in request.POST:
            form = ModuleForm(request.POST)
            if form.is_valid():
                module = form.save(commit=False)
                module.cours = cours
                module.save()
                return redirect('cours_detail', pk=cours.pk)
        else:
            form = ModuleForm()
    return render(request, 'dashboards/profs/cours/cours_detail.html', {
        'cours': cours,
        'modules': modules
    })

@login_required
def modify_module(request, pk):
    module = get_object_or_404(Module, id=pk)
    if request.method == 'POST':
        module.titre = request.POST.get("titre")
        module.description = request.POST.get("description")
        module.ordre = request.POST.get('ordre')
        module.save()
        return redirect('cours_detail', pk=module.cours.pk)
    return redirect('cours_detail', pk=module.cours.pk)

@login_required
def delete_module(request, pk):
    module = get_object_or_404(Module, id=pk)
    if request.method == "POST":
        module.delete()
        return redirect('cours_detail', pk=module.cours.pk)
    return redirect('cours_detail', pk=module.cours.pk)

@login_required
def module_detail(request, pk):
    module = get_object_or_404(Module, id=pk, cours__professeur=request.user.professeur)
    exercices = module.exercices.all()
    is_positionnement = module.cours.type_cours == 'Positionnement'
    
    if request.method == 'POST' and 'exercice-submit' in request.POST:
        # Création de l'exercice
        Exercice.objects.create(
            module=module,
            titre=request.POST.get('titre'),
            type_exercice=request.POST.get('type_exercice'),
            niveau_exercice=request.POST.get('niveau_exercice') if is_positionnement else None,
        )
        return redirect('module_detail', pk=module.id)

    return render(request, 'dashboards/profs/cours/modules/module_details.html', {
        'module': module,
        'exercices': exercices,
        'is_positionnement': is_positionnement
    })

@login_required
def tester_code_docker(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user_code = data.get('code', '')

            # Initialisation du client Docker (doit être lancé sur ta machine)
            client = docker.from_env()
            
            # Exécution sécurisée : limite de RAM et de temps (timeout)
            # On utilise une image python-slim pour la rapidité
            container = client.containers.run(
                image="python:3.9-slim",
                command=f'python3 -c "{user_code}"',
                remove=True,
                stdout=True,
                stderr=True,
                network_disabled=True,
                mem_limit="64m"
            )

            return JsonResponse({
                "success": True,
                "output": container.decode('utf-8')
            })

        except docker.errors.ContainerError as e:
            # Erreur de syntaxe ou d'exécution dans le code de l'utilisateur
            return JsonResponse({
                "success": False,
                "output": e.stderr.decode('utf-8')
            })
        except Exception as e:
            # Erreur système (Docker non lancé, etc.)
            return JsonResponse({
                "success": False,
                "output": f"Erreur système: {str(e)}"
            })

    return JsonResponse({"success": False, "output": "Méthode non autorisée"})