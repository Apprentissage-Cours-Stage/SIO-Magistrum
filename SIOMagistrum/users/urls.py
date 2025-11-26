from django.urls import path
from . import views

urlpatterns = [
    path('professeur/connexion/', views.inscription_prof,  name="prof_login"),
    path('eleve/connexion/', views.eleve_login, name="eleve_login")
]