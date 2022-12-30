from django.shortcuts import render
from .forms import StrokeForm
import pickle
import numpy as np


# custom method for generating predictions
def classification(pred_array):
    pred_array_mdl = np.array(pred_array)
    model = pickle.load(open("forecasting/models/first_try_model.sav", "rb"))
    prediction_lbl = model.predict(pred_array_mdl)
    prediction = model.predict_proba(pred_array_mdl)
    return prediction, prediction_lbl

def get_stroke_data(request):

    if request.method == 'POST':

        form = StrokeForm(request.POST)

        if form.is_valid():

            var_heart = form.cleaned_data['heart_disease']
            var_bmi = form.cleaned_data['bmi']
            var_smoke = form.cleaned_data['smoke']
            var_drink = form.cleaned_data['drink']
            var_psychical_health = form.cleaned_data['psychical_health']
            var_mental_health = form.cleaned_data['mental_health']
            var_diff_walking = form.cleaned_data['diff_walking']
            var_sex = form.cleaned_data['sex']
            var_age_cat = form.cleaned_data['age_cat']
            #print(var_age_cat)
            var_race = form.cleaned_data['race']
            var_diab = form.cleaned_data['diab']
            var_psychical_activity = form.cleaned_data['psychical_activity']
            var_general_health = form.cleaned_data['general_health']
            var_sleep = form.cleaned_data['sleep']
            var_asthma = form.cleaned_data['asthma']
            var_kidney = form.cleaned_data['kidney']
            var_skin_cancer = form.cleaned_data['skin_cancer']

            pred_array_ = [[int(var_heart), int(var_bmi), int(var_smoke), int(var_drink), int(var_psychical_health), int(var_mental_health), int(var_diff_walking),
                            int(var_sex),int(var_age_cat), int(var_race), int(var_diab), int(var_psychical_activity), int(var_general_health),
                             int(var_sleep), int(var_asthma), int(var_kidney), int(var_skin_cancer)]]

            #print(pred_array_)

            prediction, prediction_lbl = classification(pred_array_)
           
            return render(request, 'forecasting/stroke_result.html', {'prediction':prediction, 'prediction_lbl':prediction_lbl})

    else:
        form = StrokeForm()

    return render(request, 'forecasting/stroke_pred.html', {'form':form})
