from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import DiseaseForm, MedicineForm
from .models import Disease, Medicine
from users.models import Profile
import pandas as pd
import json
from django.contrib import messages
from django.shortcuts import get_object_or_404
#from django.core.urlresolvers import reverse
from django_pandas.io import read_frame

def index(request):
    return HttpResponse("Hello, world. You're at the portal index.")

@login_required
def home(request):
    return render(request, 'portal/home.html')



def get_disease_data(request):
    """ Method to get Disease from User form """
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

            messages.success(request, 'Successfully added new disease to database!')
           
        else:
            form = DiseaseForm()
    return render(request, 'portal/input_diseases.html', {'form' : form})


def get_medicine_data(request):
    """ Method to get Medicine from User form """
    form_class = MedicineForm
    form = form_class(request.POST or None)
    
    if request.method == 'POST':
        form = MedicineForm(request.POST)

        if form.is_valid():
            
            cd = form.cleaned_data

            current_user = request.user.id

            d = Medicine(
                user_id = Profile.objects.get(user=current_user),
                name = cd['name'],
                description = cd['description'],
                dose = cd['dose'],
                unit = cd['unit']
            )
            d.save()

            messages.success(request, 'Successfully added new medicine to your database!')
           
        else:
            form = MedicineForm()
    return render(request, 'portal/input_medicine.html', {'form' : form})



def medtent(request):

    #Diseases
    qs = Disease.objects.all()
    df = read_frame(qs)

    # parsing the DataFrame in json format.
    json_records = df.reset_index().to_json(orient ='records')
    data = []
    data = json.loads(json_records)

    #Medicine
    qs2 = Medicine.objects.all()
    df2 = read_frame(qs2)
    json_records2 = df2.reset_index().to_json(orient ='records')
    data2 = []
    data2 = json.loads(json_records2)

    context = {'d': data, 'm': data2}

    return render(request, 'portal/medtent.html', context)


def delete_disease(request, id):
    disease = Disease.objects.get(id=id)

    if request.method == 'POST':
        #delete disease from database
        disease.delete()
        #redirect to disease list
        return redirect('medtent')

    

def delete_medicine(request, id):
    medicine = Medicine.objects.get(id=id)

    if request.method == 'POST':
        #delete disease from database
        medicine.delete()
        #redirect to disease list
        return redirect('medtent')
    