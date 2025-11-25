from django.shortcuts import render

def prof_login(request):
    return render(request, 'user/loginprof.html')

def eleve_login(request):
    return render(request, 'users/logineleve.html')
