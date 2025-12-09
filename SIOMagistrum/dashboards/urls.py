from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/professeur/', views.dashboard_prof, name="dashboard_prof")
]