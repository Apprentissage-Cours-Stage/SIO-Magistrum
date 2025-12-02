from django.urls import path
from . import views

urlpatterns = [
    path('professeur/inscription/', views.inscription_prof,  name="inscription_prof"),
    path('professeur/connexion/', views.prof_login, name="login_prof"),
    path('eleve/connexion/', views.eleve_login, name="eleve_login")
]