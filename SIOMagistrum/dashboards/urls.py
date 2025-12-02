from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('dashboard/professeur/', views.dashboard_prof, name="dashboard_prof")
]