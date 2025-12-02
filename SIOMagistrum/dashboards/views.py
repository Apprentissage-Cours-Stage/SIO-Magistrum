from django.shortcuts import render, redirect

def dashboard_prof(request):
    if not request.user.is_authenticated:
        return redirect("prof_login")
    return render(request, 'dashboards/profs/dashboardprof.html')