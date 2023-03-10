from django import forms

age_options = (
         ('9','65-69'),('8','60-64'),('10','70-74'),
         ('7','55-59'),('6','50-54'),('12','80 or older'),
         ('11','75-79'),('0','18-24'),('4','40-44'),
         ('3','35-39'),('2','30-34'),('1','25-29'))

races = (
    ('0','American Indian/Alaskan Native'),
    ('1','Asian'),
    ('2','Black'),
    ('3','Hispanic'),
    ('4','Other'),
    ('5','White'))

diabetes = (
    ('0','No'),
    ('2','Yes'),
    ('1','No,borderline diabetes'),
    ('3','Yes (during pregnancy)')
)

gen_h = (
    ('3','Poor'),
    ('1','Fair'),
    ('2','Good'),
    ('4','Very Good'),
    ('0','Excellent')
    )

sex_options = (
    ('0','Female'),
    ('1', 'Male')
)

class StrokeForm(forms.Form):
    # 0 - Female, 1 - Male
    sex = forms.ChoiceField(choices=sex_options ,label='Sex')
    age_cat = forms.ChoiceField(choices = age_options, label='Age')
    #White - 5, Hispanic - 3, Black - 2, Other - 4, Asian - 1, American Indian/Alaskan Native - 0
    race = forms.ChoiceField(choices = races, label='Race')
    bmi = forms.FloatField(max_value=120, min_value=0, label='BMI')

    smoke = forms.BooleanField(label='Smoking')
    drink = forms.BooleanField(label='Drinking')
    general_health = forms.ChoiceField(choices = gen_h, label='Gen Health')
    psychical_activity = forms.BooleanField(label='Psychical Activity')
    psychical_health = forms.IntegerField(max_value=30, min_value=0, label='Psychical Health')
    mental_health = forms.IntegerField(max_value=30, min_value=0, label='Psychical Health')

    sleep = forms.IntegerField(max_value=24, min_value=1, label='On average, how many hours of sleep do you get in a 24-hour period?')

    #0 - No, 1 - Yes
    heart_disease = forms.BooleanField(label='Heart Disease (CHD or MI)')
    diff_walking = forms.BooleanField(label='Diff Walking')
    #0 - No, Yes - 2, No, borderline diabetes - 1, 
    diab = forms.ChoiceField(choices = diabetes, label='Diabetic')
    asthma = forms.BooleanField(label='Do you have Asthma?')
    kidney = forms.BooleanField(label='Kidney Disease?')
    skin_cancer = forms.BooleanField(label='Ever had skin cancer?')