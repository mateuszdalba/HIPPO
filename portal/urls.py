from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('', views.home, name='home'),
    path('get_disease_data/',views.get_disease_data, name='get_disease_data'),
    path('get_medicine_data/',views.get_medicine_data, name='get_medicine_data'),
    path('medtent/', views.medtent, name='medtent'),
    path('delete_disease/<int:id>', views.delete_disease, name='delete_disease'),
    path('delete_medicine/<int:id>', views.delete_medicine, name='delete_medicine'),
    path('fasting/', views.fasting, name='fasting')
]