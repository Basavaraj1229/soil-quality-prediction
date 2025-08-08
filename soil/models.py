from django.db import models

class SoilData(models.Model):
    ph = models.FloatField()
    nitrogen = models.FloatField()
    phosphorus = models.FloatField()
    potassium = models.FloatField()
    organic_carbon = models.FloatField()
    sand = models.FloatField()
    silt = models.FloatField()
    clay = models.FloatField()
    soil_type = models.CharField(max_length=100, blank=True, null=True)
