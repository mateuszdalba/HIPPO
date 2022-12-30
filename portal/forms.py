from django import forms

class DiseaseForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=300)
    symptoms = forms.CharField(max_length=300)
    intensity = forms.CharField(max_length=100)
    start_date = forms.CharField(max_length=100)

class MedicineForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=300)
    dose = forms.CharField(max_length=300)
    unit = forms.CharField(max_length=100)
    
