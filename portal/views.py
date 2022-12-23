from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import DiseaseForm


def index(request):
    return HttpResponse("Hello, world. You're at the portal index.")

@login_required
def home(request):
    return render(request, 'portal/home.html')



def get_disease_data(request):
    form_class = DiseaseForm
    form = form_class(request.POST or None)

    if request.method == 'POST':
        form = DiseaseForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form = DiseaseForm()
    return render(request, 'portal/input_diseases.html', {'form' : form})