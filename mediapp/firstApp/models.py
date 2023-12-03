from django.db import models

# Create your models here.
from django.db import models
from django.contrib import admin
class snh(models.Model):
    age = models.FloatField()
    sex = models.IntegerField()
    cp = models.FloatField()
    trestbps = models.FloatField()
    chol = models.FloatField()
    fbs = models.FloatField()
    restecg = models.FloatField()
    thalach = models.FloatField()
    exang = models.FloatField()
    oldpeak = models.FloatField()
    slope = models.FloatField()
    ca = models.FloatField()
    thal = models.FloatField()

    def _str_(self):
        return f"snh object: {self.age} - {self.sex} - {self.cp} - {self.trestbps} - {self.chol} - {self.fbs} - {self.restecg} - {self.thalach} - {self.exang} - {self.oldpeak} - {self.slope} - {self.ca} - {self.thal}"