from django.db import models

class Inventorycalculation(models.Model):
    startdate=models.DateField()
    enddate=models.DateField()
    totalsales=models.IntegerField()
