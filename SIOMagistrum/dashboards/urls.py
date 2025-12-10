from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/professeur/', views.dashboard_prof, name="dashboard_prof"),
    path('dashboard/professeur/modify/<int:pk>/', views.modify_cours, name="modify_cours"),
    path('dashboard/professeur/cours/<int:pk>/', views.cours_detail, name='cours_detail')
]