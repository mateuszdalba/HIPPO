from django.db import models
from users.models import Profile

class Stats(models.Model):
    
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    stroke_prob = models.CharField(max_length=50)
    stroke_lbl = models.CharField(max_length=10)