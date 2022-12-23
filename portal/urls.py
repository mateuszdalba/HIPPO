from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('', views.home, name='home'),
    path('get_disease_data/',views.get_disease_data, name='get_disease_data'),
]