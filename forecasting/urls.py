from django.urls import path
from . import views


urlpatterns = [
    path('get_stroke_data/', views.get_stroke_data, name='get_stroke_data'),
]