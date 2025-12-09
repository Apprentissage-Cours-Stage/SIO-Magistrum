from django.shortcuts import render, redirect
from dashboards.models import Cours
from django.contrib.auth.decorators import login_required

@login_required
def dashboard_prof(request):
    if not request.user.is_authenticated:
        return redirect("prof_login")
    professeur = request.user.professeur
    cours = Cours.objects.filter(professeur=professeur)
    return render(request, 'dashboards/profs/dashboardprof.html', {'cours': cours})