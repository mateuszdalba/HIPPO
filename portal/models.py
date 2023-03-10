from django.db import models
from users.models import Profile

class Disease(models.Model):
    """ Class representing diffrent diseases """
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    symptoms = models.CharField(max_length=300)
    intensity = models.IntegerField()
    start_date = models.DateTimeField(auto_now_add=True, blank=True, null = True)
    
    def __str__(self):
        return self.name


class Medicine(models.Model):
    """ Class representing different medicine that is taken """
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    dose = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    unit = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    

class Fasting(models.Model):
    """ Model created for fasting functionality """
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date_start = models.DateTimeField(null=True, blank=True)
    date_end = models.DateTimeField(null=True, blank=True)











