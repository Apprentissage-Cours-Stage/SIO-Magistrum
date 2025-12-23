from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/professeur/', views.dashboard_prof, name="dashboard_prof"),
    path('dashboard/professeur/modify/<int:pk>/', views.modify_cours, name="modify_cours"),
    path('dashboard/professeur/delete/<int:pk>/', views.delete_cours, name='delete_cours'),
    path('dashboard/professeur/cours/<int:pk>/', views.cours_detail, name='cours_detail'),
    path('dashboard/professeur/cours/modify/<int:pk>/', views.modify_module, name="modify_module"),
    path('dashboard/professeur/cours/delete/<int:pk>/', views.delete_module, name="delete_module"),
    path('dashboard/professeur/cours/module/<int:pk>/', views.module_detail, name="module_detail"),
    path('dashboard/professeur/cours/module/exercices/test-docker/', views.tester_code_docker, name='tester_code_docker')
]