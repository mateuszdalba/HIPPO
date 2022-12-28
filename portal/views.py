from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import DiseaseForm
from .models import Disease
from users.models import Profile
import pandas as pd
import json
from django.contrib import messages

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
            
            cd = form.cleaned_data

            current_user = request.user.id

            d = Disease(
                user_id = Profile.objects.get(user=current_user),
                name = cd['name'],
                description = cd['description'],
                symptoms = cd['symptoms'],
                intensity = cd['intensity'],
                start_date = cd['start_date']
            )
            d.save()

            messages.success(request, 'Successfully added new disease in database!')
           
        else:
            form = DiseaseForm()
    return render(request, 'portal/input_diseases.html', {'form' : form})


from django_pandas.io import read_frame

def medtent(request):
    qs = Disease.objects.all()
    df = read_frame(qs)

    # parsing the DataFrame in json format.
    json_records = df.reset_index().to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    context = {'d': data}

    return render(request, 'portal/medtent.html', context)
    